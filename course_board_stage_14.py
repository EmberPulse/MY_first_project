# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: CourseBoard
def generate_summary(courses):
    """Генерирует текстовую сводку по всем курсам."""
    lines = ["=== СВОДКА ПО КУРСАМ ==="]
    
    for course in courses:
        name = course.get("name", "Неизвестный курс")
        modules_count = len(course.get("modules", []))
        tasks_total = sum(len(m.get("tasks", [])) for m in course.get("modules", []))
        
        progress_percent = 0.0
        if tasks_total > 0:
            completed_tasks = sum(1 for m in course["modules"] 
                                 for t in m["tasks"] if t.get("status") == "completed")
            progress_percent = (completed_tasks / tasks_total) * 100
        
        deadline_str = course.get("deadline", "Нет дедлайна")
        
        lines.append(f"\nКурс: {name}")
        lines.append(f"Модулей: {modules_count}, Задач всего: {tasks_total}")
        lines.append(f"Прогресс выполнения: {progress_percent:.1f}%")
        lines.append(f"Дедлайн: {deadline_str}")

    if not courses:
        lines.append("\nНет доступных курсов.")
    
    return "\n".join(lines)
