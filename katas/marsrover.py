from dataclasses import dataclass, replace
from typing import List


@dataclass(frozen=True)
class MarsRover:
    x: int
    y: int
    direction: str

    def move(self, commands: List[str]) -> "MarsRover":
        new_coordinates = self.move_forwards()

        return replace(self, y=new_coordinates.y, x=new_coordinates.x)

    def move_forwards(self) -> "Coordinate":
        if self.direction == "N":
            return Coordinate(self.x, self.y + 1)
        elif self.direction == "S":
            return Coordinate(self.x, self.y - 1)
        elif self.direction == "W":
            return Coordinate(self.x - 1, self.y)
        elif self.direction == "E":
            return Coordinate(self.x + 1, self.y)
        else:
            raise ValueError("unknown direction!")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
