from flask import Flask, jsonify, request
app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Изучить gRPC", "status": "pending"},
    {"id": 2, "title": "Настроить Nginx", "status": "done"}
]

# 1. GET все задачи
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# 2. GET одна задача
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for t in tasks:
        if t['id'] == task_id:
            return jsonify(t), 200
    return jsonify({"error": "Не найдено"}), 404

# 3. POST создать задачу
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({"error": "Нужен title"}), 400
    
    new_id = max([t['id'] for t in tasks], default=0) + 1
    task = {"id": new_id, "title": data['title'], "status": "pending"}
    tasks.append(task)
    return jsonify(task), 201

# 4. PUT обновить статус
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    for t in tasks:
        if t['id'] == task_id:
            t['status'] = 'done'
            return jsonify(t), 200
    return jsonify({"error": "Не найдено"}), 404

# 5. DELETE задачу
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

if __name__ == '__main__':
    app.run(port=5000)