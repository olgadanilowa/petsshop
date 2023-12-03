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
    create_basket = {
        "type": "object",
        "properties": {
            "user_id": {"type": "string"},
            "product_id": {"type": "string"},
            "quantity": {"type": "integer"}

        },
        "required": ["user_id","product_id" "quantity"],
        "additionalProperties": False
    }
