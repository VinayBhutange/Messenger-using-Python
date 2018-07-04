import fbchat
from fbchat import Client
from fbchat.models import *
from getpass import getpass
# You can also use getpass module to take input the password without echoing
client = Client('username/email-id','password')

no_of_friends = int(input("Number of friends: "))
for i in range(no_of_friends):
    name = str(input("Name:"))
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    msg = str(input("Message: "))
    sent = client.send(fbchat.models.Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")

	
client.logout()
