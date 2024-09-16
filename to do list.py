

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '2':
        if tasks:
            print("\nYour To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your to-do list is empty.")

    elif choice == '3':
        if tasks:
            print("\nYour To-Do List:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task}")
            task_no = int(input("Enter the task number to update: "))
            if 1 <= task_no <= len(tasks):
                new_task = input("Enter the updated task: ")
                tasks[task_no - 1] = new_task
                print("Task updated.")
            else:
                print("Invalid task number.")
        else:
            print("Your to-do list is empty.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
