#this is the To do list app
#need to use OOP


taskFile = open('Todo.txt', "w")
class Tasks():
    def __init__ (self, name, status):

        self.name = name
        self.status = status


class TaskManager():
    def __init__(self):
        # taskFile = open('Todo.txt', "w")
        self.tasks = open('Todo.txt', "w")

    def addTasks(name, status):
        taskName = input('Enter the Tasks: ')
        taskStatus = input('Completed or Pending? : ')
        name = taskName
        status = taskStatus
        taskFile.write(taskName)



Todo = TaskManager(name, status)

        