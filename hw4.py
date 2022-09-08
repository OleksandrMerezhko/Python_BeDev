users = [
    {"registered" : True, "id" : 1000001, "user_name" : "VinniPooh", "password" : "Pyatach0k", "user_lvl" : "advanced"},
    {"registered" : True, "id" : 1000002, "user_name" : "Vinni", "password" : "P00h", "user_lvl" : "beginner"},
    {"registered" : False, "id" : 1000003, "user_name" : None, "password" : None, "user_lvl" : None}
    ]
sentences = [
    {"text" : "Kyiv is a capital of Ukraine", "user_lvl" : "beginner"},
    {"text" : "Time will not slow down when something unpleasant lies ahead", "user_lvl" : "advanced"},
    {"text" : "If you want to know what a man's like, take a good look at how he treats his inferiors, not his equals", "user_lvl" : "advanced"}
    ]
user = users[0]
text_input = "inferior"
for sentence in sentences:
    if text_input in sentence["text"]:
        if user["user_lvl"] == sentence["user_lvl"] or None:
            print(sentence["text"])
        else:
            print("Ничего не найдено")