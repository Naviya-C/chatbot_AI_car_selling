from ..core.database import supabase_client

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