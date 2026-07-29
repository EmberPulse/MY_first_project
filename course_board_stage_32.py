# === Stage 32: Добавь журнал действий пользователя ===
# Project: CourseBoard
class ActionLog:
    def __init__(self):
        self.entries = []

    def log(self, user, action_type, detail=""):
        entry = {
            "user": user,
            "type": action_type,
            "detail": detail,
            "timestamp": time.time(),
        }
        self.entries.append(entry)

    def get_recent(self, count=5):
        return list(reversed(self.entries[-count:])) if len(self.entries) >= count else list(reversed(self.entries))

    def summary(self):
        if not self.entries:
            return "Журнал пуст."
        counts = {}
        for e in self.entries:
            t = e["type"]
            counts[t] = counts.get(t, 0) + 1
        lines = ["=== Журнал действий ===", f"Всего записей: {len(self.entries)}"]
        for t, c in sorted(counts.items(), key=lambda x: -x[1]):
            lines.append(f"  {t}: {c}")
        return "\n".join(lines)


log = ActionLog()


def add_action(user, action_type, detail=""):
    log.log(user, action_type, detail)
    recent = log.get_recent(3)
    print("\n--- Последние действия ---")
    for r in recent:
        print(f"  [{r['type']}] {r['user']} — {r['detail']}")


add_action("student1", "STARTED", "Начал курс Python")
add_action("student2", "VIEWED_MODULE", "Модуль 3 — Задачи")
