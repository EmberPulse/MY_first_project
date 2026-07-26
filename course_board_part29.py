# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: CourseBoard
APP_CONFIG = {
    "app_name": "CourseBoard",
    "version": "29.0",
    "max_assignments_per_module": 10,
    "progress_threshold_percent": 75,
    "deadline_grace_days": 3,
    "notification_enabled": True,
    "dark_mode_default": False,
}

def get_config():
    return APP_CONFIG.copy()

def update_config(key, value):
    if key in APP_CONFIG:
        APP_CONFIG[key] = value
    else:
        raise KeyError(f"Unknown config key: {key}")

def reset_config():
    global APP_CONFIG
    APP_CONFIG.update({
        "app_name": "CourseBoard",
        "version": "29.0",
        "max_assignments_per_module": 10,
        "progress_threshold_percent": 75,
        "deadline_grace_days": 3,
        "notification_enabled": True,
        "dark_mode_default": False,
    })
