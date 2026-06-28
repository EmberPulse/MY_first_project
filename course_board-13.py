# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: CourseBoard
class SearchEngine:
    def __init__(self, data):
        self.data = data
    
    def search(self, query):
        if not query.strip():
            return []
        
        query_lower = query.lower()
        results = []
        
        for course in self.data:
            fields_to_check = [
                'name', 'description', 
                'module_name', 'task_description',
                'deadline_date'
            ]
            
            if any(query_lower in str(field).lower() for field in fields_to_check):
                results.append(course)
        
        return results
