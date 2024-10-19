from katas.marsrover import MarsRover


def test_rover_starts_with_coordinate_and_direction():
    rover = MarsRover(1, 0, "N")

    assert rover.x == 1
    assert rover.y == 0
    assert rover.direction == "N"


def test_rover_can_move_forwards():
    pass


def test_rover_can_move_backwards():
    pass
