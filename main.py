username = input("what is year user name? \n")
password = input("Input your password\n")
length = len(password)
secret = '*' * length


print(f'hey {username}! your password {secret} is {length} letters long')