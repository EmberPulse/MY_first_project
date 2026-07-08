# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: CourseBoard
def archive_records(archive_file, records_to_archive=None):
    """Archive completed or old course-board records to a separate file."""
    if records_to_archive is None:
        records_to_archive = []
    archived = []
    for rec in records_to_archive:
        if isinstance(rec, dict) and rec.get("completed", False) and rec.get("created_at"):
            age_days = (now() - datetime.fromisoformat(rec["created_at"])).days
            if age_days > 30 or rec.get("status") == "done":
                archived.append(rec)
    for r in archived:
        with open(archive_file, "a", encoding="utf-8") as f:
            json.dump(r, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(f"{len(archived)} records archived to {archive_file}")
