from Entities.room_type import RoomType


class Room:
    def __init__(self, id: int, name: str, room_type: RoomType):
        self.id = id
        self.name = name
        self.room_type = room_type
