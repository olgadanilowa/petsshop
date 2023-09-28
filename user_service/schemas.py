class UserSchemas:
    create_user = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "date_birth": {"type": "string"},
            "customer_type": {
                "type": "string",
                "enum": ["private", "company"]
            }
        },
        "required": ["name", "email", "customer_type"],
        "additionalProperties": False
    }
