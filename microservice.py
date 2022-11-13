from flask import Flask, request
import json

Access-Control-Allow-Origin: *

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
                return "plant needs water"
            else:
                return "plant does not need water"
        else:
            return "plant is not in the database"

# driver function
if __name__ == '__main__':
    app.run(debug=True)