from repositories import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def list_tasks(self):
        return self.repo.list()

    def create_task(self, title: str):
        return self.repo.create(title)
