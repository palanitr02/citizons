def user_role(user):

    if user.groups.filter(name="Admin").exists():
        return "admin"

    if user.groups.filter(name="Staff").exists():
        return "staff"

    return "viewer"