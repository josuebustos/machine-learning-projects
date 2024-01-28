from fastapi import FastAPI, HTTPException, Depends, Query
from databases import database
from sqlalchemy import select
from app.models import tasks

app = FastAPI()


@app.post("/tasks/")
async def create_task(title: str, description: str = ""):
    query = tasks.insert().values(title=title, description=description)
    await database.execute(query)
    return {"message": "Task created successfully"}


@app.put("/tasks/{task_id}/")
async def update_task(task_id: int, title: str, description: str = ""):
    query = (
        tasks.update()
        .where(tasks.c.id == task_id)
        .values(title=title, description=description)
    )
    await database.execute(query)
    return {"message": "Task updated successfully"}


@app.get("/tasks/{task_id}/")
async def get_task(task_id: int):
    query = select([tasks]).where(tasks.c.id == task_id)
    result = await database.fetch_one(query)
    if result is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return result


@app.get("/tasks/")
async def get_tasks():
    query = select([tasks])
    results = await database.fetch_all(query)
    return results


@app.delete("/tasks/{task_id}/")
async def delete_task(task_id: int):
    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
    return {"message": "Task deleted successfully"}
