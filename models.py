from marshmallow import Schema, fields

class Task:
    def __init__(self, id, title, description, status='todo'):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

class TaskSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    status = fields.Str()
