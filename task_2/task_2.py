def get_cats_info(path):
    cats_info = [] # Ініціалізуємо пустий список для зберігання інформації про котів
    try:
        with open('task_2\cats_file.txt', 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                cat_dict = { # Створюємо словник для інформації про кота
                    "id": cat_data[0], "name": cat_data[1], "age": cat_data[2]
                }
                cats_info.append(cat_dict) # Додаємо словник про кота до списку
    # Обробляємо можливі винятки
    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return cats_info # Повертаємо список словників інформації про котів

# Приклад використання функції
cats_info = get_cats_info('task_2\cats_file.txt')
for cat in cats_info:
    print(f"{{\n    \"id\": \"{cat['id']}\", \"name\": \"{cat['name']}\", \"age\": \"{cat['age']}\"\n}}")
