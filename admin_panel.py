from fastapi import FastAPI
from sqladmin import Admin, ModelView

from utils.db_api.models import User

from loader import db

engine = db.get_engine()

app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.user_id, User.username, User.first_name]
    can_create = False
    can_edit = False
    can_delete = False
    icon = "fa-solid fa-user"
   

admin.add_view(UserAdmin)