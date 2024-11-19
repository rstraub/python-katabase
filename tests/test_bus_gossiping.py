from katas.bus_gossiping import create_bus_drivers, exchange_gossips, parse_routes


def test_bus_drivers_meet():
    input = """3 1 2 3
3 2 3 1
4 2 3 4 5"""

    assert exchange_gossips(input) == "5"


def test_bus_drivers_dont_meet():
    input = """2 1 2
5 2 8"""

    assert exchange_gossips(input) == "never"


def test_parse_routes():
    input = """3 1 2 3
3 2 3 1
4 2 3 4 5"""

    expected = ((3, 1, 2, 3), (3, 2, 3, 1), (4, 2, 3, 4, 5))

    assert parse_routes(input) == expected


def test_create_bus_drivers():
    routes = ((1, 2), (3, 2))

    expected = (
        {"gossips": ["gossip 1"], "route": (1, 2)},
        {"gossips": ["gossip 2"], "route": (3, 2)},
    )

    assert create_bus_drivers(routes) == expected