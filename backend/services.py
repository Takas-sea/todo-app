from sqlalchemy.orm import Session
from repositories import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def list_tasks(self, db: Session):
        return self.repo.list(db)

    def create_task(self, db: Session, title: str):
        try:
            task = self.repo.create(db, title)
            db.commit()
            return task
        except Exception:
            db.rollback()
            raise
