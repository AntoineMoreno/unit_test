def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

def get_user_name_from_input():
    """ Not empty string. No spaces. """
    username=input("Create your user name: ")
    if(" " in username or username==""):
        print("Invalid username")
    else:
        return username

# def get_password_from_input():
#     """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
#     password=input("Create your password: ")
#     numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     alphabet
#     if (len(password)<8 or )
