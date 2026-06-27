# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: CourseBoard
import json, os, sys

def load_courses(filepath='courses.json'):
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден.")
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and 'courses' in data:
            return data['courses']
        else:
            print("Неверный формат данных JSON.")
            return []
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        print(f"Произошла неизвестная ошибка при чтении файла: {e}")
        return []

if __name__ == "__main__":
    courses = load_courses()
    if courses:
        for c in courses:
            print(c.get('title', 'Без названия'))
