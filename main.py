from fastapi import FastApi


app = FastApi()

@app.get("/")
def main():
    return {"hi": "there"}
