# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: CourseBoard
def print_course_record(course):
    if not course:
        return
    name = course.get("name", "Unknown")
    modules = course.get("modules", [])
    total_modules = sum(m.get("tasks", []) for m in modules)
    completed_tasks = sum(1 for t in total_modules)
    
    print(f"Курс: {name}")
    print(f"Модулей: {len(modules)}, Задач: {completed_tasks}/{total_modules}")
    if course.get("deadline"):
        print(f"Дедлайн: {course['deadline']}")
