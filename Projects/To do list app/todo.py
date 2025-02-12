class Task:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open('Todo.txt', 'r') as file:
                for line in file:
                    name, status = line.strip().split(" - ")
                    self.tasks.append(Task(name, status))
        except FileNotFoundError:
            print('No existing tasks found.')

    def save_tasks(self):
        with open('Todo.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name} - {task.status}\n")

    def addTasks(self):
        taskName = input('Enter the Task: ')
        taskStatus = input('Completed or Pending? : ').capitalize()
        new_task = Task(taskName, taskStatus)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{taskName}' added!")

    def show_tasks(self):
        print("\n---- Your Tasks -----")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
        print('==================')

    def update_task(self):
        self.show_tasks()
        try:
            task_id = int(input("Enter the task number to update: ")) - 1
            if 0 <= task_id < len(self.tasks):
                print(f"Updating Task: {self.tasks[task_id]}")
                new_name = input("Enter the new Task Name (or press enter to keep current name): ")
                new_status = input("Enter the new status of the Task (Completed/Pending) (or press enter to keep the current status): ").capitalize()

                if new_name:
                    self.tasks[task_id].name = new_name
                if new_status:
                    self.tasks[task_id].status = new_status

                self.save_tasks()
                print("Task Updated successfully!")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Please enter a valid number.")


# Main Program Loop
def main():
    manager = TaskManager()

    while True:
        print("\nWelcome, What would you like to do?")
        print("\nA - Add a task\nS - Show all tasks\nU - Update a task\nQ - Quit")
        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            manager.addTasks()
        elif choice == 'S':
            manager.show_tasks()
        elif choice == 'U':
            manager.update_task()
        elif choice == 'Q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()