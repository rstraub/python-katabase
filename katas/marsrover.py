from dataclasses import dataclass, replace
from enum import Enum, auto
from typing import List


@dataclass(frozen=True)
class MarsRover:
    x: int
    y: int
    direction: str

    _NORTH = "N"
    _SOUTH = "S"
    _EAST = "E"
    _WEST = "W"

    _FORWARDS = "f"

    def move(self, commands: List[str]) -> "MarsRover":
        first_command = commands[0]

        if first_command == self._FORWARDS:
            new_coordinates = self.move_forwards()
        else:
            new_coordinates = self.move_backwards()

        return replace(self, y=new_coordinates.y, x=new_coordinates.x)

    def move_forwards(self) -> "Coordinate":
        if self.direction == self._NORTH:
            return Coordinate(self.x, self.y + 1)
        elif self.direction == self._SOUTH:
            return Coordinate(self.x, self.y - 1)
        elif self.direction == self._WEST:
            return Coordinate(self.x - 1, self.y)
        elif self.direction == self._EAST:
            return Coordinate(self.x + 1, self.y)
        else:
            raise ValueError("unknown direction!")

    def move_backwards(self) -> "Coordinate":
        if self.direction == self._NORTH:
            return Coordinate(self.x, self.y - 1)
        elif self.direction == self._SOUTH:
            return Coordinate(self.x, self.y + 1)
        elif self.direction == self._WEST:
            return Coordinate(self.x + 1, self.y)
        elif self.direction == self._EAST:
            return Coordinate(self.x - 1, self.y)
        else:
            raise ValueError("unknown direction!")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
