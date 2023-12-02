class GoodsSchemas:
    create_product = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "price": {"type": "integer"},
            "quantity": {"type": "integer"},
            "description": {"type": "string", "maxLength": 200}
        },
        "required": ["name", "price", "quantity", "description"],
        "additionalProperties": False
    }


class BasketSchemas:
    basket = {
         "type": "object",
        "properties": {
            "id": {"type": "string"},
            "basket_id": {"type": "string"},
            "user_id": {"type": "string"},
            "product_id": {"type": "string"},
            "quantity": {"type": "integer"},
            "sum": {"type": "integer"}

        },
        "required": ["user_id", "product_id", "quantity", "sum"],
        "additionalProperties": False
    }
