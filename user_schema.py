# EXERCICI 3

# Suprimim els camps password i email, per privacitat i no donar dades personals.
def user_schema(user) -> dict:
    return {
        "name": user[0],
        "surname": user[1],
        "addres": user[2],
        "CP": user[3],
        "desciption": user[4],
        "age": user[5]
    }

def users_schema(users) -> dict:
    return [user_schema(user) for user in users]