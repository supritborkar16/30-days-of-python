tasks = []

while True:
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "3":
        if not tasks:
            print("\nNo tasks to remove.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                task_num = int(input("Enter task number to remove: "))

                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"🗑️ Removed: {removed_task}")
                else:
                    print("❌ Invalid task number.")

            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":
        print("👋 Exiting To-Do List. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please select 1-4.")