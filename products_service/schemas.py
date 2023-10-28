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
