# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: CourseBoard
import json, os, uuid

class UserProfile:
    def __init__(self, username, email="", avatar=""):
        self.id = str(uuid.uuid4())[:8]
        self.username = username
        self.email = email
        self.avatar = avatar or f"avatars/{username.lower()}.png"
        self.progress = {}

    @property
    def display_name(self):
        return self.username if self.avatar else f"@{self.username}"


class UserStore:
    def __init__(self, path="data/users.json"):
        self.path = path
        self.data = self._load()

    def _load(self):
        try:
            with open(self.path) as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=2)

    def get(self, username):
        if not self.data:
            return None
        for user in self.data.values():
            if user["username"] == username:
                return UserProfile(**user)
        return None

    def create(self, username, email=""):
        if username in {u["username"] for u in self.data.values()}:
            return None
        profile = {"id": str(uuid.uuid4())[:8], "username": username, "email": email}
        self.data[username] = profile
        self.save()
        return UserProfile(**profile)

    def all(self):
        if not self.data:
            return []
        return [UserProfile(**u) for u in self.data.values()]
