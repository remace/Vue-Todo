from flask_marshmallow import Marshmallow

from .views import app

ma = Marshmallow(app)

class TodoSchema(ma.Schema):
    class Meta:
        fields = ('id','title','description','created_at', 'updated_at', 'visible', 'done')

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)