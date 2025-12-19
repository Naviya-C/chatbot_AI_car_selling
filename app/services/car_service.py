from app.repositories.car_repo import get_cars_under_price, get_cars_by_fuel_type, get_available_cars

def fetch_cars_under_price(max_price: float):
    cars = get_cars_under_price(max_price)
    
    if not cars:
        return {"message": "No cars available under the specified price."}
    
    return cars


def get_best_cars_under_budget(max_price: float, limit: int = 3):
    cars = get_cars_under_price(max_price)
    
    if not cars:
        return []
    
    car_sorted = sorted(cars, key = lambda x: x['price'])

    return car_sorted[:limit]

def list_all_cars():
    return get_available_cars()