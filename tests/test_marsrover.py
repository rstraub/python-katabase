import pytest
from katas.marsrover import MarsRover


def test_rover_starts_with_coordinate_and_direction():
    rover = MarsRover(1, 0, "N")

    assert rover.x == 1
    assert rover.y == 0
    assert rover.direction == "N"


@pytest.mark.parametrize(
    "direction, expected_x, expected_y",
    [("N", 5, 6), ("S", 5, 4), ("W", 4, 5), ("E", 6, 5)],
)
def test_rover_can_move_forwards(direction, expected_x, expected_y):
    rover = MarsRover(5, 5, direction)
    moved = rover.move(["f"])

    assert moved == MarsRover(expected_x, expected_y, direction)


@pytest.mark.parametrize(
    "direction, expected_x, expected_y",
    [("N", 5, 4), ("S", 5, 6), ("W", 6, 5), ("E", 4, 5)],
)
def test_rover_can_move_backwards(direction, expected_x, expected_y):
    rover = MarsRover(5, 5, direction)
    moved = rover.move(["b"])

    assert moved == MarsRover(expected_x, expected_y, direction)


@pytest.mark.parametrize(
    "direction, expected_direction",
    [("N", "W"), ("S", "E"), ("W", "S"), ("E", "N")],
)
def test_rover_can_turn_left(direction, expected_direction):
    rover = MarsRover(5, 5, direction)
    moved = rover.move(["l"])

    assert moved == MarsRover(5, 5, expected_direction)


@pytest.mark.parametrize(
    "direction, expected_direction",
    [("N", "E"), ("S", "W"), ("W", "N"), ("E", "S")],
)
def test_rover_can_turn_right(direction, expected_direction):
    rover = MarsRover(5, 5, direction)
    moved = rover.move(["r"])

    assert moved == MarsRover(5, 5, expected_direction)


@pytest.mark.skip(reason="todo")
def test_rover_can_execute_multiple_commands():
    pass
