# === Stage 20: Добавь восстановление записей из архива ===
# Project: CourseBoard
def archive_restore(self):
        """Восстанавливает записи из архива курсов."""
        if not self._archives:
            print("Архив пуст")
            return
        arch = input("Введите идентификатор архива для восстановления (или 'all' для всех):\n> ")
        restored = []
        if arch == "all":
            for aid, records in list(self._archives.items()):
                print(f"\nАрхив {aid}: {len(records)} записей")
                for rec in records:
                    print(rec)
                self._courselist.extend(records)
                restored.extend(records)
        else:
            if arch not in self._archives:
                print("Архив не найден")
                return
            recs = list(self._archives[arch])
            for r in recs:
                print(r)
            self._courselist.extend(recs)
            restored = recs
        if restored:
            print(f"\n{len(restored)} записей восстановлено в список курсов")
