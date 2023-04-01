'''
This is a Python console application that manages a to-do list. It provides the user with options to add tasks, mark tasks as completed, and view the list of tasks. The program stores the tasks in a text file called tasks.txt.

When the program starts, the user is presented with a menu of options to choose from. If the user selects "Add a task", they are prompted to enter the name of the task, which is then added to the tasks.txt file. If the user selects "Show tasks", the program reads the tasks from the tasks.txt file and displays them on the console. If no tasks have been added yet, the program displays a message indicating that there are no tasks. If the user selects "Mark a task as completed", the program displays the list of tasks and prompts the user to enter the number of the completed task. When the user enters the task number, the program removes the corresponding task from the tasks.txt file. Finally, if the user selects "Exit", the program terminates.'''

def show_menu():
    print('1. Add a task')
    print('2. Show tasks')
    print('3. Mark a task as completed')
    print('4. Exit')

def get_user_input():
    user_input = input('Enter your choice: ')

    if user_input in ['1', '2', '3', '4']:
        return user_input
    else:
        print('Invalid input')
        return None

def add_task():
    task_name = input('Enter task name: ')
    with open('tasks.txt', 'a') as file:
        file.write(task_name + '\n')
    print('Task added successfully!')

def view_task():
    try:
      with open('tasks.txt', 'r') as file:
          tasks = file.readlines()
          if not tasks:
              print('There are no tasks yet!')
          else:
              print('List of tasks:')
              for i, task in enumerate(tasks):
                  print(f'{i+1}. {task}')

    except FileNotFoundError as e:
        print('Error: {}'.format(e))

def mark_completed():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print('There are no tasks yet!')
            else:
                view_task()
                task_number = int(input('Enter the number of the completed task: '))
                if task_number > len(tasks):
                    print('Invalid input!')
                else:
                    with open('tasks.txt', 'w') as file:
                        for i, task in enumerate(tasks):
                            if i != task_number - 1:
                                file.write(task)
                    print('Task marked as completed!')
    except FileNotFoundError as e:
        print('Error: {}'.format(e))

def main():
    while True:
        show_menu()
        choice = get_user_input()

        if choice == '1':
            add_task()
        elif choice == '2':
            view_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            break
        else:
          print('Invalid choice!')


if __name__ == '__main__':
    main()