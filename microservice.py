from flask import Flask, request
import json

# plant watering database
database: dict = {}
with open ("db.json", "r") as f :
    database = json.load(f)

app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns if plant need watering when we use GET method

@app.route('/plantwatering', methods=['GET'])
def home():
    if (request.method == 'GET'):
        plant = request.args.get('plant')
        days = request.args.get('days')
        if plant in database.keys():
            if int(days) >= database[plant]:
                response = "plant needs water"
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                response = "plant does not need water"
                response.headers['Access-Control-Allow-Origin'] = '*'
                return response
        else:
            response = "plant is not in the database"
            response.headers['Access-Control-Allow-Origin'] = '*'
            return response

# driver function
if __name__ == '__main__':
    app.run(debug=True)