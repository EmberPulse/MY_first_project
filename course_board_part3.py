# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: CourseBoard
class CourseBoard:
    def __init__(self):
        self.courses = {}
    
    def add_course(self, name, modules=None):
        if not modules:
            modules = []
        self.courses[name] = {'modules': modules}
        return self.courses[name]

    def add_module(self, course_name, title, tasks=None):
        if course_name not in self.courses:
            raise ValueError(f"Course {course_name} not found")
        module_id = len(self.courses[course_name]['modules']) + 1
        self.courses[course_name]['modules'].append({
            'id': module_id,
            'title': title,
            'tasks': tasks or []
        })

    def add_task(self, course_name, module_title, description, deadline=None):
        for mod in self.courses[course_name]['modules']:
            if mod['title'] == module_title:
                task = {
                    'description': description,
                    'deadline': deadline,
                    'completed': False
                }
                mod['tasks'].append(task)
                return task
        raise ValueError(f"Module {module_title} not found in course {course_name}")

    def mark_task_complete(self, course_name, module_title, task_description):
        for mod in self.courses[course_name]['modules']:
            if mod['title'] == module_title:
                for i, task in enumerate(mod['tasks']):
                    if task['description'] == task_description:
                        task['completed'] = True
                        return task
        raise ValueError(f"Task {task_description} not found")

    def get_progress(self, course_name):
        total_tasks = 0
        completed_tasks = 0
        for mod in self.courses[course_name]['modules']:
            for task in mod['tasks']:
                total_tasks += 1
                if task.get('completed', False):
                    completed_tasks += 1
        return (total_tasks, completed_tasks)
