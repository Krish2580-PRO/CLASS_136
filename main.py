from data import data

from flask import Flask , jsonify , request

# creating the object for the Flask
# objectname = classNme()
app = Flask(__name__)

@app.route("/data")

def showData():
    return jsonify({
        "data" :    data,
        "message" : "success"         
    })


@app.route("/planet")

def planet():
    name = request.args.get("name")
    pData = next(i for i in data if i["name"] == name )

    return jsonify({
        "data" : pData,
        "message" : "success"
    })

# http://127.0.0.1:5000/planet?name=



if __name__ == "__main__":
    app.run()







