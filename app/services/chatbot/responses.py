def cars_list_response(cars: list) -> str:
    lines = ["Here are the available cars:"]

    for car in cars:
        lines.append(
            f"- {car['brand']} {car['model']} (Rs. {car['price']:,})"
        )

    return "\n".join(lines)


def best_cars_response(cars: list) -> str:
    lines = ["These are the best cars for your budget:"]

    for car in cars:
        lines.append(
            f"- {car['brand']} {car['model']} (Rs. {car['price']:,})"
        )

    return "\n".join(lines)


def no_results_response() -> str:
    return (
        "Sorry, I couldn't find any cars matching your request. "
        "Please try a different budget."
    )


def fallback_response() -> str:
    return (
        "I'm not sure I understood that. "
        "You can ask about available cars, prices, or best cars under a budget."
    )
