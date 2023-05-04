from datetime import datetime


class UserRequest():
    name: str
    email: str
    service: str
    message: str
    created_at: datetime = datetime.now()
