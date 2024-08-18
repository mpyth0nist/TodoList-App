import csv

class TodoList():
    
    def __init__(self):
        self.tasks = [['Task', 'Priority']]

    def set_task(self,task, priority):
        self.tasks.append(f"{task}{priority}")

    def del_task(self, task):
        self.tasks.remove(task)

    def show_list(self):
        if len(self.tasks) < 2:
            print("Your ToDo List is empty, Try adding some Tasks to it!")
        else:
            sort_tasks(self.tasks)
            printable = remove_indexing(self.tasks)
            print(printable)

    def get_list(self):
        if len(self.tasks) < 2:
            return "Your list is empty."
        return remove_indexing(sort_tasks(self.tasks))


def sort_tasks(tasks):
    for i in range(1,len(tasks)-1):
        if int(tasks[i][-1]) > int(tasks[i+1][-1]):
            tasks[i],tasks[i+1] = tasks[i+1], tasks[i]


def remove_indexing(tasks):
    cleared = tasks.copy()
    for i in range(1,len(cleared)):
        cleared[i] = cleared[i].replace(cleared[i][-1], "")

    return cleared



lists = {}
print("Welcome to Tasky! A simple Minimalistic Todo-List App. \n This mini-program created a todolist for you and save it as a CSV file that you can use after.")
print("[A]: Add a Task.  \n [U]: Update a Task.  \n [S]: Show Tasks. \n [Q]: Quit the App.")
choice = input('You choose to .. : ')

td = TodoList()


while choice != 'Q':
    if choice.upper() == 'A':
        while True:

            task = input("Add Your Task Here: ")

            priority = input("Task priority[1: Crucial, 2: Important, 3: Optional]: ")

            td.set_task(task,int(priority))

            quit = input("Press q to quit or press any other key to add more tasks: ")

            if quit == 'q':
                break







