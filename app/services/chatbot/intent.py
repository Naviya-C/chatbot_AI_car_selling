def detect_intent(message: str) -> str:
    text = message.lower()

    if "best" in text and "car" in text:
        return "best_car" 
    if "under" in text or "budget" in text or "price" in text:
        return "cars_under_budget"
    if "cars" in text:
        return "list_cars"
    
    return "unknown"