import time

print("Hello, this is your personal assistant.\n"
      "I can make calls for you, tell you the time, schedule meetings, and even switch the light on and off.\n")
user_name=input("Please enter your name to get started: ")
bot_name=input("What would you like to call me? : ")

while True:
    question=input("What do you want me to do ?")

    if question=="What is your name?" or question=="Who are you?":
        time.sleep(0.5)
        print(f"Hello, I am {bot_name}.")

    if question=="Who is your father?":
        time.sleep(0.5)
        print("Well technically I don’t have any father, but I do have a founder- Aditya Goyal.\n"
              "Keeping all that aside, i do work for you now.")

    if question==f"Switch on the lights {bot_name}":
        time.sleep(0.5)
        print("Switching on the lights, sir.")

    if question==f"Switch off the lights {bot_name}":
        time.sleep(0.5)
        print("Switching off the lights, sir.")

    if question==f"What is the time, {bot_name}?":
        time.sleep(0.5)
        print(time.localtime())

    if question==f"What is my name,{bot_name}":
        time.sleep(0.5)
        print(f"Sir, your name is {user_name}.")

    if question==f"Schedule a meeting for 10:00 tomorrow, {bot_name}":
        time.sleep(0.5)
        print(f"Meeting Scheduled for 10am.")

    if question=="Call Saffin Matthew.":
        time.sleep(0.5)
        print("Calling Saffin Matthew.")

    if question=="Increase the ending time of mission3 by 5mins.":
        time.sleep(0.5)
        print("Increasing mission3 time limit by 5 mins.")

    if question=="Quit":
        time.sleep(0.5)
        print("Exiting.")
        exit()