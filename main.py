from typing import Optional
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

app = FastAPI()

# Dummy firmware version
firmware_version = "1.0.0"

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)