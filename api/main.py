
from fastapi import FastAPI
import uvicorn

from action import Action
a = Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/my_name")
def read_root():
    data = "Jirapat Kesornbua"
    return data


@app.get("/input_name")
def input_name(name):
    data = name
    return data


@app.get("/input_name_2")
def input_name_2(name, last_name):
    data = "{}-{}".format(name, last_name)
    return data


@app.get("/formula")
def formula(s, t):
    v = float(s) / float(t)
    data = "V = {:.2f}".format(v)
    return data


@app.get("/r")
def r(r1, r2, r3):
    rt1 = float(r1)+float(r2)+float(r3)
    rt2 = ((1/float(r1))+(1/float(r2))+(1/float(r3)))**-1
    data = {"อนุกรม": rt1, "ขนาน": rt2}
    return data


@app.get("/diff")
def diff():
    data = a.gethard_ware()
    return data

@app.get("/update_status_hw")
def update_status_hw(id,status,value):
    data = a.updatehard_ware(id,status,value)
    return data

@app.get("/add_hw")
def add_hw(name,hw_name):
    data = a.inserthard_ware(name,hw_name)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
