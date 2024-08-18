import csv

from tabulate import tabulate


# The main todo list class
class TodoList():

    def __init__(self):
        # setting the default list header
        self.task_num = 1
        self.tasks = []

    # Add a task
    def set_task(self,task, priority):
        self.tasks.append([self.task_num,task,priority])
        self.task_num+=1

    # Update a task.
    def update_task(self, task_num, new_task):
        # Search for the task in the todo list
        for i in range(0,len(self.tasks)):
                # Replace it if found in the list
            if self.tasks[i][0] == task_num:
                self.tasks[i][1] = new_task

    # Remove a task
    def del_task(self, task):
        self.tasks.remove(task)

    # Print the full Todo list
    def show_list(self):
        if len(self.tasks) < 1:
            print("Your ToDo List is empty, Try adding some Tasks to it!")
        else:
            headers = ['Task Number', 'Task', 'Priority']

            table = tabulate(self.tasks, headers, tablefmt='grid')

            print(table)

    # Return the Todo list as a value
    def get_list(self):
        if len(self.tasks) < 1:
            return "Your list is empty."
        return self.tasks




def add_task(td,t,p):

    td.set_task(t,int(p))


def edit_task(td,t1,t2):
    td.update_task(t1,t2)



print("Welcome to Tasky! A simple Minimalistic Todo-List App. \n This mini-program created a todolist for you and save it as a CSV file that you can use after.")


# Initializing a Todolist instance

lists = {}
choice = ''
# Main loop of the program.
while choice != 'Q':

    print("[N]: Create a new ToDo List. \n [S]: Show Todo Lists \n [Q]: Quit the App.")

    choice = input('You choose to .. : ')
    
    if choice.upper() == 'N':
        list_name = input("Name your list: ")
        td = TodoList()
        lists[list_name] = td
        print("Your ToDo list is created and ready to be filled with tasks")
        print("Press [A] to Add Tasks to that list or press any other keys to get back to main menu")

        user_choice2 = input("You choose to..: ")

        if user_choice2.upper() == 'A':

            while True:
                task = input("Add Your Task Here: ")

                priority = input("Task priority[1: Crucial, 2: Important, 3: Optional]: ")

                add_task(td, task, priority)

                stop = input("Press [q] if you want to quit or any other key to keep on adding tasks: ")

                if stop.upper() == 'Q':
                    break

        continue


    # If the user chooses to Add a task.

    if choice.upper() == 'U':
        while True:
            
            # Getting the task number
            user_input = input("Which task you want to update? \n[ If you forgot the task number, You can list all tasks to choose which one by typing 's' ]: ")
            
            if user_input.upper() == 'S':
                print("[TASK_NUMBER, TASK, PRIORITY]")
                print(td.get_list()[1:])
                continue
            
            else:
                
                # converting the input into an int

                task_num = int(user_input)

                # Getting the new task
                new_task = input("Enter the new task: ")

                # Updating the task
                td.update_task(task_num, new_task)

                # Printing the Updated ToDo list
                print(td.get_list())

    if choice.upper() == 'S':

        todolists = [lists[l] for l in lists]
        
        
        j = 1
        for i in range(len(todolists)):
            print(f"Todolist Number {j}")
            todolists[i].show_list()
            j+=1
        
        print("[U]: Update a ToDo list. \n [D]: Delete a list \n [B]: Main Menu")

        user_choice3 = input("You choose: ")

        if user_choice3.upper() == 'U':

            # the user chooses which list he's going to edit
            num = input("Choose the list by its number: ")
            num = int(num)
            # getting the list by its number from the todolists collection
            user_todolist = todolists[num-1]
            
            # List all the list's tasks.
            user_task = input("Choose which task you want to update by its Task Number in the list or press q to quit: ")

            user_task = int(user_task)
            
            if user_task == 'q':
                continue

            new_task = input("Enter the new task here: ")

            edit_task(user_todolist, user_task, new_task)

            print("ToDo List Updated!")

            user_todolist.show_list()





        










