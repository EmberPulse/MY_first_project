# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: CourseBoard
def main():
    courses = {"Python": {"modules": [{"name": "Основы", "tasks": 3, "done": 1}, {"name": "Продвинутые темы", "tasks": 5, "done": 2}]}}
    while True:
        print("\n=== CourseBoard ===")
        for name in courses:
            print(f"[{len(courses[name]['modules'])} модулей] {name}")
        cmd = input("Команда (c - курс, m - модуль, t - задача, h - выход): ").strip().lower()
        if not cmd or cmd == "h": break
        parts = cmd.split(maxsplit=1)
        action, target = parts[0], parts[1] if len(parts) > 1 else None
        try:
            course_name = next(c for c in courses if c.startswith(target)) if target else list(courses)[0]
            module_idx = int(action.split()[1]) - 1 if action == "m" else 0
            task_idx = int(action.split()[2]) - 1 if len(action.split()) > 2 else 0
        except (ValueError, StopIteration):
            print("Некорректный ввод.")
            continue
        if action == "c":
            course_name = target or list(courses)[0]
            mod_idx = int(input(f"Выберите модуль курса '{course_name}' (1-{len(courses[course_name]['modules'])}): ")) - 1
            print(f"\n--- Модуль: {courses[course_name]['modules'][mod_idx]['name']} ---")
        elif action == "m":
            course_name = target or list(courses)[0]
            mod_idx = int(action.split()[1]) - 1 if len(action.split()) > 1 else 0
            print(f"\n--- Модуль: {courses[course_name]['modules'][mod_idx]['name']} ---")
        elif action == "t":
            course_name = target or list(courses)[0]
            mod_idx = int(action.split()[1]) - 1 if len(action.split()) > 1 else 0
            task_idx = int(action.split()[2]) - 1 if len(action.split()) > 2 else 0
            courses[course_name]['modules'][mod_idx]['done'] += 1
            print("Задача выполнена!")

if __name__ == "__main__":
    main()
