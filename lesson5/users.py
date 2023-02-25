from pprint import pprint

JSON_DATA = [
    {"username": "jack1994", "email": "jsads@mail.com", "is_active": True},
    {"username": "jaoh1994", "email": "ohal@mail.com", "is_active": True},
    {"username": "mamama", "email": "amamam@mail.com", "is_active": False},
    {"username": "alskdja", "email": "asldka@mail.com", "is_active": True},
]


class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.username}"

    @classmethod
    def from_json(cls, json_data):
        return [cls(**x) for x in json_data if x['is_active']]  # cls == User

    @classmethod
    def get_from_db_by_id(cls, id, db_engine):
        query = f"""select * from user where id = {id}"""
        result = db_engine.execute_query(query)
        return User(**result)


if __name__ == '__main__':
    users_list_from_json = User.from_json(JSON_DATA)
    pprint(users_list_from_json)
