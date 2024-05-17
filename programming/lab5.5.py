school = {
    "1а": 25,
    "1б": 28,
    "2б": 30,
    "6а": 22,
    "7в": 26
}
def change_class_size(class_name, new_size):
    if class_name in school:
        school[class_name] = new_size
        print(f"Количество учащихся в классе {class_name} изменено на {new_size}")
    else:
        print(f"Класс {class_name} не найден в базе данных")
def add_new_class(class_name, initial_size):
    if class_name not in school:
        school[class_name] = initial_size
        print(f"Добавлен новый класс {class_name} с количеством учащихся {initial_size}")
    else:
        print(f"Класс {class_name} уже существует в базе данных")
def dissolve_class(class_name):
    if class_name in school:
        total_students = school.pop(class_name)  # Удаляем класс из словаря и получаем количество учеников
        remaining_classes = len(school)
        if remaining_classes > 0:
            new_size = total_students // remaining_classes
            for cls in school:
                school[cls] += new_size
            print(f"Класс {class_name} расформирован, ученики равномерно распределены по остальным классам")
        else:
            print("Невозможно расформировать последний класс")
    else:
        print(f"Класс {class_name} не найден в базе данных")
def export_data():
    total_students = sum(school.values())
    total_classes = len(school)
    print(f"Общее количество учащихся в школе: {total_students}")
    print(f"Общее количество классов в школе: {total_classes}")
    print("Распределение учеников по классам:")
    for class_name, num_students in school.items():
        print(f"{class_name}: {num_students} учеников") 