import falcon
from models import Task, TaskSchema
import json
from ai . foundation import LMMistral

task_schema = TaskSchema()

class TaskCollectionResource:
    def on_get(self, req, resp):
        # Get all tasks
        tasks = [
            Task(id=1, title='Task 1', description='Description for Task 1', status='done'),
            Task(id=2, title='Task 2', description='Description for Task 2'),
            Task(id=3, title='Task 3', description='Description for Task 3'),
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
        ai_suggestion = Ai._ai()

        if task:
            resp.body = task_schema.dumps(task, ai_suggestion)
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


class AiModel:

    def __init__(self):
        pass


    def _generate_bot_response(self, prompt, task_id, title, description):
        
        self.mistral_instance = LMMistral()

        self.task_id = TaskCollectionResource.id
        self.title = TaskCollectionResource.title
        self.description = TaskCollectionResource.description

        try:
            prompt = f"""<s>[INST]Based on the following task, can you give the user tips and recommendations to finish them well?. 
            Task ID: {task_id}, Title: {title}, and Description: {description}            
            [/INST]"""
            
            result = self.mistral_instance.pipe(prompt)

            return result[0]['generated_text']
        except Exception as e:
            print(f"Error in inference: {e}")

            return None

    def fitness_ai(self, prompt):
        return self._generate_bot_response(prompt, 'FitMateBot')

class Ai:
    def _ai():
        result = AiModel._generate_bot_response()

        return result