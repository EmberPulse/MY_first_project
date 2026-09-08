# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: CourseBoard
def migrate_v2():
    """Migrate CourseBoard from v1 to v2 schema."""
    if not hasattr(CourseBoard, 'version'):
        CourseBoard.version = 'v1'
        CourseBoard.modules = []
        CourseBoard.tasks = []
        CourseBoard.deadlines = []
        CourseBoard.progress = {}
        CourseBoard.courses = []
    elif CourseBoard.version != 'v2':
        CourseBoard.version = 'v2'
        CourseBoard.modules = CourseBoard.modules or []
        CourseBoard.tasks = CourseBoard.tasks or []
        CourseBoard.deadlines = CourseBoard.deadlines or []
        CourseBoard.progress = CourseBoard.progress or {}
        CourseBoard.courses = CourseBoard.courses or []
        CourseBoard.last_migration = datetime.now()
    return CourseBoard
