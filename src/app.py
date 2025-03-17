from flask import Flask , request , jsonify

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def obtener_todos():
    return jsonify(todos), 200

@app.route('/todos' , methods=['POST'])
def agregar_todo():
   datos = request.get_json()
   # print(datos_todo)
   tarea = datos.get('label') 

   nuevo_todo = {
        'id': len(todos) + 1,
        'tarea': tarea,
        'done': False
    }
   todos.append(nuevo_todo)
   return jsonify({ "mensaje" : "Tarea agregada con exito"})

@app.route('/todos/<int:id>', methods=['DELETE'])
def eliminar_todo(id):
    tarea_a_eliminar = None
    for tarea in todos:
       if tarea['id'] == id:
          tarea_a_eliminar = tarea
          break
       
    todos.remove(tarea)
    return jsonify({"mensaje": "Tarea eliminada con exito."}), 200



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)