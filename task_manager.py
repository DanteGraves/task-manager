# Import section.
from datetime import date, datetime
import re

# Empty lists for storing data as lists.
username= []
password= []
today= date.today()

# Code to open data.txt file.
with open("user.txt" , "r") as file:
    for rows in file:
        # Split text in file into strings.
        temp= rows.split()
        
        # Assign data of strings to correct lists.
        username.append(temp[0].replace(",", "")) 
        password.append(temp[1])

# Create function for user registry.
def reg_user():
    # Request input from user.
    new_username= input("Please enter new username for registry [username must be more than 4 characters] : \n")

    # Check if username is more than 4 characters.
    if len(new_username) > 4:

        # If username does not exist new loop starts.
        if new_username not in username:

            # Prompts user to enter a password.
            new_password = input("Please enter a password [must contain one special character ]: \n")

            if re.search(r"[!@#$%^&*()_+{}[\]:;<>,.?~]", new_password):

                # Prompts user to confirm password.
                final_password= input("Confirm password : \n")

                # If both password entries match username and password will be appended to data file.
                if final_password == new_password:

                    # Opens data.txt file to append lists.
                    with open("user.txt", "a") as file:
                                
                        # Writes new data to user.txt file.
                        file.write(f"\n{new_username}, {new_password}")

                        # Prints confirmation of registry.
                        print("User registered successfully! \n")

                # Error message if password entries do not match.
                else:
                    print("password entries do not match! \n")

            # Error message if user entered password without a special character.
            else:
                print("Password must contain a special character!\n")

        # Error message if username already exists.
        elif new_username in username:
            print("Username already exists!")

    # Error message if username is too short.
    else:
        print("Username should be more than 4 characters!\n")
# End function.
        
# Create function for adding tasks.
def add_task():
    # Open tasks.txt file.
    with open("tasks.txt", "a") as file:
                    
        # Code block to request details from user.
        task_username= input("Please enter the username assigned to the task : \n")
        task_title= input("Please enter the tasks title :\n")
        task_description= input("Please enter description of task : \n")
        task_date= input("Please enter the tasks due date : \n")
        task_completion= "No"

        # Write details obtained from user to tasks.txt file.
        file. write(f"\n{task_username}, {task_title}, {task_description}, {today}, {task_date}, {task_completion}")

        # Shows confirmation of task registry.
        print("\nTask registry completed! \n")
# End function.
        
# Create function for displaying all tasks.
def view_all():
    # Open tasks.txt.
    with open("tasks.txt", "r") as file:
        for line in file:
                            
            # Empty lists for storing data.
            task_user = []
            task_name= []
            task_details= []
            task_entered= []
            task_due_date= []
            task_completed= []

            # Split string into lists.
            temp = line.split(",")
            # Remove unnecessary characters.
            temp = [item.strip("[]' ") for item in temp]  

            # Append lines to corresponding lists.
            task_user.append(temp[0])
            task_name.append(temp[1])
            task_details.append(temp[2])
            task_entered.append(temp[3])
            task_due_date.append(temp[4])
            task_completed.append(temp[5])

            # Print each task individually.
            for i in range(len(task_user)):
                print()
                print(f"User assigned to task:     {task_user[i]}")
                print(f"Title of task:             {task_name[i]}")  
                print(f"Task created:              {task_entered[i]}")
                print(f"Task due date:             {task_due_date[i]}")
                print(f"Task completed:            {task_completed[i]}")
                print(f"Task description:\n{task_details[i]}")
                print()
                print("Next task:")
# End function.
                
