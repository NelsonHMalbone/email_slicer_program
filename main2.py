# slicing your email at the @ symbol
# but also telling you how many characters your username is

email = input("Enter your email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

lenUsername = len(username)

print(f'Username is {username} and Domain is {domain}')
print(f'Username is {lenUsername} characters')