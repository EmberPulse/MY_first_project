# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: CourseBoard
def edit_record(record_id, updates):
    if not isinstance(updates, dict) or len(updates) == 0:
        raise ValueError("Updates must be a non-empty dictionary")
    
    for key in ["title", "description", "deadline", "modules"]:
        if key in updates and (updates[key] is None or updates[key].strip() == ""):
            raise ValueError(f"Field '{key}' cannot be empty")

    course_index = next((i for i, c in enumerate(courses) if c["id"] == record_id), -1)
    if course_index == -1:
        raise KeyError(f"No course found with id {record_id}")

    course = courses[course_index]
    
    if "title" in updates:
        course["title"] = updates["title"].strip()
    if "description" in updates:
        course["description"] = updates["description"].strip()
    if "deadline" in updates and updates["deadline"]:
        try:
            from datetime import datetime
            date_str = updates["deadline"].split()[0]
            deadline_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            course["deadline"] = deadline_date.isoformat() if deadline_date else None
        except ValueError:
            raise ValueError("Invalid date format for 'deadline'. Use YYYY-MM-DD")

    if "modules" in updates and isinstance(updates["modules"], list):
        new_modules = []
        for mod in updates["modules"]:
            if not isinstance(mod, dict) or len(mod) == 0:
                raise ValueError("Each module must be a non-empty dictionary")
            
            if "title" in mod and (mod["title"] is None or str(mod["title"]).strip() == ""):
                raise ValueError("Module title cannot be empty")
            
            new_mod = {k: v for k, v in mod.items()}
            if "description" in new_mod and (new_mod["description"] is None or str(new_mod["description"]).strip() == ""):
                del new_mod["description"]
            else:
                new_mod["description"] = new_mod.get("description", "").strip()
            
            if "deadline" in new_mod and (new_mod["deadline"] is None or str(new_mod["deadline"]).strip() == ""):
                try:
                    from datetime import datetime
                    date_str = new_mod["deadline"].split()[0]
                    deadline_date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    new_mod["deadline"] = deadline_date.isoformat() if deadline_date else None
                except ValueError:
                    raise ValueError("Invalid date format for module 'deadline'. Use YYYY-MM-DD")
            
            new_modules.append(new_mod)

        course["modules"] = new_modules

    return course
