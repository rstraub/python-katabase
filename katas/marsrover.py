from dataclasses import dataclass


@dataclass(frozen=True)
class MarsRover:
    x: int
    y: int
    direction: str
