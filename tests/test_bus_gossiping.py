from katas.bus_gossiping import exchange_gossips


def test_bus_drivers_meet():
    input = """3 1 2 3
3 2 3 1
4 2 3 4 5"""

    assert exchange_gossips(input) == "5"


def test_bus_drivers_dont_meet():
    input = """2 1 2
5 2 8"""

    assert exchange_gossips(input) == "never"
