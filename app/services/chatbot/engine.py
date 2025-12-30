from app.services.chatbot.intent import detect_intent
from app.services.chatbot.entities import extract_budget
from app.services.chatbot.responses import (
    cars_list_response,
    best_cars_response,
    no_results_response,
    fallback_response,
)
from app.services.car_service import (
    fetch_cars_under_price, 
    get_best_cars_under_budget, 
    list_all_cars
)
from app.services.chatbot.memory import ConversationMemory
from app.services.chatbot.context import resolve_budget

memory = ConversationMemory()

def process_message(message: str) -> str:
    intent = detect_intent(message)
    budget = extract_budget(message)

    budget = resolve_budget(budget, memory)

    if intent == "cars_under_budget":
        if budget is None:
            return "Could you please specify your budget?"

        cars = fetch_cars_under_price(budget)
        if not cars:
            return no_results_response()

        memory.update(intent=intent, budget=budget, results=cars)
        return cars_list_response(cars)

    if intent == "best_car":
        if budget is None:
            return "Could you please specify your budget for the best car?"

        best_cars = get_best_cars_under_budget(budget)
        if not best_cars:
            return no_results_response()

        memory.update(intent=intent, budget=budget, results=best_cars)
        return best_cars_response(best_cars)

    if intent == "list_cars":
        cars = list_all_cars()
        if not cars:
            return no_results_response()

        memory.update(intent=intent, results=cars)
        return cars_list_response(cars)

    return fallback_response()
