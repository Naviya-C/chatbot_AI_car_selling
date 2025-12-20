from app.core.database import supabase_client

def get_cars_under_price(max_price: float):
    response = (
        supabase_client
        .table("Car")
        .select("brand, model, price, year")
        .lte("price", max_price)
        .execute()
    )
    return response.data

def get_cars_by_fuel_type(fuel_type: str):
    response = (
        supabase_client
        .table("Car")
        .select("brand, model, price, fuel_type")
        .eq("fuel_type", fuel_type)
        .execute()
    )
    return response.data

def get_available_cars():
    response = (
        supabase_client
        .table("Car")
        .select("*")
        .execute()
    )
    return response.data


