# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: CourseBoard
def print_metrics(courses, assignments):
    """Показывает ключевые метрики проекта CourseBoard."""
    total = sum(len(c['modules']) for c in courses)
    done = sum(
        sum(a.get('done', 0) for a in m.get('assignments', []))
        for c in courses
        for m in c['modules']
    )
    deadline_misses = sum(
        1 for c in courses
        for m in c['modules']
        for a in m.get('assignments', [])
        if not a.get('done') and a.get('deadline') < now()
    )
    print(f"Курсы: {len(courses)}, Модулей: {total}, Готово: {done}")
    pct = (done / total * 100) if total else 0
    print(f"Процент выполнения: {pct:.1f}%")
    print(f"Мисс дедлайнов: {deadline_misses}")
