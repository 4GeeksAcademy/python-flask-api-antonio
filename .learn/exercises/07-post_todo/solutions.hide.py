from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    task = request_body.get('label')

    new_todo = {
        'id': len(todos) + 1,
        'task': task,
        'done': False
    }
    todos.append(new_todo)
    return jsonify({ "message" : "task successfully added" })


# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
