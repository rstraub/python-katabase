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
    _BACKWARDS = "b"
    _LEFT = "l"
    _RIGHT = "r"

    def move(self, commands: List[str]) -> "MarsRover":
        first_command = commands[0]

        new_coordinates = Coordinate(self.x, self.y)
        new_direction = self.direction

        if first_command == self._FORWARDS:
            new_coordinates = self.move_forwards()
        elif first_command == self._BACKWARDS:
            new_coordinates = self.move_backwards()
        elif first_command == self._LEFT:
            new_direction = self.turn_left()
        elif first_command == self._RIGHT:
            new_direction = self.turn_right()

        return replace(
            self, y=new_coordinates.y, x=new_coordinates.x, direction=new_direction
        )

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

    def turn_left(self) -> str:
        if self.direction == self._NORTH:
            return self._WEST
        elif self.direction == self._SOUTH:
            return self._EAST
        elif self.direction == self._WEST:
            return self._SOUTH
        elif self.direction == self._EAST:
            return self._NORTH
        else:
            raise ValueError("unknown direction!")

    def turn_right(self) -> str:
        if self.direction == self._NORTH:
            return self._EAST
        elif self.direction == self._SOUTH:
            return self._WEST
        elif self.direction == self._WEST:
            return self._NORTH
        elif self.direction == self._EAST:
            return self._SOUTH
        else:
            raise ValueError("unknown direction!")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
