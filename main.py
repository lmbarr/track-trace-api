from flask import Flask, request, jsonify
from mongodb import get_mongo_db_connection
from weather import get_current_weather, UNAVAILABLE_MESSAGE
from redis_cache import set_cache_value, get_cache_value
from dotenv import load_dotenv
import sys


load_dotenv()
client = get_mongo_db_connection()
app = Flask(__name__)


@app.route("/article", methods=['GET'])
def get_article():
    args = request.args
    tracking_number = args.get('tracking_number')
    carrier = args.get('carrier')

    if tracking_number is None or carrier is None:
        return 'Bad request', 400

    try:
        shipment = client['Shipment']
        articles_collection = shipment["articles"]
        record = articles_collection.find_one({'tracking_number': tracking_number, 'carrier': carrier})

        if record is None:
            return {}, 200

    except Exception as e:
        print('DB error ', e)
        return 'Internal Server Error', 500

    weather = get_weather(tracking_number, carrier, record.get('receiver_address'))
    record.pop('_id')
    return jsonify({"weather": weather, **record}), 200


def get_weather(tracking_number, carrier, receiver_address):

    if receiver_address is None:
        return ''

    key = tracking_number + ':' + carrier
    weather = get_cache_value(key)

    if weather:
        return weather
    else:
        try:
            weather = get_current_weather(receiver_address)
        except Exception as e:
            print('Response format invalid ', e)
            weather = UNAVAILABLE_MESSAGE

        if weather and weather != UNAVAILABLE_MESSAGE:
            set_cache_value(tracking_number + ':' + carrier, weather)

        return weather


if __name__ == '__main__':
    host = sys.argv[1]
    app.run(host=host, port=5000)



