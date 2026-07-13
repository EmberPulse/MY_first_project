# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: CourseBoard
def show_reminders():
    """Списывает напоминания для курсов, у которых есть задания с датой дедлайна."""
    reminders = []
    for course in courses:
        for module in course.modules.values():
            for task in module.tasks.values():
                if hasattr(task, 'deadline') and task.deadline is not None:
                    days_left = (task.deadline - datetime.now()).days
                    status = "Сегодня" if days_left == 0 else \
                             f"Через {abs(days_left)} дней" if days_left > 0 else "ПРОСРОЧЕН"
                    reminders.append(f"[{course.name}] М: {module.name} — \"{task.title}\" ({status})")
    return "\n".join(reminders)

courses = []
