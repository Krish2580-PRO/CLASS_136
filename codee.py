from dataa import data

from flask import Flask , jsonify , request

app = Flask(__name__)

@app.route("/")

def star():
    return jsonify ({
        "data" : data,
        "message" : "sucess"
    })

@app.route("/star")

def shtar():
    name = request.args.get("name")
    sData = next( i for i in data if i["name"] == name )
    return jsonify({
         "data" : sData,
        "message" : "sucess"
    })



if __name__ == "__main__":
    app.run ()