# Create function to view tasks matching login username.
def view_mine():
    # Empty lists for storing data.
    task_assigned = []
    task_title = []
    task_description = []
    task_today = []
    task_final_date = []
    task_finished = []

    # Code block to open tasks.txt file and sort lists into correct variables.
    with open("tasks.txt", "r") as file:
        for line in file:

            # Split string into lists.
            temp = line.split(",")
            # Remove unnecessary characters.
            temp = [item.strip("[]' ") for item in temp]

            # Append lists to corresponding variables.
            task_assigned.append(temp[0])
            task_title.append(temp[1])
            task_description.append(temp[2])
            task_today.append(temp[3])
            task_final_date.append(temp[4])
            task_finished.append(temp[5])

    # Check if login username match any tasks.
    matching_tasks = []
    for i in range(len(task_assigned)):
        if login_username == task_assigned[i]:
            matching_tasks.append(i)

    # If the usernames match any tasks those tasks are printed out.
    if matching_tasks:
        for i in matching_tasks:

            print(f"Task {i + 1}: ")     
            print(f"User assigned to task:        {task_assigned[i]}")
            print(f"Title of task:                {task_title[i]}") 
            print(f"Task created:                 {task_today[i]}")
            print(f"Task due date:                {task_final_date[i]}")
            print(f"Task completed:               {task_finished[i]}")
            print(f"Task description:\n{task_description[i]}")
            print()
        
        # Start while loop for user to edit task information.
        while True:
            # Request user to input task to edit.
            task_number_input= int(input("Please enter task number you wish to proceed with or enter -1 to return to main menu: \n"))

            if task_number_input != -1:
                # Request user to choose between two options to continue.
                task_adjust= input("Enter yes to mark task as complete, Enter No to edit task details : \n").lower()

                # If user chooses 'yes' code block will edit task_finished details and write to file. 
                if task_adjust == "yes":
                    task_finished[i]= "Yes"

                    with open("tasks.txt", "w") as file:

                        for j in range (len(task_assigned)):
                        
                            file.write(f"{task_assigned[j]}, {task_title[j]}, {task_description[j]}, {task_today[j]}, {task_final_date[j]}, {task_finished[j]}")
                        print("Task updated!\n")

                # If user chose 'no' code block will request new information and write to file.
                elif task_adjust == "no":
                    
                    # If the task is marked incomplete user can edit details.
                    if task_finished[i] == "No":
                        
                        # Request new details from user.
                        new_task_username= input("Please enter new username to assign to task : \n")
                        new_due_date= input("Please enter new task due date : \n")

                        # Assign new value to variables.
                        task_assigned[i] = new_task_username
                        task_final_date[i] = new_due_date

                        # Open text file and write new data to file.
                        with open("tasks.txt", "w") as file:

                            for j in range(len(task_assigned)):

                                file.write(f"{task_assigned[j]}, {task_title[j]}, {task_description[j]}, {task_today[j]}, {task_final_date[j]}, {task_finished[j]}")
                            print("Task updated!\n")

                    # Error message if task is already marked completed and no details can be changed.
                    else:
                        print("Task is already completed!\n")

                # Error message if user entered incorrectly.
                else:
                    print("Invalid entry!")

            # If user entered -1 code will break and send user back to main menu.
            elif task_number_input == -1:
                
                print("Returning to main menu.\n")
                break

    # Shows error message if no matching tasks are found.                       
    else:
        print("No tasks found!\n")
# End function.
            
# Create function for displaying statistics.
def display_stat():
    # Line count starting at 0.
    line_count_user= 0
    line_count_tasks= 0

    # Open user.txt file and count number of lines +1.
    with open("user.txt", "r") as file:
        for lines in file:
            line_count_user += 1

    # Open tasks.txt file and count number of lines +1.       
    with open("tasks.txt", "r") as file:
        for lines in file:
            line_count_tasks += 1

    # Print out the totals of lines counted to respective categories. 
    print("Checking 'user.txt' and 'tasks.txt' files : \n")       
    print(f"The total number of registered users in 'user.txt' is :     {line_count_user}") 
    print(f"The total number of tasks registered in 'tasks.txt' is :    {line_count_tasks}")
    print()

    # Call function to generate rapport.
    print("General report overview :")
    gen_raport()

