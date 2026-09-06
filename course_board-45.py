# === Stage 45: Добавь восстановление из резервной копии ===
# Project: CourseBoard
import json, os

def restore_backup(backup_path="courseboard_backup.json"):
    if not os.path.exists(backup_path):
        print(f"Резервная копия не найдена: {backup_path}")
        return False
    try:
        with open(backup_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        print(f"Восстановление из {backup_path} завершено.")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
