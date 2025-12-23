from app.core.database import supabase_client

def get_cars_under_price(max_price: float):
    response = (
        supabase_client.table("Car")
        .select("brand, model, price, year")
        .lte("price", max_price)
        .execute()
    )
    return response.data

def get_available_cars():
    response = (
        supabase_client.table("Car")
        .select("*")
        .execute()
    )
    return response.data
