# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: CourseBoard
def delete_record(record_id, records_list):
    if record_id not in records_list:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    index = records_list.index(record_id)
    
    # Определяем тип записи по ключевым полям (упрощенная логика для примера)
    if 'modules' in record_id or isinstance(records_list[index], dict) and 'module_name' in records_list[index]:
        deleted = records_list.pop(index)
        print(f"Модуль '{deleted.get('module_name')}' успешно удалён.")
        return True
    
    elif 'assignments' in record_id or isinstance(records_list[index], dict) and 'assignment_title' in records_list[index]:
        deleted = records_list.pop(index)
        print(f"Задание '{deleted.get('assignment_title')}' успешно удалено.")
        return True
        
    else:
        # Если это просто ID курса или другого типа записи
        deleted = records_list.pop(index)
        print(f"Запись с ID {record_id} успешно удалена.")
        return True

# Пример вызова (раскомментируйте при тестировании):
# course_id = "course_101"
# module_id = "mod_python_basics"
# if delete_record(module_id, courses_data.get(course_id).get('modules', [])):
#     print("Удаление завершено.")
