import csv


# The main todo list class
class TodoList():
    
    
    def __init__(self):
        # setting the default list header
        self.tasks = [['Task', 'Priority']]

    # Add a task
    def set_task(self,task, priority):
        self.tasks.append(f"{task}{priority}")

    # Remove a task
    def del_task(self, task):
        self.tasks.remove(task)

    # Print the full Todo list
    def show_list(self):
        if len(self.tasks) < 2:
            print("Your ToDo List is empty, Try adding some Tasks to it!")
        else:
            sort_tasks(self.tasks)
            printable = remove_indexing(self.tasks)
            print(printable)

    # Return the Todo list as a value
    def get_list(self):
        if len(self.tasks) < 2:
            return "Your list is empty."
        return remove_indexing(sort_tasks(self.tasks))


# Sort task per priority
def sort_tasks(tasks):
    for i in range(1,len(tasks)-1):
        if int(tasks[i][-1]) > int(tasks[i+1][-1]):
            tasks[i],tasks[i+1] = tasks[i+1], tasks[i]


# Removes the priority indexing at the end of each task
def remove_indexing(tasks):
    cleared = tasks.copy()
    for i in range(1,len(cleared)):
        cleared[i] = cleared[i].replace(cleared[i][-1], "")

    return cleared



print("Welcome to Tasky! A simple Minimalistic Todo-List App. \n This mini-program created a todolist for you and save it as a CSV file that you can use after.")
print("[A]: Add a Task.  \n [U]: Update a Task.  \n [S]: Show Tasks. \n [Q]: Quit the App.")

choice = input('You choose to .. : ')

# Initializing a Todolist instance
td = TodoList()

# Main loop of the program.
while choice != 'Q':
    
    # If the user chooses to Add a task.
    if choice.upper() == 'A':
        while True:

            task = input("Add Your Task Here: ")

            priority = input("Task priority[1: Crucial, 2: Important, 3: Optional]: ")

            td.set_task(task,int(priority))
            
            quit = input("Press q to quit or press any other key to add more tasks: ")

            if quit == 'q':
                break







