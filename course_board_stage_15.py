# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: CourseBoard
def calculate_weekly_stats(courses, start_date=None):
    if not courses: return {}
    from datetime import date, timedelta
    today = date.today()
    if start_date is None: start_date = today - timedelta(days=today.weekday()) # начало текущей недели (понедельник)
    week_start = start_date
    while True:
        stats = {date.strftime('%Y-%w'): {'total_deadlines': 0, 'completed_tasks': 0}}
        current_week_end = week_start + timedelta(days=6)
        for course in courses.values():
            for module in course.get('modules', []):
                for task in module.get('tasks', []):
                    deadline = date.fromisoformat(task['deadline'])
                    if week_start <= deadline < current_week_end:
                        stats[deadline.strftime('%Y-%w')]['total_deadlines'] += 1
        # Прогресс по задачам в этой неделе (условно считаем выполненные те, что дедлайн уже прошел)
        for course in courses.values():
            completed = sum(1 for m in course.get('modules', []) for t in m.get('tasks', []) if t['completed'])
            stats[week_start.strftime('%Y-%w')]['completed_tasks'] += completed
        yield week_start, dict(stats)
        week_start += timedelta(days=7)
