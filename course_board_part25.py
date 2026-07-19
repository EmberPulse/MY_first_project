# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: CourseBoard
def parse_date(date_str):
    """Парсит дату в формате 'YYYY-MM-DD'. Возвращает datetime или строку ошибки."""
    if not date_str or len(date_str.split('-')) != 3:
        return "Ошибка: некорректный формат даты. Используйте YYYY-MM-DD."
    try:
        from datetime import datetime, date as dt_date
        parts = date_str.split('-')
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        d = dt_date(year, month, day)
        return d
    except ValueError as e:
        return f"Ошибка: невозможная дата — {e}"

class CourseBoard:
    def __init__(self):
        self.courses = []

    def add_course(self, name, description="", modules=None):
        if not name or not isinstance(name, str) or len(name.strip()) == 0:
            return "Ошибка: имя курса обязательно и не может быть пустым."
        course = {"name": name, "description": description or "", "modules": []}
        if modules is None:
            modules = []
        for m in modules:
            task_name = m.get("task") or m.get("title")
            deadline_str = m.get("deadline") or ""
            progress = m.get("progress", 0)
            if not isinstance(task_name, str):
                return "Ошибка: задание должно иметь текстовое название."
            if task_name.strip() == "":
                return "Ошибка: название задания не может быть пустым."
            deadline = parse_date(deadline_str)
            if isinstance(deadline, str):
                m["deadline"] = deadline
            else:
                m["deadline"] = deadline
                m["is_overdue"] = datetime.now() > deadline if hasattr(self, "__class__") else None
            m["progress"] = int(progress)
            course["modules"].append(m)
        self.courses.append(course)
        return f"Курс '{name}' добавлен с {len(modules)} модулями."

    def get_progress_report(self):
        if not self.courses:
            return "Нет курсов для отчёта."
        report = []
        for course in self.courses:
            total_modules = len(course["modules"])
            completed = sum(1 for m in course["modules"] if m.get("progress", 0) >= 100)
            overdue = sum(1 for m in course["modules"] if isinstance(m.get("deadline"), dt_date) and m.get("is_overdue"))
            report.append(f"Курс: {course['name']}, завершено: {completed}/{total_modules}")
        return "\n".join(report)

    def get_deadline_alerts(self):
        alerts = []
        now = datetime.now()
        for course in self.courses:
            for m in course["modules"]:
                deadline = m.get("deadline")
                if isinstance(deadline, dt_date):
                    if deadline <= now and (m.get("progress", 0) < 100 or not m.get("is_overdue")):
                        alerts.append(f"⚠️ {course['name']} — задание '{m.get('task')}' просрочено!")
        return alerts

    def clear_alerts(self):
        if self._alert_count == 0:
            return "Нет активных предупреждений."
        self._alert_count = 0
        return f"Удалено {self._old_alert_count} предупреждений."
