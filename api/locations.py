from fastapi import APIRouter, status, HTTPException
from datetime import datetime

from schemas.locations import Location

locations_router = APIRouter()
locations = list()


@locations_router.get("/", status_code=status.HTTP_200_OK,response_model=list[Location])
async def get_locations():
    return locations


@locations_router.get("/{location_id}",status_code=status.HTTP_200_OK, response_model=Location)
async def get_location(location_id):
    for location in locations:
        if location.id == location_id:
            return location
    raise HTTPException(detail="Локация не найдена",
                        status_code=status.HTTP_404_NOT_FOUND)


@locations_router.post("/add", status_code=status.HTTP_201_CREATED, response_model=Location)
async def create_location(name, is_published)->Location:
    new_location = Location(id=len(locations) + 1,
                            name=name,
                            is_published=is_published,
                            created_at=datetime.now())
    locations.append(new_location)
    return new_location
