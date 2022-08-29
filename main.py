import random

ask_joke = "tell me a joke"

chat_dict = {
    "hello" : "hi, how are you?",
    "im good" : "great to hear",
    "how are you" : "im a computer, i feel nothing",
    ask_joke : {
        1 : "what do you call a duck that's pretending to be a doctor? a quack!",
        2 : "what kind of tree can fit in one hand? a PALM tree!",
        3 : "why do bees have sticky hair? they use honeyCOMBS!"
    }
}

def random_joke():
    joke_dict = chat_dict.get(ask_joke)
    return random.choice(list(joke_dict.values()))

def chat():
    init = input("talk to me, human! >")
    while init:
        if init == "goodbye":
            break
        elif init in chat_dict:
            if init == ask_joke:
                print(random_joke())
                return chat()
            else:
                response = chat_dict.get(init)
                print(response)
                return chat()
                
        else:
            print("Sorry, I don't know what that means. Try again?")
            return chat()

    return ("Thanks for chatting!")

print(chat())

# lessons learned: while loops, dicts and dict-manipulation, conditional statements, functions, casting (with lists)