# End function.

# Create function to generate rapport to user.
def gen_raport():
   
    task_user = []
    task_date= []
    task_complete= []
    
    # Open tasks.txt file and extract needed data
    with open("tasks.txt", "r") as file:
        for line in file :

            # Split string into lists.
            temp = line.split(",")
            # Remove unnecessary characters.
            temp = [item.strip("[]' \n") for item in temp]

            task_user.append(temp[0])
            task_date.append(temp[4])
            task_complete.append(temp[5])

    # Convert date string to usable format.
    parsed_task_date = [datetime.strptime(date_str, '%d %b %Y').date() for date_str in task_date]

    # Calculate data extracted from file.
    total_tasks= len(task_user)
    total_completed= task_complete.count("Yes")
    total_uncompleted= len(task_user) - total_completed
    total_overdue = sum(1 for overdue, parsed_date in zip(task_complete, parsed_task_date) if overdue != "Yes" and parsed_date < today)
    percent_incomplete = (total_uncompleted / total_tasks) * 100
    percent_overdue = (total_overdue / total_tasks) * 100

    # Print data to user.
    print("Task overview:")
    print(f"The total number of tasks that have been generated and tracked using the task_manager.py is :    {total_tasks}")
    print(f"The total number of completed tasks is :                                                         {total_completed}")
    print(f"The total number of uncompleted tasks is :                                                       {total_uncompleted}")
    print(f"The total number of tasks that have not been completed and that are overdue is :                 {total_overdue}")
    print(f"The percentage of tasks that are incomplete is :                                                 {percent_incomplete:.2f}%")
    print(f"The percentage of tasks that are overdue is :                                                    {percent_overdue:.2f}%")
    print()

    # Write data to new task_overview file.
    with open("task_overview.txt", "w") as file:
        file.write(f"The total number of tasks that have been generated and tracked using the task_manager.py is : {total_tasks}\nThe total number of completed tasks is : {total_completed}\nThe total number of uncompleted tasks is : {total_uncompleted}\nThe total number of tasks that have not been completed and that are overdue is : {total_overdue}\nThe percentage of tasks that are incomplete is : {percent_incomplete:.2f}%\nThe percentage of tasks that are overdue is : {percent_overdue:.2f}%")

    # Count the number of users registred in user.txt file.
    line_count_in_user = 0
    with open("user.txt", "r") as file:
        for line in file:
            line_count_in_user += 1

    # Open new user_overview.txt file.
    with open("user_overview.txt", "w") as f:
        
        # Write data to file.
        f.write(f"The total number of users registered with task_manager.py is : {line_count_in_user}\n")
        f.write(f"The total number of tasks that have been generated and tracked using task_manager.py is : {total_tasks}\n")

        # Print initial data to user.
        print("User overview: ")
        print(f"The total number of users registered with task_manager.py is :                              {line_count_in_user}")
        print(f"The total number of tasks that have been generated and tracked using task_manager.py is :   {total_tasks}")
        print()
        
        # Create lists to store needed variables
        users = list(set(task_user))
        total_assigned = [task_user.count(user) for user in set(task_user)]
        percent_assigned = [(count / total_tasks) * 100 for count in total_assigned]
        percent_assigned_complete = []
        percent_assigned_incomplete = []
        percent_overdue_incomplete = []

        # Calculate data collection for each user.
        for user in users:

            user_tasks = [task_complete[i] for i in range(len(task_user)) if task_user[i] == user]
            completed_count = user_tasks.count("Yes")
            assigned_to_user = total_assigned[users.index(user)]
            incomplete_count = total_tasks - completed_count - total_assigned[users.index(user)]
            overdue_incomplete_count = sum(1 for overdue, parsed_date in zip(user_tasks, parsed_task_date) if overdue != "Yes" and parsed_date < today)
            percent_assigned_complete.append((completed_count / assigned_to_user) * 100 )
            percent_assigned_incomplete.append(((incomplete_count - completed_count) / assigned_to_user) * 100)
            percent_overdue_incomplete.append((overdue_incomplete_count / assigned_to_user) * 100 )

        # Loop through all users.
        for i, user in enumerate(users):

            # Print collected data to user.
            print(f"For user {user}:")
            print(f"The total number of tasks assigned is :                                                     {total_assigned[i]}")
            print(f"The percentage of the total number of tasks that have been assigned is :                    {percent_assigned[i]:.2f}%")
            print(f"The percentage of the tasks assigned that have been completed is :                          {percent_assigned_complete[i]:.2f}%")
            print(f"The percentage of the tasks assigned that must still be completed is :                      {percent_assigned_incomplete[i]:.2f}%")
            print(f"The percentage of the tasks assigned that has not yet been completed and are overdue is :   {percent_overdue_incomplete[i]:.2f}%")
            print()

            # Write extracted data to user_overview file.
            f.write(f"For user {user}:\n")
            f.write(f"The total number of tasks assigned is : {total_assigned[i]}\n")
            f.write(f"The percentage of the total number of tasks that have been assigned is : {percent_assigned[i]:.2f}%\n")
            f.write(f"The percentage of the tasks assigned that have been completed is :  {percent_assigned_complete[i]:.2f}%\n")
            f.write(f"The percentage of the tasks assigned that must still be completed is : {percent_assigned_incomplete[i]:.2f}%\n")
            f.write(f"The percentage of the tasks assigned that has not yet been completed and are overdue is : {percent_overdue_incomplete[i]:.2f}%\n")
