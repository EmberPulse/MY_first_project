# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: CourseBoard
import json
from datetime import datetime, timedelta
from pathlib import Path

# Конфигурация и демо-данные
COURSES = [
    {
        "id": 1,
        "title": "Основы Python",
        "modules": [
            {"id": 101, "name": "Введение", "tasks": [{"id": 1001, "desc": "Установка окружения", "deadline": datetime.now() + timedelta(days=2), "done": False}]},
            {"id": 102, "name": "Переменные", "tasks": [{"id": 1002, "desc": "Типы данных", "deadline": datetime.now() + timedelta(days=5), "done": True}]}
        ]
    },
    {
        "id": 2,
        "title": "Веб-разработка",
        "modules": [
            {"id": 201, "name": "HTML/CSS", "tasks": [{"id": 2001, "desc": "Семантика", "deadline": datetime.now() + timedelta(days=10), "done": False}]}
        ]
    }
]

def load_data():
    """Загрузка данных из JSON или использование демо-данных."""
    data_file = Path("courseboard.json")
    if data_file.exists():
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Ошибка чтения файла данных. Используются демо-данные.")
    return COURSES

def save_data(data):
    """Сохранение данных в JSON файл."""
    data_file = Path("courseboard.json")
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_progress(course_id):
    """Вычисление прогресса курса (процент выполненных задач)."""
    course = next((c for c in COURSES if c["id"] == course_id), None)
    if not course:
        return 0
    total_tasks = sum(len(m["tasks"]) for m in course["modules"])
    done_tasks = sum(1 for m in course["modules"] for t in m["tasks"] if t["done"])
    return (done_tasks / total_tasks * 100) if total_tasks > 0 else 0

def print_dashboard():
    """Вывод дашборда с курсами и прогрессом."""
    data = load_data()
    for course in data:
        print(f"\nКурс: {course['title']}")
        print(f"Прогресс: {get_progress(course['id']):.1f}%")
        for module in course["modules"]:
            print(f"  Модуль: {module['name']}")
            for task in module["tasks"]:
                status = "✓" if task["done"] else "○"
                due = task["deadline"].strftime("%d.%m")
