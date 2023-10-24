class GoodsSchemas:
    create_product = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "price": {"type": "string"},
            "quantity": {"type": "string"},
            "description": {"type": "string"}
        },
        "required": ["name", "price", "quantity", "description"],
        "additionalProperties": False
    }