# End function.
            
# Start loop for login protocol.
while True:

    # Prompts user to input a username.
    login_username= input("Please enter your username : \n")

    # If correct username is enter user is prompted to enter their password.
    if login_username in username:
        login_password= input("Please enter your password : \n")
        print()

        # If correct password is entered menu will be displayed.
        if login_password in password:
        
        # Start loop for menu selection.
         while True:

            # Menu details will be printed out for admin user.
            if login_username == "admin": 
                print("Menu options: \n r - register a user \n a - add task \n va - view all tasks \n vm - view my tasks \n gr - generate report \n ds- display statistics \n e - exit \n")

            # Menu details will be printed out for non admin users.
            else:   
                print("Menu options: \n r - register a user \n a - add task \n va - view all tasks \n vm - view my tasks \n gr - generate report \n e - exit \n")

            # User is promted to choose an option from the menu.
            menu= input("Please select from the options above: \n").lower()
            print()

            # Call function if user inputs 'r'.
            if menu == "r":
                
                # If user is logged in as 'admin' reg_user function will run.
                if login_username == "admin":
                    reg_user()

                # If user is not logged in as 'admin' error message will show.
                else:
                    print("Only admin can register new users!\n")
                    
            # Call function if user inputs 'a'.
            elif menu == "a":
                add_task()
            
            # Call function if user inputs 'va'.
            elif menu == "va":
                view_all()

            # Call function if user inputs 'vm'.
            elif menu == "vm":
                view_mine()

            # Call function if user inputs 'ds'.
            elif menu == "ds":
                display_stat()

            #Call function if user inputs 'gr'.
            elif menu == "gr":
                gen_raport()
            
            # Start loop for option to exit the menu.
            elif menu == "e":

                # Sign off message will print.
                print("Goodbye!!! \n")

                # End loop.
                break
            
            # Error message if invalid option is entered in the menu option.
            else:
                print("Entry invalid, please try again \n")

        # If incorrect password is entered error message will show and user will be prompted to re-enter username and password.       
        else:
            print("Incorrect password, please try again \n")

    # If incorrect username is entered error message will show and user will be prompted to re-enter username.
    else:
        print("username incorrect please try again \n")   

# End code.
