#this is the To do list app
#need to use OOP
# Trying to use a idea where the code is alwsys actie and users press a letter to perform a functions?

taskFile = open('Todo.txt', "a")
class Tasks():
    def __init__ (self, name, status):

        self.name = name
        self.status = status


class TaskManager():
    def __init__(self):
        # taskFile = open('Todo.txt', "w")
        self.tasks = open('Todo.txt', "a")

    def addTasks(name, status):
        taskName = input('Enter the Tasks: ')
        taskStatus = input('Completed or Pending? : ')
        name = taskName
        status = taskStatus
        taskFile.write(taskName)



Todo = TaskManager(name, status)

        