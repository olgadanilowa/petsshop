class UserSchemas:
    create_user = {
        "type":"object",
        "properties": {
            "name":{"type":"string"},
            "email":{"type":"string"},
            "date_birth":{"type":"string"}
        },
        "required":["name","email"],
        "additionalProperties":False
    }
