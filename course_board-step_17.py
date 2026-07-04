# === Stage 17: Добавь группировку записей по категориям ===
# Project: CourseBoard
from collections import defaultdict

def group_by_category(records, key_func):
    groups = defaultdict(list)
    for record in records:
        category = key_func(record)
        groups[category].append(record)
    return dict(sorted(groups.items()))

# Пример использования для CourseBoard (предполагается наличие списка курсов/заданий)
# courses_data = [...] # ваш список данных
# grouped_courses = group_by_category(courses_data, lambda c: c.get('category', 'Uncategorized'))
