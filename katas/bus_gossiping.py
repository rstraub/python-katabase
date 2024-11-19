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
        result.append({"gossips": {f"gossip {gossip_number}"}, "route": route})

    return tuple(result)


def stop(drivers: Drivers, minute: int) -> Drivers:
    return drivers
