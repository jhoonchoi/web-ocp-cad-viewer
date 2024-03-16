from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse

app = FastAPI()

# Serve static files, assuming you have a "static" folder in your project directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_viewer():
    return FileResponse('static/index.html')

@app.post("/upload-json/")
async def upload_json(file: UploadFile = File(...)):
    content = await file.read()
    # You might want to process the JSON or simply save it to serve later
    # For this example, let's assume you save it to a file
    with open("static/model.json", "wb") as f:
        f.write(content)
    return {"filename": file.filename}