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

def process_message(message: str) -> str:
    intent = detect_intent(message)

    if intent == "cars_under_budget":
        budget = extract_budget(message)
        if budget is None:
            return "Could you please specify your budget?"
        
        cars = fetch_cars_under_price(budget)
        if "message" in cars:
            return no_results_response()
        
        best_cars = get_best_cars_under_budget(budget)
        return best_cars_response(best_cars)

    elif intent == "best_car":
        budget = extract_budget(message)
        if budget is None:
            return "Could you please specify your budget for the best car?"
        
        best_cars = get_best_cars_under_budget(budget)
        if not best_cars:
            return no_results_response()
        
        return best_cars_response(best_cars)

    elif intent == "list_cars":
        cars = list_all_cars()
        if not cars:
            return no_results_response()
        
        return cars_list_response(cars)

    else:
        return fallback_response()