# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: CourseBoard
import unittest

class TestEdgeCases(unittest.TestCase):
    def test_zero_duration(self):
        course = Course()
        course.add_module(Module("Test", 0, 1, 2))
        self.assertEqual(course.duration, 0)

    def test_negative_duration(self):
        course = Course()
        course.add_module(Module("Test", -1, 1, 2))
        with self.assertRaises(ValueError):
            _ = course.duration

    def test_empty_assignments(self):
        course = Course()
        course.add_module(Module("Empty", 1, 0, 1))
        self.assertEqual(course.progress, 0)

    def test_due_date_before_start(self):
        course = Course()
        course.add_module(Module("Early", 1, 1, 0))
        with self.assertRaises(ValueError):
            course.add_assignment(1, 1, 0, "Task")

    def test_due_date_after_end(self):
        course = Course()
        course.add_module(Module("Late", 1, 1, 2))
        with self.assertRaises(ValueError):
            course.add_assignment(1, 1, 2, "Task")

    def test_due_date_in_range(self):
        course = Course()
        course.add_module(Module("OnTime", 1, 1, 2))
        course.add_assignment(1, 1, 1, "Task")
        self.assertEqual(course.progress, 1)

    def test_multiple_modules(self):
        course = Course()
        course.add_module(Module("M1", 1, 1, 2))
        course.add_module(Module("M2", 1, 2, 3))
        course.add_assignment(1, 1, 1, "Task1")
        course.add_assignment(1, 2, 2, "Task2")
        self.assertEqual(course.progress, 2)

    def test_duplicate_module_names(self):
        course = Course()
        course.add_module(Module("Dup", 1, 1, 2))
        with self.assertRaises(ValueError):
            course.add_module(Module("Dup", 1, 2, 3))

    def test_empty_course_progress(self):
        course = Course()
        self.assertEqual(course.progress, 0)

    def test_progress_with_no_assignments(self):
        course = Course()
        course.add_module(Module("NoAssign", 1, 1, 2))
        self.assertEqual(course.progress, 0)

    def test_progress_with_all_assignments(self):
        course = Course()
        course.add_module(Module("All", 1, 1, 2))
        course.add_assignment(1, 1, 1, "Task1")
        course.add_assignment(1, 1, 2, "Task2")
        self.assertEqual(course.progress, 2)

if __name__ == '__main__':
    unittest.main()
