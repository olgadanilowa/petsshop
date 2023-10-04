class UserSchemas:
    create_user = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string",
                      "minLength": 1,
                      "maxLength": 10},
            "date_birth": {"type": "string",
                           "minLength": 1,
                           "maxLength": 55},
            "customer_type": {
                "type": "string",
                "enum": ["private", "company"]
            }
        },
        "required": ["name", "email", "customer_type"],
        "additionalProperties": False
    }
