# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: CourseBoard
def undo_last_action():
    """Откат последовательного изменения: курсор → модуль → задание → дедлайн → прогресс."""
    history = []
    
    def log(key, value):
        history.append((key, value))
    
    def revert():
        if not history:
            return
        key, _ = history.pop()
        return key  # возвращает ключ для восстановления
    
    # Пример использования в CourseBoard
    course_data = {
        "name": "Python Basics",
        "modules": [
            {"title": "Модуль 1", "tasks": [{"title": "Задание 1", "deadline": "2024-12-31", "progress": 50}]},
            {"title": "Модуль 2", "tasks": [{"title": "Задание 2", "deadline": "2024-12-31", "progress": 75}]}
        ]
    }
    
    # Модифицируем данные и сохраняем в историю
    course_data["modules"][0]["tasks"][0]["progress"] = 90
    log("task_progress", (course_data["modules"][0]["tasks"][0], "progress"))
    
    print(f"Текущий прогресс: {course_data['modules'][0]['tasks'][0]['progress']}%")
    
    # Откат изменений
    key = revert()
    if key == "task_progress":
        course_data["modules"][0]["tasks"][0]["progress"] = 50
    
    print(f"После отката: {course_data['modules'][0]['tasks'][0]['progress']}%")
