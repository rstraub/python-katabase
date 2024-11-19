def exchange_gossips(input: str) -> str:
    routes = parse_routes(input)
    return routes


def parse_routes(input: str) -> tuple[tuple[str]]:
    lines = input.split("\n")

    result = []
    for line in lines:
        driver_stops = []
        stops = line.split(" ")

        for stop in stops:
            driver_stops.append(int(stop))

        result.append(tuple(driver_stops))

    return tuple(result)
