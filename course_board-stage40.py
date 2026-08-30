# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: CourseBoard
def main():
    import argparse
    parser = argparse.ArgumentParser(description="CourseBoard CLI")
    sub = parser.add_subparsers(dest="command")
    courses = sub.add_parser("courses", help="list courses")
    courses.add_argument("--json", action="store_true", help="output as JSON")
    sub.add_parser("modules", help="list modules")
    sub.add_parser("tasks", help="list tasks")
    sub.add_parser("progress", help="show progress")
    args = parser.parse_args()
    if args.command == "courses":
        for c in courses_data:
            print(f"{c['id']}  {c['name']}  {c['status']}")
    elif args.command == "modules":
        for c in courses_data:
            print(f"{c['id']}  {c['name']}  {c['modules']}")
    elif args.command == "tasks":
        for t in tasks_data:
            print(f"{t['id']}  {t['name']}  {t['status']}  {t['deadline']}")
    elif args.command == "progress":
        total = sum(len(c['modules']) for c in courses_data)
        done = sum(
            sum(1 for m in c['modules'] for t in m['tasks'] if t['status'] == "done")
            for c in courses_data
        )
        print(f"progress: {done}/{total}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
