# from typing import Optional
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse



app = FastAPI()

# Dummy firmware version
firmware_version = "1.0.0"

# Mounting static files directory
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates directory
# templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# async def home(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request, "version": firmware_version})


@app.get("/firmware/version")
async def get_firmware_version():
    return {"version": firmware_version}


@app.post("/firmware/version")
async def set_firmware_version(version: str):
    global firmware_version
    firmware_version = version
    return {"message": "Firmware version set successfully", "version": firmware_version}


@app.post("/firmware/bin")
async def upload_bin_file(file: UploadFile = File(...)):
    # Save the uploaded .bin file
    with open(file.filename, "wb") as buffer:
        buffer.write(await file.read())
    return {"message": "File uploaded successfully"}


@app.get("/firmware/bin")
async def download_bin_file():
    # You may implement logic here to return the appropriate .bin file
    # For now, just returning a sample file named "example.bin"
    file_path = "example.bin"
    return FileResponse(file_path, media_type="application/octet-stream")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)