from fastapi import FastAPI
import user
from database import engine
import user_controller
user.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Md Mahfuzur Rahman")

app.include_router(user_controller.router)

@app.get("/")
def home():
    return {"message": "Hello Bangladesh"}