# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: CourseBoard
def validate_and_fix(courses):
    """Проверяет целостность данных курсов и автоматически исправляет простые проблемы."""
    fixes_applied = 0
    
    for course in courses:
        if not isinstance(course, dict) or 'title' not in course or 'modules' not in course:
            print(f"⚠️ Курс '{course}' не валиден — удалён")
            continue
        
        # Проверка: все модули имеют задачи с дедлайнами
        for i, module in enumerate(course['modules']):
            if not isinstance(module, dict) or 'name' not in module or 'tasks' not in module:
                print(f"⚠️ Модуль в курсе '{course['title']}' не валиден — пропущен")
                continue
            
            for j, task in enumerate(module['tasks']):
                if not isinstance(task, dict) or 'description' not in task or 'deadline' not in task:
                    print(f"⚠️ Задача в модуле '{module['name']}' курса '{course['title']}' не валидна — пропущена")
                    continue
                
                # Автоматическое присвоение дедлайна, если он отсутствует (используем текущую дату + 7 дней)
                if task.get('deadline') is None:
                    import datetime
                    new_deadline = datetime.date.today() + datetime.timedelta(days=7).isoformat()
                    task['deadline'] = new_deadline
                    fixes_applied += 1
                
                # Проверка: все задачи в модуле должны быть уникальными по описанию
                descriptions = [t['description'] for t in module['tasks']]
                if len(descriptions) != len(set(descriptions)):
                    print(f"⚠️ Дублирующиеся описания задач в модуле '{module['name']}' курса '{course['title']}' — удалены дубли")
                    seen = set()
                    unique_tasks = []
                    for t in module['tasks']:
                        if t['description'] not in seen:
                            seen.add(t['description'])
                            unique_tasks.append(t)
                    course['modules'][i]['tasks'] = unique_tasks
                    fixes_applied += 1
    
    print(f"✅ Проверка завершена. Применилось {fixes_applied} исправлений.")
