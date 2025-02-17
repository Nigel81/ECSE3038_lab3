from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from uuid import UUID, uuid4


app = FastAPI()

data = []

class Tank(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    location: str
    lat: str
    long: str

class Tank_Update(BaseModel):
    location: str | None = None
    lat: str | None = None
    long: str | None = None

@app.get("/tank")
async def get_all_tanks():
    return data
    
@app.post("/tank")
async def create_new_tank(tank_request: Tank):
    if tank_request.location and tank_request.lat and tank_request.long:
        data.append(tank_request)
    else:
        raise HTTPException(status_code=400, detail="Invalid Tank entry")

    tank_json = jsonable_encoder(tank_request)

    return JSONResponse(tank_json, status_code=201)

@app.get("/tank/{id}")
async def get_one_tank(id:UUID):
    for tank in data:
        if tank.id == id:
            json_tank = jsonable_encoder(tank)
            return JSONResponse(json_tank, status_code=200)
    raise HTTPException(status_code=404, detail="Tank not found")

@app.delete("/tank/{id}")
async def remove_tank(id:UUID):  
    for tank in data:
        if tank.id == id:
            data.remove(tank)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Tank not found")

@app.patch("/tank/{id}")
async def update_tank(id:UUID, tank_update: Tank_Update):
    for i, tank in enumerate(data):
        if tank.id == id:
            tank_update_dict = tank_update.model_dump(exclude_unset=True) #exclude empty field
            try:
                updated_tank = tank.copy(update = tank_update_dict)
                data[i] = Tank.model_validate(updated_tank)
                json_updated_tank = jsonable_encoder(updated_tank)
                return JSONResponse(json_updated_tank, status_code=200)
            except ValidationError:
                raise HTTPException(status_code=400, detail="Tank must have a location with both lat and long")
    raise HTTPException(status_code=404, detail="Tank not found")