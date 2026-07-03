# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: CourseBoard
def calculate_monthly_stats(courses, year=2024):
    from datetime import date, timedelta
    stats = {}
    for course in courses:
        if 'deadline' not in course or not isinstance(course['deadline'], date): continue
        d = course['deadline']
        month_key = f"{year}-{d.month}"
        if month_key not in stats: stats[month_key] = {'total': 0, 'completed': 0}
        stats[month_key]['total'] += 1
        if course.get('status') == 'completed': stats[month_key]['completed'] += 1
    return stats
