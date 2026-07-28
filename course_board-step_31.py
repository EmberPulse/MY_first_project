# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: CourseBoard
def switch_profile():
    """Переключение активного профиля пользователя."""
    profiles = {
        "student": {"name": "Студент", "role": "учащийся"},
        "teacher": {"name": "Преподаватель", "role": "преподаватель"},
        "admin": {"name": "Администратор", "role": "администратор"},
    }
    active = get_setting("active_profile", default="student")
    print(f"Текущий профиль: {profiles[active]['name']} ({active})")
    new_profile = input("Введите новый профиль (student/teacher/admin) или Enter для останова: ").strip()
    if not new_profile or new_profile.lower() in ("", "cancel"):
        return
    if new_profile not in profiles:
        print(f"Профиль '{new_profile}' не найден.")
        return
    set_setting("active_profile", new_profile)
    print(f"Переключено на профиль: {profiles[new_profile]['name']}")


switch_profile()
