mood_list = ["happy,", "nervous", "sad", "excited", "relaxed"]

mood = input("in what mood you are in?: ")
print (mood)

if mood not in mood_list:
    print("I don't recognise that mood")
if mood in mood_list:
    if mood == "happy":
        print("It is great to see you happy!")
    if mood == "sad":
        print("It's all good, man")
    if mood == "nervous":
        print("Take a deep breath 3 times.")
    if mood == "relaxed":
        print("keep chillin'")
    if mood == "excited":
        print("Why are you excited?")


