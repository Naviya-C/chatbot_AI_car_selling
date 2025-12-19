from app.core.database import supabase_client

def get_cars_under_price(max_price: float):
    response = (
        supabase_client
        .table("cars")
        .select("brand, model, price, fuel_type")
        .lte("price", max_price)
        .eq("availability", True)
        .execute()
    )
    return response.data

def get_cars_by_fuel_type(fuel_type: str):
    response = (
        supabase_client
        .table("cars")
        .select("brand, model, price, fuel_type")
        .eq("fuel_type", fuel_type)
        .eq("availability", True)
        .execute()
    )
    return response.data

def get_available_cars():
    response = (
        supabase_client
        .table("cars")
        .select("brand, model, price, fuel_type")
        .eq("availability", True)
        .execute()
    )
    return response.data

