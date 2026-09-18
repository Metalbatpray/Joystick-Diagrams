from dataclasses import dataclass


@dataclass
class Task:
    name: str
    priority: int
    completed: bool = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority):
        self.tasks.append(Task(name, priority))

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.completed = True
                break

    def sort_tasks(self):
        self.tasks.sort(
            key=lambda task: (task.completed, -task.priority)
        )

    def print_report(self):
        print("Task Report")
        print("===========")

        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(
                f"{task.name} | Priority: {task.priority} | {status}"
            )

        completed = sum(task.completed for task in self.tasks)
        pending = len(self.tasks) - completed

        print("===========")
        print(f"Total Tasks: {len(self.tasks)}")
        print(f"Completed: {completed}")
        print(f"Pending: {pending}")


manager = TaskManager()

manager.add_task("Build Website", 5)
manager.add_task("Write Documentation", 3)
manager.add_task("Fix Bugs", 4)
manager.add_task("Deploy Application", 5)
manager.add_task("Update Database", 2)

manager.complete_task("Build Website")
manager.complete_task("Fix Bugs")

manager.sort_tasks()
manager.print_report()
