from typing import Protocol, List
from sqlalchemy.orm import Session
import models


class TaskRepository(Protocol):
    def list(self) -> List[models.Task]: ...
    def create(self, title: str) -> models.Task: ...


class SQLAlchemyTaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self):
        return self.db.query(models.Task).all()

    def create(self, title: str):
        new_task = models.Task(title=title)
        self.db.add(new_task)
        # commit inside repository to keep transactional behavior consistent
        self.db.commit()
        self.db.refresh(new_task)
        return new_task
