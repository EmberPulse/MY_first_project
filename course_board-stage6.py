# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: CourseBoard
def filter_records(records, filters=None):
    if not filters: return records
    for key, value in filters.items():
        if isinstance(value, list):
            records = [r for r in records if any(r.get(key) == v for v in value)]
        else:
            records = [r for r in records if r.get(key) == value]
    return records

def get_filtered_courses(courses, status=None, category=None, tags=None):
    filters = {}
    if status is not None: filters['status'] = status
    if category is not None: filters['category'] = category
    if tags is not None and len(tags) > 0: filters['tags'] = set(tags)
    return filter_records(courses, filters)
