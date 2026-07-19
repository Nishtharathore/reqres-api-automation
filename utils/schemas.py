
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id":         {"type": "integer"},
                "email":      {"type": "string"},
                "first_name": {"type": "string"},
                "last_name":  {"type": "string"},
                "avatar":     {"type": "string"}
            },
            "required": ["id", "email", "first_name", "last_name", "avatar"]
        }
    },
    "required": ["data"]
}

USERS_LIST_SCHEMA = {
    "type": "object",
    "properties": {
        "page":         {"type": "integer"},
        "per_page":     {"type": "integer"},
        "total":        {"type": "integer"},
        "total_pages":  {"type": "integer"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id":         {"type": "integer"},
                    "email":      {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name":  {"type": "string"},
                    "avatar":     {"type": "string"}
                },
                "required": ["id", "email", "first_name", "last_name", "avatar"]
            }
        }
    },
    "required": ["page", "per_page", "total", "total_pages", "data"]
}

CREATE_USER_SCHEMA = {
    "type": "object",
    "properties": {
        "name":      {"type": "string"},
        "job":       {"type": "string"},
        "id":        {"type": "string"},
        "createdAt": {"type": "string"}
    },
    "required": ["name", "job", "id", "createdAt"]
}

LOGIN_SCHEMA = {
    "type": "object",
    "properties": {
        "token": {"type": "string"}
    },
    "required": ["token"]
}