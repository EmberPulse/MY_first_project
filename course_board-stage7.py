# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: CourseBoard
def sort_assignments(assignments, key='date'):
    if not assignments:
        return []
    
    def get_sort_value(item):
        date = item.get('due_date', '')
        priority = item.get('priority', 3)
        name = item.get('title', '').lower()
        
        try:
            dt = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            dt = datetime.min
        
        return (dt.year, dt.month, dt.day, -priority, name)
    
    if key == 'date':
        return sorted(assignments, key=get_sort_value)
    elif key == 'priority':
        return sorted(assignments, key=lambda x: (-x.get('priority', 3), x.get('title', '')))
    else: # by title
        return sorted(assignments, key=lambda x: (x.get('due_date', ''), -x.get('priority', 3), x.get('title', '').lower()))
