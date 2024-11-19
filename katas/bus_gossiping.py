from copy import copy
from itertools import chain, groupby
from typing import Dict, Union


def exchange_gossips(input: str) -> str:
    routes = parse_routes(input)
    drivers = create_bus_drivers(routes)
    return ""


Route = tuple[int, ...]
Routes = tuple[Route, ...]


def parse_routes(input: str) -> Routes:
    lines = input.split("\n")

    result = []
    for line in lines:
        driver_stops = []
        stops = line.split(" ")

        for stop in stops:
            driver_stops.append(int(stop))

        result.append(tuple(driver_stops))

    return tuple(result)


Driver = Dict[str, Union[set[str], Route]]
Drivers = tuple[Driver, ...]


def create_bus_drivers(routes: Routes) -> Drivers:
    result = []

    for index, route in enumerate(routes):
        gossip_number = index + 1
        initial_gossips = {f"gossip {gossip_number}"}
        initial_stop = route[0]
        result.append(
            {"gossips": initial_gossips, "route": route, "currentStop": initial_stop}
        )

    return tuple(result)


def stop(drivers: Drivers, minute: int) -> Drivers:
    # TODO copy driver and update current stop according to minute

    sorted_drivers = sorted(drivers, key=lambda d: d["currentStop"])

    grouped_by_stop = {
        key: list(group)
        for key, group in groupby(sorted_drivers, lambda d: d["currentStop"])
    }

    updated_drivers = []
    for _, drivers in grouped_by_stop.items():
        all_gossips = set(chain.from_iterable(map(lambda d: d["gossips"], drivers)))

        for driver in drivers:
            updated_driver = copy(driver)
            updated_driver["gossips"] = all_gossips
            updated_drivers.append(updated_driver)

    print(updated_drivers)

    return tuple(updated_drivers)
