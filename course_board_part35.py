# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: CourseBoard
def get_next_action(user, course):
    """Recommend the next action based on current state."""
    if not course.get('modules'):
        return {'action': 'start', 'text': f'Create your first module for {course["title"]}.'}

    pending = [m for m in course['modules'] if not m.get('completed')]
    if pending:
        next_mod = min(pending, key=lambda m: m.get('order', 0))
        if not next_mod.get('tasks'):
            return {'action': 'add_tasks', 'text': f'Add tasks to module "{next_mod["title"]}".'}

        incomplete_tasks = [t for t in next_mod['tasks'] if not t.get('completed')]
        if incomplete_tasks:
            due_task = min(incomplete_tasks, key=lambda t: (not t.get('deadline'), t.get('order', 0)))
            return {'action': 'do_task', 'text': f'Work on task "{due_task["title"]}" in module "{next_mod["title"]}": {due_task["description"]}'.strip()}

    if course.get('progress') < 1.0:
        return {'action': 'continue', 'text': "You're making progress! Keep going."}

    return {'action': 'review', 'text': f'Course "{course["title"]}": all modules completed. Consider reviewing or starting a new course.'}
