class Task:
    def __init__(self, title, priority=1, completed=False):
        self.title = title
        self.priority = priority
        self.completed = completed

    def mark_as_complete(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.completed]

    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]
