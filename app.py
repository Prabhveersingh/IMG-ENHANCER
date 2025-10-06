from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import os

# Folder paths (keep this file next to index.html and models/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

app = FastAPI(title="Image Enhancer Host")

# Serve everything in the current folder as static (models/, images, JS, CSS…)
app.mount("/", StaticFiles(directory=BASE_DIR, html=True), name="static")

# Optional: explicit root route to index.html
@app.get("/")
def root():
    return FileResponse(INDEX_FILE)

if __name__ == "__main__":
    # 0.0.0.0 so it’s reachable on LAN/cloud; change port if you like
    uvicorn.run(app, host="0.0.0.0", port=8000)
