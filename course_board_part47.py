# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: CourseBoard
def demo():
    print("=== CourseBoard Demo ===\n")
    courses = CourseBoard()
    courses.add("Python для начинающих", [
        ("Введение в Python", [
            {"name": "Установка", "description": "Установи Python 3.12", "deadline": "2024-01-10", "points": 5, "done": True},
            {"name": "Первая программа", "description": "Напечатай 'Hello, World!'", "deadline": "2024-01-12", "points": 10, "done": False},
        ]),
        ("Основы Python", [
            {"name": "Переменные", "description": "Изучи типы данных", "deadline": "2024-01-15", "points": 15, "done": True},
            {"name": "Функции", "description": "Напиши три функции", "deadline": "2024-01-20", "points": 20, "done": False},
        ]),
    ])
    courses.add("JavaScript", [
        ("Основы JS", [
            {"name": "Переменные", "description": "var, let, const", "deadline": "2024-01-18", "points": 10, "done": True},
            {"name": "DOM", "description": "Работа с DOM", "deadline": "2024-01-25", "points": 25, "done": False},
        ]),
    ])
    courses.add("Web-разработка", [
        ("HTML/CSS", [
            {"name": "Структура HTML", "description": "Создай базовую страницу", "deadline": "2024-01-14", "points": 10, "done": False},
            {"name": "CSS стилизация", "description": "Добавь стили", "deadline": "2024-01-19", "points": 15, "done": False},
        ]),
    ])
    print(courses)
    print("\n=== Задачи на дедлайне ===")
    courses.show_overdue()
    print("\n=== Прогресс по курсам ===")
    courses.show_progress()
