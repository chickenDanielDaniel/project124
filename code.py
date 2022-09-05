from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': u'Buy groceries',
        'name': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'contact': u'Learn Python',
        'name': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")
def helloworld():
    return "This is python"

@app.route("/get-data")
def gettasks():
    return jsonify({
        "data":tasks
    })

@app.route("/add-data", methods = ["POST"])
def addtasks():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "Please provide your data"
        },400)

    task = {
        'id':tasks[-1]['id'] + 1,
        'contact':request.json['contact'],
        'name':request.json['name'],
        'done': False
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Contact added successfully"
    })
    
if __name__ == "__main__":
    app.run(debug = True)