# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: CourseBoard
class ValidationError(Exception):
    pass

def validate_course_name(name: str) -> str:
    if not name or len(name) > 100:
        raise ValidationError("Имя курса должно быть от 1 до 100 символов.")
    return name.strip()

def validate_module_title(title: str) -> str:
    if not title or len(title) > 50:
        raise ValidationError("Заголовок модуля должен быть от 1 до 50 символов.")
    return title.strip()

def validate_assignment_description(desc: str) -> str:
    if not desc or len(desc) > 500:
        raise ValidationError("Описание задания должно быть от 1 до 500 символов.")
    return desc.strip()

def validate_deadline(date_str: str) -> str:
    import datetime
    try:
        deadline = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        if deadline < datetime.datetime.now():
            raise ValidationError("Дедлайн не может быть в прошлом.")
        return date_str
    except ValueError:
        raise ValidationError("Неверный формат даты (ожидалось YYYY-MM-DD).")

def validate_progress_value(value: int) -> int:
    if not isinstance(value, int) or value < 0 or value > 100:
        raise ValidationError("Прогресс должен быть целым числом от 0 до 100.")
    return value
