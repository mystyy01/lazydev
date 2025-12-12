# barebones fastapi template
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}
if __name__ == "__main__":
    print("Run with uvicorn. More info in README.md")