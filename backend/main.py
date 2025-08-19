from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

react_build_path = os.path.join(os.path.dirname(__file__), "..", "React", "my-app", "build")

app.mount("/static", StaticFiles(directory=os.path.join(react_build_path, "static")), name="static")

@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_file = os.path.join(react_build_path, "index.html")
    return FileResponse(index_file)
