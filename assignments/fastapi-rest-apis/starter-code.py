from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI()

# Define Pydantic models for data validation
class TodoItem(BaseModel):
    """Model for a todo item"""
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for todos
todos: List[TodoItem] = []
next_id = 1

# TODO: Implement GET endpoint to retrieve all todos
@app.get("/todos")
def get_todos():
    """Retrieve all todos or filter by completion status"""
    pass

# TODO: Implement GET endpoint to retrieve a specific todo by id
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    """Retrieve a specific todo item by ID"""
    pass

# TODO: Implement POST endpoint to create a new todo
@app.post("/todos")
def create_todo(todo: TodoItem):
    """Create a new todo item"""
    pass

# TODO: Implement PUT endpoint to update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: TodoItem):
    """Update an existing todo item"""
    pass

# TODO: Implement DELETE endpoint to remove a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    """Delete a todo item"""
    pass

# Run the app with: uvicorn starter-code:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
