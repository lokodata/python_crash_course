def show_messages(messages):
    for message in messages:
        print(message)


messages = ['hello', 'hi', 'how are you?']
show_messages(messages)

print()

sent_messages = []


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    print(f'messages in function: {messages}')


def show_messages(list, list1):
    print(f'messages: {list}')
    print(f'send messages: {list1}')


send_messages(messages[:], sent_messages)
show_messages(messages, sent_messages)
