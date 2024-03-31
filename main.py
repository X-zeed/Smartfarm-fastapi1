from fastapi import FastAPI
import json
import asyncio
app = FastAPI()

In_Humid = 0
In_Mois = 0
In_Temp = 0
Out_Humid = 0
Out_light = 0
Out_Temp = 0
Cooler = 0
Fan = 0
Fog = 0
Led = 0
Water = 0

data = {
    "In": {
        "Humidity": str(In_Humid),
        "Temperature": str(In_Temp),
        "Moisture": str(In_Mois)
    },
    "Out": {
        "Humidity": str(Out_Humid),
        "Temperature": str(Out_Temp),
        "Light": str(Out_light)
    },
    "Output": {
        "Cooler": str(Cooler),
        "Fan": str(Fan),
        "Fog": str(Fog),
        "Led": str(Led),
        "Water": str(Water)
    }
}

@app.get("/data")
async def get_data():
    return json.dumps(data)

@app.get("/In_humd/{value}")
async def update_In_Humid(value: int):
    global In_Humid
    In_Humid = value
    data["In"]["Humidity"] = str(In_Humid)
    return json.dumps(data)

@app.get("/In_temp/{value}")
async def update_In_Temp(value: int):
    global In_Temp
    In_Temp = value
    data["In"]["Temperature"] = str(In_Temp)
    return json.dumps(data)

@app.get("/In_mois/{value}")
async def update_In_Mois(value: int):
    global In_Mois
    In_Mois = value
    data["In"]["Moisture"] = str(In_Mois)
    return json.dumps(data)

@app.get("/Out_humd/{value}")
async def update_Out_Humid(value: int):
    global Out_Humid
    Out_Humid = value
    data["Out"]["Humidity"] = str(Out_Humid)
    return json.dumps(data)

@app.get("/Out_temp/{value}")
async def update_Out_Temp(value: int):
    global Out_Temp
    Out_Temp = value
    data["Out"]["Temperature"] = str(Out_Temp)
    return json.dumps(data)

@app.get("/Out_light/{value}")
async def update_Out_light(value: int):
    global Out_light
    Out_light = value
    data["Out"]["Light"] = str(Out_light)
    return json.dumps(data)

# soil
if In_Mois <= 60:
    data["Output"]["Water"] = "1"
    asyncio.sleep(3)
    data["Output"]["Water"] = "0"
else:
    data["Output"]["Water"] = "0"

# humid
if In_Humid < 60:
    data["Output"]["Fog"] = "1"
    data["Output"]["Fan"] = "0"
    asyncio.sleep(5)
    data["Output"]["Fog"] = "0"
elif In_Humid > 80:
    data["Output"]["Fan"] = "1"
else:
    data["Output"]["Fan"] = "0"

# light
if Out_light < 1100:
    data["Output"]["Led"] = "1"
else:
    data["Output"]["Led"] = "0"

# temp
if In_Temp >= 30:
    data["Output"]["Cooler"] = "1"
else:
    data["Output"]["Cooler"] = "0"
