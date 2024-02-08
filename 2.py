from ProGPT import Conversation

conversation = Conversation(session_token)  # See above on how to get session_token

print(conversation.send("hello"))
print(conversation.send("how's your day going?"))
print(conversation.send("i want to ask something..."))