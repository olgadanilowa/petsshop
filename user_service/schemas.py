class UserSchemas:
    create_user = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
            "date_birth": {"type": "string",
                           "minLength": 8,
                           "maxLength": 10},
            "customer_type": {
                "type": "string",
                "enum": ["private", "company"]
            },
            "password":{"type":"string"}
        },
        "required": ["name", "email", "customer_type", "password"],
        "additionalProperties": False
    }
