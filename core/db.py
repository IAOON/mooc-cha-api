TORTOISE_ORM = {
    "connections": {
        "default": "postgres://mooc_cha_user:@localhost/mooc_cha",
    },
    "apps": {
        "rating": {
            "models": ["rating.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

