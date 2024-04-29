def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:        
        with open('task_1\salary_file.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # Розділяємо рядок на прізвище та заробітну плату
                name, salary = line.strip().split(',')
                # Додаємо зарплату до загальної суми
                total_salary += int(salary)
                # Збільшуємо лічильник розробників
                num_developers += 1

        # Розраховуємо середню заробітну плату
        average_salary = total_salary / num_developers
        return total_salary, average_salary

    except FileNotFoundError:
        print("Файл не знайдено")
        return None, None
    except Exception as e:
        print(f"Помилка: {e}")
        return None, None

# Приклад використання
total, average = total_salary("task_1\salary_file.txt")
if total is not None and average is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
