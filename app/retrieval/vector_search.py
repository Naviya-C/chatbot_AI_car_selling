import json
from sqlalchemy import text
from app.database.azure_database import get_engine

engine = get_engine()


def vector_search(
    query_embedding,
    top_k=10,
    min_price=None,
    max_price=None,
    sort=None,
    transmission=None,
    fuel_type=None,
    condition=None,
    max_mileage=None,
    brand = None
):

    vector_json = json.dumps(query_embedding)

    sql_query = """
        SELECT TOP (:limit)
            c.id,
            c.brand,
            c.model,
            c.year_of_manufacture,
            c.price,
            c.condition,
            c.mileage,
            c.transmission,
            c.fuel_type,
            cv.chunk_text,
            VECTOR_DISTANCE(
                'cosine',
                cv.embedding,
                CAST(CAST(:vec AS NVARCHAR(MAX)) AS VECTOR(384))
            ) AS vector_score
        FROM CarVectors cv
        JOIN Car c ON c.id = cv.car_id
        WHERE 1=1
    """

    params = {
        "limit": top_k,
        "vec": vector_json
    }

    # price filters
    if max_price is not None:
        sql_query += " AND c.price <= :max_price "
        params["max_price"] = max_price

    if min_price is not None:
        sql_query += " AND c.price >= :min_price "
        params["min_price"] = min_price

    # transmission filter
    if transmission:
        sql_query += " AND LOWER(c.transmission) = LOWER(:transmission) "
        params["transmission"] = transmission

    # fuel filter
    if fuel_type:
        sql_query += " AND LOWER(c.fuel_type) LIKE LOWER(:fuel_type) "
        params["fuel_type"] = f"%{fuel_type}%"
        print("SQL:", sql_query)
        print("PARAMS:", params)

    # condition filter
    if condition:
        sql_query += " AND LOWER(c.condition) = LOWER(:condition) "
        params["condition"] = condition

    # mileage filter
    if max_mileage is not None:
        sql_query += " AND c.mileage <= :max_mileage "
        params["max_mileage"] = max_mileage

    # sorting logic
    if sort == "price_asc":
        sql_query += " ORDER BY c.price ASC " 

    elif sort == "price_desc":
        sql_query += " ORDER BY c.price DESC "

    else:
        sql_query += " ORDER BY vector_score ASC "

    sql = text(sql_query)
    
    # brand filter
    if brand:
        sql_query += " AND LOWER(c.brand) = LOWER(:brand) "
        params["brand"] = brand

    with engine.connect() as conn:
        result = conn.execute(sql, params)
        return [dict(row) for row in result.mappings()]
    