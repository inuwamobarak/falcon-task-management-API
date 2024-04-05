import falcon
from resources import TaskCollectionResource, TaskResource

api = falcon.API()

task_collection_resource = TaskCollectionResource()
task_resource = TaskResource()

api.add_route('/tasks', task_collection_resource)
api.add_route('/tasks/{task_id}', task_resource)