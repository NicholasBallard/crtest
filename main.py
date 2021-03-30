from fastapi import FastAPI


app = FastApi()

@app.get("/")
def main():
    return {"hi": "there"}
