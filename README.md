**Lab 3**
**Purpose:**
        <To create a list of tank information from data gathered from different tank locations. Additionally, to allow the client to updated or search for a specific tank.>

<**async def get_all_tanks()**>
    <Return all tanks and their associated data>

<**async def create_new_tank(tank_request: Tank)**>
    <Takes the data from the based model and checks each field. If all fields are filled, the tank data is added to the data list, hence a new item is created and the client received a copy of the created information to view. However, if all the fields are not filled, the user will get a 400 status code with the accompanying message: "Invalid Tank entry".>

<**async def get_one_tank(id:UUID)**>
    <This function uses an ID to search for a specific tank in the data list using a for each loop. If a match is founded, that specific tank is returned as a json object. If no matches is founded, the client will received a error status code 404: "Tank not found".>

<**async def remove_tank(id:UUID)**>
    <This function uses an ID to search for a specific tank in the data list using a for each loop. If a match is founded, that specific tank is deleted or removed. If no matches is founded, the client will received a error status code 404: "Tank not found".>

<**async def update_tank(id:UUID, tank_update: Tank_Update)**>
    <This function uses an ID to search for a specific tank in the data list. For the for each loop, the data is enumerated to return both the index and ID. The ID is used to search the data list for the matching tank. When a match is found, the update is temporarily stored in a dictionary. A try and except block is used to updated the a specfic part of the matching tank data. If an validation error occurs while updating the tank data, the client will receive the error status code 400 with the accompanying details "Tank must have a location with both lat and long". If no matches is founded, the client will received a error status code 404: "Tank not found".>

<Guess which is the lie?>
    <1. I built a fully functional pure sinewave at the age of 19>
    <2. I can walk to speeds of 8.2 km/h for 15 km without the need for water>
    <3. My first career thought was engineering>
