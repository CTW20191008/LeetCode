######################################################################
# https://leetcode.cn/problems/design-parking-system/
######################################################################


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._big = big
        self._medium = medium
        self._small = small

        self._big_left = self._big
        self._medium_left = self._medium
        self._small_left = self._small

        self._left_map = {
            1: self._big_left,
            2: self._medium_left,
            3: self._small_left
        }

    def addCar(self, carType: int) -> bool:
        if self._left_map[carType] > 0:
            self._left_map[carType] -= 1
            return True

        return False 


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)