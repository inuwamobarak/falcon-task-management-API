import falcon
from models import Task, TaskSchema
import json

task_schema = TaskSchema()

class TaskCollectionResource:
    def on_get(self, req, resp):
        # Get all tasks
        tasks = [
            Task(id=1, title='Task 1', description='Description for Task 1', status='done'),
            Task(id=2, title='Task 2', description='Description for Task 2'),
        ]
        # Serialize tasks using TaskSchema
        tasks_data = task_schema.dump(tasks, many=True)
        resp.body = json.dumps(tasks_data)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        # Deserialize request body using TaskSchema
        task_data = task_schema.load(json.loads(req.stream.read().decode('utf-8')))
        task = Task(id=task_data['id'], title=task_data['title'], description=task_data['description'])
        # Save the task (e.g., in a database)
        # Return the created task with status code 201
        resp.body = task_schema.dumps(task)
        resp.status = falcon.HTTP_201

class TaskResource:
    def on_get(self, req, resp, task_id):
        # Get task by ID (e.g., from a database)
        task = Task(id=task_id, title=f'Task {task_id}', description=f'Description for Task {task_id}')
        # Check if task exists
        if task:
            resp.body = task_schema.dumps(task)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404

    def on_put(self, req, resp, task_id):
        # Update task by ID (e.g., in a database)
        task_data = task_schema.load(json.loads(req.stream.read().decode('utf-8')))
        task = Task(id=task_id, title=task_data['title'], description=task_data['description'])
        # Save the updated task
        # Return the updated task
        resp.body = task_schema.dumps(task)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, task_id):
        # Delete task by ID (e.g., from a database)
        # Set response status code
        resp.status = falcon.HTTP_204