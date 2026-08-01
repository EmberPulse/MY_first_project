# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: CourseBoard
TEMPLATES = {
    "assignment": {
        "type": "Assignment",
        "title": "",
        "description": "",
        "deadline": None,
        "points": 10,
        "status": "pending"
    },
    "module": {
        "type": "Module",
        "name": "",
        "topics": [],
        "duration_hours": 2
    }
}

def create_from_template(template_name):
    if template_name not in TEMPLATES:
        raise ValueError(f"Unknown template: {template_name}")
    record = dict(TEMPLATES[template_name])
    return record
