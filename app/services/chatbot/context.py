def resolve_budget(current_budget, memory):
    if current_budget is not None:
        return current_budget
    
    return memory.last_budget

def is_follow_up(current_intent, memory):
    if current_intent == "best_car" and memory.last_intent in ("best_car", "compare_cars"):
        return True
    
    return False