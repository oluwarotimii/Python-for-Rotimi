#this is the To do list app
#need to use OOP
# Trying to use a idea where the code is alwsys actie and users press a letter to perform a functions?

taskFile = open('Todo.txt', "a")
class Tasks():
    def __init__ (self, name, status):

        self.name = name
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.status}"


class TaskManager():
    def __init__(self):
       self.tasks = []
       self.load_tasks()

    def load_tasks(self):
        try:
            with open('Todo.txt', 'r') as file:
                for line in file::
                    name, status = line.strip().split("-")
                    self.tasks.append(Task(name, status))
        except FileNotFoundError:
            print('No existing tasks found.')

    def save_tasks(self):
        with open('Todo.txt', 'w') as file:
            for task in self.tasks:
                file.write(f"{task.name} - {task.status}\n")

    def addTasks(name, status):
        taskName = input('Enter the Tasks: ')
        taskStatus = input('Completed or Pending? : ').capitalize()
        new_task = Task(taskName, taskStatus)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{taskName}' added!")
    
    def show_tasks(self):
        print("\n---- Your Tasks-----")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
        print('==================')

    def update_task(self):
        self.show_tasks()
        try:
            task_id = int(input("Enter the tasks number to update: ")) - 1
            if 0 <= task_id <len(self.tasks):
                print(f"Updating Task: {self.tasks[task_id]}")
                new_name = input("Enter the new Task Name (or press enter to keep current name): ")
                new_status = input("Enter the new status of the Tasks (Completedd/Pending) (or press enter to keep the current status)")
        except:



Todo = TaskManager(name, status)

        