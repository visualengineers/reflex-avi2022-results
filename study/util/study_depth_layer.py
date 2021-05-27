class StudyDepthLayer:
    __depth_start: float
    __depth_end: float
    __index: int

    def __init__(self, start: float, end: float, index: int):
        self.__depth_start = start
        self.__depth_end = end
        self.__index = index

    def get_depth_pos_in_layer(self, depth: float) -> float:
        return depth - self.__depth_start / self.get_layer_depth_difference()

    def get_layer_depth_difference(self) -> float:
        return self.__depth_end - self.__depth_start

    def get_start(self) -> float:
        return self.__depth_start

    def get_end(self) -> float:
        return self.__depth_end

    def get_index(self) -> int:
        return self.__index
