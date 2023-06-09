from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from sqladmin import Admin as AdminView, ModelView
from sqladmin.authentication import AuthenticationBackend
from utils.db_api.models import User, Channel, Audio, Admin

from loader import db
from data.config import BASE_URL


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        request.session.update({"token": "123"})
        form = await request.form()

        await db.load()
        resp = await db.get_admin(form['username'], form['password'])
        
        if resp:
            return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> Optional[RedirectResponse]:
        if not "token" in request.session:
            return RedirectResponse(request.url_for("admin:login"), status_code=302)


app = FastAPI()
engine = db.get_engine()
authentication_backend = AdminAuth(secret_key="123")
admin = AdminView(app=app, engine=engine, base_url=BASE_URL, authentication_backend=authentication_backend)


class UserAdmin(ModelView, model=User):
    column_list = [User.user_id, User.username, User.first_name]
    can_create = False
    can_edit = False
    can_delete = False
    icon = "fa-solid fa-user"

    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True


class ChannelAdmin(ModelView, model=Channel):
    column_list = [Channel.chat_id, Channel.title]
    can_create = False
    can_edit = False
    icon = "fa-solid fa-user"

    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True
   

class AudioAdmin(ModelView, model=Audio):
    column_list = [Audio.text, Audio.distination]
    can_create = False
    can_edit = False
    icon = "fa-solid fa-user"
    
    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True


class AdminAdmin(ModelView, model=Admin):
    column_list = [Admin.username, Admin.password]
    icon = "fa-solid fa-user"
    
    def is_visible(self, request: Request) -> bool:
        return True

    def is_accessible(self, request: Request) -> bool:
        return True


admin.add_view(UserAdmin)
admin.add_view(ChannelAdmin)
admin.add_view(AudioAdmin)
admin.add_view(AdminAdmin)