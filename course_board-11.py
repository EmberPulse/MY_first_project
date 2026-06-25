# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: CourseBoard
import json, os

DATA_FILE = "courseboard_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"[Error] Не удалось сохранить данные: {e}")
        return False

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"courses": [], "user_id": None}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Восстановление структуры по умолчанию если файл повреждён
        if not isinstance(data.get("courses"), list):
            return {"courses": [], "user_id": None}
        return data
    except Exception:
        return {"courses": [], "user_id": None}

def init_storage():
    save_state(load_state())
