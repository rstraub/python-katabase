def exchange_gossips(input: str) -> str:
    routes = parse_routes(input)
    return routes


def parse_routes(input: str) -> tuple[tuple[str]]:
    lines = input.split("\n")
    routes = map(lambda s: s.split(" "), lines)

    return tuple(routes)
