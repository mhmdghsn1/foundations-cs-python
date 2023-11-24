class Task:
    counter = 1

    def __init__(self, description, priority):
        self.task_id = Task.counter
        Task.counter += 1
        self.description = description
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __lt__(self, other):
        return self.priority < other.priority


class Priority:
    def __init__(self):
        self.tasks = []

    def enqueue(self, task):
        self.tasks.append(task)
        self.tasks.sort()

    def dequeue(self):
        if not self.is_empty():
            return self.tasks.pop(0)

    def is_empty(self):
        return len(self.tasks) == 0


class Stack:
    def __init__(self):
        self.tasks = []

    def push(self, task):
        self.tasks.append(task)

    def pop(self):
        if not self.is_empty():
            return self.tasks.pop()

    def is_empty(self):
        return len(self.tasks) == 0


class TaskManager:
    def __init__(self):
        self.task_queue = Priority()
        self.task_history = Stack()

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.task_queue.enqueue(task)

    def get_task(self, task_id):
        for task in self.task_queue.tasks:
            if task.task_id == task_id:
                return task

    def mark_highest_priority_task_completed(self):
        task = self.task_queue.dequeue()
        if task:
            task.mark_completed()
            self.task_history.push(task)

    def display_all_tasks(self):
        print("All tasks:")
        if self.task_queue.is_empty():
            print("No tasks.")
        else:
            for task in self.task_queue.tasks:
                print(f"Task ID: {task.task_id}, Description: {task.description}, Priority: {task.priority}")

    def display_incomplete_tasks(self):
        print("Incomplete tasks:")
        incomplete_tasks = [task for task in self.task_queue.tasks if not task.completed]
        if not incomplete_tasks:
            print("No incomplete tasks.")
        else:
            for task in incomplete_tasks:
                print(f"Task ID: {task.task_id}, Description: {task.description}, Priority: {task.priority}")

    def display_last_completed_task(self):
        print("Last completed task:")
        task = self.task_history.pop()
        if task:
            print(f"Task ID: {task.task_id}, Description: {task.description}, Priority: {task.priority}")
        else:
            print("No completed tasks.")

    def display_menu(self):
        while True:
            print("\nTask Management Menu:")
            print("1. Add a new task")
            print("2. Get a task by ID")
            print("3. Mark the highest priority task as completed")
            print("4. Display all tasks")
            print("5. Display incomplete tasks")
            print("6. Display last completed task")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                description = input("Enter the task description: ")
                priority = int(input("Enter the task priority: "))
                self.add_task(description, priority)
                print("Task added successfully.")
            elif choice == "2":
                task_id = int(input("Enter the task ID: "))
                task = self.get_task(task_id)
                if task:
                    print(f"Task ID: {task.task_id}, Description: {task.description}, Priority: {task.priority}")
                else:
                    print("Task not found.")
            elif choice == "3":
                self.mark_highest_priority_task_completed()
                print("Marked the task as completed.")
            elif choice == "4":
                self.display_all_tasks()
            elif choice == "5":
                self.display_incomplete_tasks()
            elif choice == "6":
                self.display_last_completed_task()
            elif choice == "7":
                print("Exiting the task management system...")
                break
            else:
                print("Invalid choice. Please try again.")