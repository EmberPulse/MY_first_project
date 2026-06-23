# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: CourseBoard
def export_state():
    import json
    from datetime import datetime
    state = {
        "timestamp": datetime.utcnow().isoformat(),
        "courses": courses,
        "user_progress": user_progress,
        "notifications": notifications
    }
    return json.dumps(state, indent=2, ensure_ascii=False)
