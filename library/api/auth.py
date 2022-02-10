#very mini auth middleware
from ..models import User

def authUser(userEmail):
    try:
        User.objects.get(email=userEmail)
    except :
        return False
    return True