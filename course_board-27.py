# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: CourseBoard
def reset_demo_data():
    """Сбросить все демо-данные в дефолтные значения."""
    courses = [
        {
            "id": 1,
            "name": "Python для начинающих",
            "modules": [
                {"id": 1, "title": "Введение", "lessons": ["Что такое Python", "Установка окружения"]},
                {"id": 2, "title": "Переменные и типы данных", "lessons": ["int", "str", "float", "bool"]}
            ],
            "assignments": [
                {"id": 1, "title": "Первый скрипт", "deadline": "2024-11-30", "completed": False},
                {"id": 2, "title": "Работа с типами данных", "deadline": "2024-12-15", "completed": False}
            ],
            "progress": 0.0,
            "active": True
        },
        {
            "id": 2,
            "name": "Web-разработка",
            "modules": [
                {"id": 1, "title": "HTML основы", "lessons": ["Теги", "Форматирование"]},
                {"id": 2, "title": "CSS стилизация", "lessons": ["Цвета", "Шрифты", "Отступы"]}
            ],
            "assignments": [
                {"id": 1, "title": "Тест HTML", "deadline": "2024-12-01", "completed": False},
                {"id": 2, "title": "Стилизация страницы", "deadline": "2024-12-10", "completed": False}
            ],
            "progress": 0.0,
            "active": True
        },
        {
            "id": 3,
            "name": "Математический анализ",
            "modules": [
                {"id": 1, "title": "Пределы", "lessons": ["Определение предела", "Теорема о夹逼"]},
                {"id": 2, "title": "Производная", "lessons": ["Определение производной", "Правила дифференцирования"]}
            ],
            "assignments": [
                {"id": 1, "title": "Задачи на пределы", "deadline": "2024-12-20", "completed": False},
                {"id": 2, "title": "Дифференцирование функций", "deadline": "2025-01-05", "completed": False}
            ],
            "progress": 0.0,
            "active": True
        }
    ]

    settings = {
        "theme": "light",
        "language": "en",
        "notifications_enabled": True,
        "show_deadlines": True
    }

    global courses, settings
    courses.clear()
    settings.clear()
    _courses.extend(courses)
    _settings.update(settings)
