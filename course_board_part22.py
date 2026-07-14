# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: CourseBoard
def check_overdue_reminders(reminders):
    overdue = []
    now = datetime.now()
    for r in reminders:
        if r['deadline'] < now and not r.get('completed'):
            overdue.append(r)
    return overdue
