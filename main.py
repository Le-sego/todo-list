
# Function to display the to-do list
def display_list(todo_list):
    # Checking if the to-do list is empty
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        # Printing each task in the to-do list with its index
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the to-do list
def add_task(todo_list, task):
    # Appending the new task to the to-do list
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(todo_list, task_index):
    # Checking if the task index is valid
    if 1 <= task_index <= len(todo_list):
        # Removing the task at the specified index
        removed_task = todo_list.pop(task_index - 1)
        print(f"Task '{removed_task}' removed from the to-do list.")
    else:
        print("Invalid task index.")


# Main function
def main():
    # Initializing an empty list to store tasks
    todo_list = []

    while True:
        # Displaying options to the user
        print("\nOptions:")
        print("1. Display to-do list")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")

        # Asking for user input to choose an option
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_list(todo_list)
        elif choice == "2":
            # Asking the user for a task and add it to the to-do list
            task = input("Enter the task: ")
            add_task(todo_list, task)
        elif choice == "3":
            # Asking the user for the task index to remove
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            # Exiting the program when the user chooses to quit
            print("Exiting the to-do list app. Goodbye!")
            break
        else:
            # Handling invalid user input
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Start the application by calling the main function
    main()
