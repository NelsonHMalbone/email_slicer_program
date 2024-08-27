# BroCode
# Email Slicer Program
# youtube link: https://youtu.be/4wGuB3oAKc4?si=p6WqFZXzKIxUXAEd&t=858

# accepts user input
email = input("Enter Your Email: ")

# course of project is to split the email at the '@'
index = email.index("@")
# the index will return a number

# create two new vars
username = email[:index]
domain = email[index:]

print(f'Username is {username} and Domain is {domain}')