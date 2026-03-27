from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import schemas
from services import TaskService
from repositories import SQLAlchemyTaskRepository, TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])


def get_task_repository() -> TaskRepository:
    return SQLAlchemyTaskRepository()


def get_task_service(repo: TaskRepository = Depends(get_task_repository)):
    return TaskService(repo)


@router.get("", response_model=list[schemas.Task])
def get_tasks(service: TaskService = Depends(get_task_service), db: Session = Depends(get_db)):
    return service.list_tasks(db)


@router.post("", response_model=schemas.Task)
def add_task(task: schemas.TaskCreate, service: TaskService = Depends(get_task_service), db: Session = Depends(get_db)):
    return service.create_task(db, task.title)
