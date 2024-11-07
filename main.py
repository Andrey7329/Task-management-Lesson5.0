class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        self.tasks.append(Task(description, due_date))

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Ошибка: Индекс задачи вне диапазона.")

    def show_current_tasks(self):
        current_tasks = [task for task in self.tasks if not task.completed]
        if not current_tasks:
            print("Нет текущих задач.")
        else:
            for index, task in enumerate(current_tasks):
                print(f"{index}. {task}")


def main():
    task_manager = TaskManager()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать текущие задачи")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения задачи (YYYY-MM-DD): ")
            task_manager.add_task(description, due_date)
            print("Задача добавлена.")

        elif choice == '2':
            task_manager.show_current_tasks()
            task_index = int(input("Введите номер задачи, которую хотите отметить как выполненную: "))
            task_manager.mark_task_as_completed(task_index)
            print("Задача отмечена как выполненная.")

        elif choice == '3':
            print("Текущие задачи:")
            task_manager.show_current_tasks()

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из меню.")


if __name__ == "__main__":
    main()