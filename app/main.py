import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host="192.168.31.94", port=8000, reload=True)