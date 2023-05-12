from fastapi import FastAPI
from sqladmin import Admin, ModelView

from utils.db_api.models import User, Channel, Audio

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
   

class ChannelAdmin(ModelView, model=Channel):
    column_list = [Channel.chat_id, Channel.title]
    can_create = False
    can_edit = False
    can_delete = False
    icon = "fa-solid fa-user"
   

class AudioAdmin(ModelView, model=Audio):
    column_list = [Audio.text, Audio.distination]
    can_create = False
    can_edit = False
    can_delete = False
    icon = "fa-solid fa-user"
   

admin.add_view(UserAdmin)
admin.add_view(ChannelAdmin)
admin.add_view(AudioAdmin)