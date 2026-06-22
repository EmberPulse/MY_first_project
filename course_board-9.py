# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: CourseBoard
import json, os

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки."""
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        
        # Валидация структуры данных
        required_keys = {"courses", "users"}
        missing_keys = required_keys - set(data.keys())
        if missing_keys:
            raise KeyError(f"Отсутствуют ключи: {missing_keys}")
        
        return data
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return {}

# Пример использования (раскомментируйте для тестирования):
# initial_json = '{"courses": [{"id": 1, "name": "Python", "modules": []}], "users": []}'
# course_board_data = load_initial_data(initial_json)
