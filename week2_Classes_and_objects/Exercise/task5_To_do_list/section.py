from task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if new_task.name == task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        deleted = 0
        for task in self.tasks:
            if task.completed:
                del task
                deleted += 1

        return f"Cleared {deleted} tasks."

    def view_section(self):
        details = []
        for task in self.tasks:
            details.append(task.details())

        sep = '\n'
        return f"Section {self.name}:\n" \
               f"{f'{sep}'.join(details)}"


section = Section("New section")
task = Task("Tst", "27.04.2020")
section.add_task(task)
section.complete_task("Tst")
message = section.clean_section()
print(message)
expected = "Cleared 1 tasks."
