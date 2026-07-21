# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: CourseBoard
def demo():
    print("=== CourseBoard Demo ===")
    for i in range(1, 4):
        course = Course(f"Python {i}", "Курс по Python", 5)
        m1 = Module("Введение", "Базовые концепции", 3)
        m2 = Module("Функции", "Ф-ии и лямбды", 4)
        course.add_module(m1)
        course.add_module(m2)
        for j in range(1, m1.tasks_count + 1):
            task = Task(f"Задание {j}", f"Описать {i}-е понятие", datetime.now().replace(day=datetime.now().day - 3))
            course.add_task(task)
        for j in range(1, m2.tasks_count + 1):
            task = Task(f"Задание {j} части 2", f"Реализовать пример", datetime.now().replace(day=datetime.now().day - 5))
            course.add_task(task)
        print(course.to_json())

demo()
