import fbchat
from fbchat import Client
from fbchat.models import *
from getpass import getpass
from easygui import passwordbox
import easygui
username = easygui.enterbox("Enter Username/Email-Id:")
#username = str(input("Username: "))
password = passwordbox("Password: ")
client = fbchat.Client(username,password)

no_of_friends = easygui.integerbox("Enter No. of friends")
for i in range(no_of_friends):
    name = easygui.enterbox("Name of friends")
    friends = client.searchForUsers(name)  # return a list of names
    friend = friends[0]
    msg = easygui.enterbox("Message")
    sent = client.send(fbchat.models.Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
    if sent:
        easygui.msgbox("Message sent successfully!")

client.logout()
