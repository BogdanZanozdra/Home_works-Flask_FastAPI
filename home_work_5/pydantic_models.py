from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    status: str = 'Не выполнена'
