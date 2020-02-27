from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model


class ToDoModel(Model):
    class Meta:
        host = 'http://localhost:18000'
        table_name = 'todo'
        region = 'us-west-1'
        write_capacity_units = 10
        read_capacity_units = 10

    user_id = UnicodeAttribute(hash_key=True)
