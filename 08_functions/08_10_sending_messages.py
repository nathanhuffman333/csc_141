# This code shows text messages and moves the messages from one list to another individually.

import os
os.system('cls')

def show_messages(joke):
    for message in joke:
        print(message)

def send_messages(joke):
    for x in joke:
        print(x)
        sent_messages.append(x)

sent_messages = []
joke = ["Knock knock.", "Who's there?", "Kenya", "Kenya who?", "Kenya lend me some money?"]

send_messages(joke)
print(f"\nFirst list:{joke}")
print(f"Second list: {sent_messages}")
