from typing import Protocol, List
from sqlalchemy.orm import Session
import models


class TaskRepository(Protocol):
    def list(self, db: Session) -> List[models.Task]: ...
    def create(self, db: Session, title: str) -> models.Task: ...


class SQLAlchemyTaskRepository:
    def list(self, db: Session):
        return db.query(models.Task).all()

    def create(self, db: Session, title: str):
        new_task = models.Task(title=title)
        db.add(new_task)
        # NOTE: do not commit here — transaction managed by service/unit-of-work
        db.flush()
        db.refresh(new_task)
        return new_task
