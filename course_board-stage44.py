# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: CourseBoard
import json, datetime

def backup_data(data_path, backup_dir="backups"):
    """Резервное копирование файла данных."""
    try:
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        import os
        os.makedirs(backup_dir, exist_ok=True)
        backup_path = os.path.join(backup_dir, f"courseboard_backup_{ts}.json")
        with open(backup_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Backed up to {backup_path}")
        return backup_path
    except Exception as e:
        print(f"Backup failed: {e}")
        return None
