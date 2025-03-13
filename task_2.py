# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def add_assigned_subjects(self, subjects):
        self.assigned_subjects.update(subjects)
         

def create_schedule(subjects, teachers):
    remaining_teachers = teachers.copy()
    uncovered_subjects = subjects.copy()
    schedule = []


    while remaining_teachers and uncovered_subjects:
        best_teacher = max(remaining_teachers, key=lambda t: (len(t.can_teach_subjects & uncovered_subjects), -t.age), default=None)
        
        if best_teacher is None or not best_teacher.can_teach_subjects & uncovered_subjects:
            break
        
        assigned_subjects = best_teacher.can_teach_subjects & uncovered_subjects
        best_teacher.add_assigned_subjects(assigned_subjects)

        schedule.append(best_teacher)

        uncovered_subjects -= assigned_subjects
        remaining_teachers.remove(best_teacher)
    
    
    return schedule if not uncovered_subjects else False


if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
    Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
    Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
    Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
    Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
    Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
    Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"})
]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
