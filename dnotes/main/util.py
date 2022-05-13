from main import models

def can_user_see_note(user, note):
    if note.link_share: return True
    return user == note.owner or user.is_superuser
