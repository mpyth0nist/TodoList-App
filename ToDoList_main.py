import csv


# The main todo list class


class TodoList():
    

    def __init__(self):
        # setting the default list header
        self.task_num = 1
        self.tasks = [['Task', 'Priority']]

    # Add a task
    def set_task(self,task, priority):
        self.tasks.append([self.task_num,task,priority])
        self.task_num+=1

    # Update a task.
    def update_task(self, task_num, new_task):
        # Search for the task in the todo list
        for i in range(1,len(self.tasks)):
                # Replace it if found in the list
            if self.tasks[i][0] == task_num:
                self.tasks[i][1] = new_task

    # Remove a task
    def del_task(self, task):
        self.tasks.remove(task)

    # Print the full Todo list
    def show_list(self):
        if len(self.tasks) < 2:
            print("Your ToDo List is empty, Try adding some Tasks to it!")
        else:
            print(self.tasks)

    # Return the Todo list as a value
    def get_list(self):
        if len(self.tasks) < 2:
            return "Your list is empty."
        return self.tasks




print("Welcome to Tasky! A simple Minimalistic Todo-List App. \n This mini-program created a todolist for you and save it as a CSV file that you can use after.")


# Initializing a Todolist instance
td = TodoList()

choice = ''
# Main loop of the program.
while choice != 'Q':

    print("[A]: Add a Task.  \n [U]: Update a Task.  \n [S]: Show Tasks. \n [Q]: Quit the App.")

    choice = input('You choose to .. : ')
    
    # If the user chooses to Add a task.
    if choice.upper() == 'A':
        while True:

            task = input("Add Your Task Here: ")

            priority = input("Task priority[1: Crucial, 2: Important, 3: Optional]: ")

            td.set_task(task,int(priority))

            quit = input("Press q to quit or press any other key to add more tasks: ")

            if quit == 'q':
                break

    if choice.upper() == 'U':
        while True:
            
            # Getting the task number
            user_input = input("Which task you want to update? \n[ If you forgot the task number, You can list all tasks to choose which one by typing 's' ]: ")
            
            if user_input.upper() == 'S':
                print("[TASK_NUMBER, TASK, PRIORITY]")
                print(td.get_list()[1:])
                continue
            # converting the input into an int
            
            else:
                task_num = int(user_input)

                # Getting the new task
                new_task = input("Enter the new task: ")

                # Updating the task
                td.update_task(task_num, new_task)

                # Printing the Updated ToDo list
                print(td.get_list())










