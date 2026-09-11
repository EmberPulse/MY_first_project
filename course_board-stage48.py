# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: CourseBoard
def _compact_refactor():
    """Консольный демонстратор CourseBoard: показывает курсы, модули, задания и прогресс."""
    courses = [
        {"name": "Python-базы", "modules": [
            {"name": "Введение", "tasks": [
                {"title": "Установка Python", "deadline": "2025-01-10", "done": True},
                {"title": "Первые скрипты", "deadline": "2025-01-15", "done": False},
            ]},
            {"name": "Типы данных", "tasks": [
                {"title": "Строки", "deadline": "2025-01-20", "done": True},
                {"title": "Списки", "deadline": "2025-01-25", "done": False},
            ]},
        ]},
        {"name": "Web-разработка", "modules": [
            {"name": "HTML", "tasks": [
                {"title": "Теги", "deadline": "2025-02-01", "done": False},
            ]},
        ]},
    ]

    print("=== CourseBoard ===")
    for c in courses:
        print(f"\nКурс: {c['name']}")
        for m in c["modules"]:
            print(f"  Модуль: {m['name']}")
            for t in m["tasks"]:
                status = "✅" if t["done"] else "❌"
                print(f"    {status} {t['title']} (дедлайн: {t['deadline']})")
        # прогресс модуля
        total = sum(len(m["tasks"]) for m in c["modules"])
        done = sum(1 for m in c["modules"] for t in m["tasks"] if t["done"])
        print(f"  Прогресс: {done}/{total} ({100 * done // total}%)")

_compact_refactor()
