# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: CourseBoard
def print_table(courses, columns=("name", "progress_pct", "deadline", "modules_count")):
    """Форматированный вывод таблицы курсов в консоль."""
    header = [str(col) for col in columns]
    separator = "+" + "+".join("-" * max(len(s), 5) for s in header) + "+"
    
    print(separator)
    print("| " + " | ".join(header) + " |")
    print(separator)
    
    for course in courses:
        name = str(course["name"])[:20]
        progress = f"{course['progress_pct']:.1f}%" if hasattr(course, 'progress_pct') and course.get('progress_pct', 0) else "-"
        deadline = str(course["deadline"])[:15] if hasattr(course, 'deadline') and course.get("deadline") else "-"
        modules_count = str(len(course["modules"])) if hasattr(course, "modules") and course.get("modules") else "-"
        
        row = f"| {name} | {progress:>6s} | {deadline:>15s} | {modules_count:>3s} |"
        print(row)
    
    print(separator)

if __name__ == "__main__":
    demo_courses = [
        {"name": "Python Basics", "progress_pct": 80.0, "deadline": "2024-12-15", "modules": ["Intro", "Variables", "Functions"]},
        {"name": "Data Structures", "progress_pct": 45.5, "deadline": "2024-12-20", "modules": ["Lists", "Dictionaries", "Tuples", "Sets"]},
        {"name": "Algorithms", "progress_pct": 0.0, "deadline": "2025-01-30", "modules": []},
    ]
    
    print_table(demo_courses)
