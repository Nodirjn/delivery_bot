from aiogram.types import Message
from geopy.distance import geodesic

from router import router

from coordinates import BRANCHES


@router.message(lambda message: message.content_type == "location")
async def send_nearest_branch_location(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    nearest_branch_distance = None  # ((..., ...), 7.5)

    if not nearest_branch_distance:
        nearest_branch_distance = (BRANCHES[0], geodesic(BRANCHES[0], (latitude, longitude)).km)

    for index, branch in enumerate(BRANCHES[1:]):
        if geodesic(branch, (latitude, longitude)) < geodesic(BRANCHES[index], (latitude, longitude)):
            nearest_branch_distance = (branch, geodesic(branch, (latitude, longitude)).km)

    if round(nearest_branch_distance[-1], 2) >= 1.0:
        distance = f"{round(nearest_branch_distance[-1], 2)} km"
    else:
        distance = f"{round(nearest_branch_distance[-1], 2) * 1000} m"

    await message.answer(text=f"Sizga eng yaqin bo'lan filialimiz 👇, masofa: {distance}")
    await message.answer_location(latitude=nearest_branch_distance[0][0],
                                  longitude=nearest_branch_distance[0][1])

    
