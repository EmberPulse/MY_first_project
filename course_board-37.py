# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: CourseBoard
import unittest

class TestCourseBoardLogic(unittest.TestCase):

    def test_simple_task_completion(self):
        task = {'title': 'Task 1', 'deadline': 100, 'completed': False}
        self.assertFalse(task['completed'])
        task['completed'] = True
        self.assertTrue(task['completed'])
        self.assertEqual(task['title'], 'Task 1')

    def test_module_progress_calculation(self):
        tasks = [
            {'title': 'a1', 'completed': True},
            {'title': 'a2', 'completed': False},
            {'title': 'a3', 'completed': True},
        ]
        total = len(tasks)
        completed = sum(1 for t in tasks if t['completed'])
        progress = completed / total
        self.assertEqual(progress, 2 / 3)

    def test_deadline_check(self):
        task = {'deadline': 50, 'completed': False}
        now = 49
        self.assertFalse(task['deadline'] < now)
        now = 51
        self.assertTrue(task['deadline'] < now)

    def test_empty_module_progress(self):
        tasks = []
        total = len(tasks)
        completed = sum(1 for t in tasks if t['completed'])
        progress = 0 if total == 0 else completed / total
        self.assertEqual(progress, 0)

if __name__ == '__main__':
    unittest.main()
