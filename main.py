from fastapi import FastAPI

app = FastAPI()

tasks = []

@app.get("/")
def home():
    return {"message": "Todo API running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/add-task")
def add_task(task: str):
    tasks.append(task)
    return {"message": "Task added", "tasks": tasks}

@app.delete("/delete-task")
def delete_task(task: str):
    if task in tasks:
        tasks.remove(task)
        return {"message": "Task deleted", "tasks": tasks}
    return {"message": "Task not found"}