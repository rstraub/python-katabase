from katas.bus_gossiping import create_bus_drivers, exchange_gossips, parse_routes, stop


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
        {"gossips": {"gossip 1"}, "route": (1, 2), "currentStop": 1},
        {"gossips": {"gossip 2"}, "route": (3, 2), "currentStop": 3},
    )

    assert create_bus_drivers(routes) == expected


def test_stop_exchanges_gossip_when_drivers_are_at_same_stop():
    drivers = (
        {"gossips": {"gossip 1"}, "route": (1, 3), "currentStop": 1},
        {"gossips": {"gossip 2"}, "route": (1, 2), "currentStop": 1},
    )

    expected = (
        {"gossips": {"gossip 2", "gossip 1"}, "route": (1, 3), "currentStop": 1},
        {"gossips": {"gossip 2", "gossip 1"}, "route": (1, 2), "currentStop": 1},
    )

    assert stop(drivers, 0) == expected


def test_stop_should_not_exchange_gossip_when_drivers_are_at_different_stops():
    pass
