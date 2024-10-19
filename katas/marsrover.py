from dataclasses import dataclass, replace
from typing import List


@dataclass(frozen=True)
class MarsRover:
    x: int
    y: int
    direction: str

    def move(self, commands: List[str]) -> "MarsRover":
        new_y, new_x = self.move_forwards()

        return replace(self, y=new_y, x=new_x)

    def move_forwards(self):
        new_y = self.y
        new_x = self.x

        if self.direction == "N":
            new_y = self.y + 1
        elif self.direction == "S":
            new_y = self.y - 1
        elif self.direction == "W":
            new_x = self.x - 1
        elif self.direction == "E":
            new_x = self.x + 1
        else:
            raise ValueError("unknown direction!")
        return new_y, new_x
