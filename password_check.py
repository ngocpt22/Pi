password = 'abc123'
def passwordcheck():
    name = input('Enter name: ')
    lastname = input('Enter last name: ')
    pwd = input('Enter password: ')
    while(pwd != password):
        print('You entered wrong password. Please try again')
        pwd = input('Enter password: ')
    message = "Hi %s %s, You are logged in!" % (name, lastname)
    print(message)

passwordcheck()