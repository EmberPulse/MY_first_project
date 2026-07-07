# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: CourseBoard
class Tag:
    def __init__(self, name):
        self.name = name.lower()

    def __eq__(self, other):
        if isinstance(other, Tag): return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)

class CourseBoard:
    _tags = set()

    @staticmethod
    def add_tag(tag_name):
        tag = Tag(tag_name)
        CourseBoard._tags.add(tag)
        print(f"Теги добавлены: {tag}")

    @staticmethod
    def remove_tag(tag_name):
        tag = Tag(tag_name)
        if tag in CourseBoard._tags:
            CourseBoard._tags.remove(tag)
            print(f"Тег удалён: {tag}")
            return True
        else:
            print(f"Тег не найден: {tag}")
            return False

    @staticmethod
    def get_tags():
        return list(CourseBoard._tags)
