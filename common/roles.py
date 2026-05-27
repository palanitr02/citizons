def is_admin(user):
    return user.groups.filter(name="Admin").exists()

def is_staff(user):
    return user.groups.filter(name="Staff").exists()

def is_viewer(user):
    return user.groups.filter(name="Viewer").exists()