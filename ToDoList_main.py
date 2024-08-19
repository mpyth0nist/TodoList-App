import csv

from tabulate import tabulate


# The main todo list class
class TodoList():

    def __init__(self):
        # setting the default list header
        self.task_num = 1
        self.tasks = [["Task Number", "Task", "Task Priority"]]

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

            table = tabulate(self.tasks[1:], self.tasks[0], tablefmt='grid')

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


def show_all_lists(lists):
    
    todolists = [lists[l] for l in lists]
        
        
    j = 1
    for i in range(len(todolists)):
        print(f"Todolist Number {j}")
        todolists[i].show_list()
        j+=1

def save_list(l):
    with open(f"{l}.csv", 'w', newline="") as file:
        todo_list = csv.writer(file)
        todo_list.writerows(lists[l].get_list())



print("Welcome to Tasky! A simple Minimalistic Todo-List App. \n This mini-program created a todolist for you and save it as a CSV file that you can use after.")


# Initializing a Todolist instance

lists = {}
choice = ''
todolists = [lists[l] for l in lists]

# Main loop of the program.
while choice != 'Q':

    print("[N]: Create a new ToDo List. \n [L]: Show Todo Lists \n [S]: Save Lists \n[Q]: Quit the App.")

    choice = input('You choose to .. : ')
    
    if choice.upper() == 'N':
        list_name = input("Name your list: ")
        td = TodoList()
        lists[list_name] = td
        print("Your ToDo list is created and ready to be filled with tasks")
        print("Press [A] to Add Tasks to that list or press any other keys to get back to main menu")

        choice = input("You choose to..: ")


        if choice.upper() == 'A':

            while True:
                task = input("Add Your Task Here: ")

                priority = input("Task priority[1: Crucial, 2: Important, 3: Optional]: ")

                add_task(td, task, priority)

                stop = input("Press [q] if you want to quit or any other key to keep on adding tasks: ")

                if stop.upper() == 'Q':
                    break

        continue

    if choice.upper() == 'L':

        show_all_lists(lists)
        
        print("[U]: Update a ToDo list. \n [D]: Delete a list \n [B]: Main Menu")

        choice = input("You choose: ")

        if choice.upper() == 'U':

            while choice.upper() != 'N':

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

                choice = input("Want to keep updating this list? [Y/N]: ")

        if choice.upper() == 'B':
            continue

    if choice.upper() == 'S':

        print("[1]. Save All lists \n [2]. Save a specific list")
        choice = int(input("Enter a number: "))
        if choice == 1:
            for l in lists:
                save_list(l)

            print("Your Lists are saved Sucessfully!")

        if choice == 2:
            stop = ''
            while stop != 'q':
                show_all_lists(lists)
                choice = input("Choose a specific list by it's number: ")
                choice = int(choice)

                list_name = list(lists.keys())[choice-1]
                
                save_list(list_name)

                print("Your List is saved Sucessfully!")

                stop = input("Press [q] to go back to main menu \n or press any key if you want to save another list: ")




            





        










