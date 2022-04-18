def main():
    nameOfemail = {}
    email = input("Email: ")
    while email != "":
        name = getEmailname(email)
        check = input("Is your name {}? (Y/n) ".format(name))
        if check.upper() != "Y" and check != "":
            name = input("Name: ")
        nameOfemail[email] = name
        email = input("Email: ")

    for email, name in nameOfemail.items():
        print("{} ({})".format(name, email))


def getEmailname(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


if __name__ == '__main__':
    main()