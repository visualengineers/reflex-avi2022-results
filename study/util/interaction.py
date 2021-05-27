from datetime import datetime, timedelta


class Interaction:

    __posX: float
    __posY: float
    __posZ: float
    __timestamp: int
    __date_time: datetime

    __net_offset: timedelta
    __net_offset_hours: int = -2

    def __init__(self, x: float, y: float, z: float, timestamp: int, dt: str):
        self.__date_time = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ")
        self.__posX = x
        self.__posY = y
        self.__posZ = z
        self.__timestamp = timestamp
        self.__net_offset = timedelta(hours=self.__net_offset_hours)

    def x(self) -> float:
        return self.__posX

    def y(self) -> float:
        return self.__posY

    def z(self) -> float:
        return self.__posZ

    def get_timestamp(self) -> int:
        return self.__timestamp

    def get_time(self) -> datetime:
        return self.__date_time

    def get_converted_timestamp(self) -> datetime:
        start_dt = datetime(1, 1, 1)
        return start_dt + timedelta(microseconds=self.__timestamp / 10) + self.__net_offset
