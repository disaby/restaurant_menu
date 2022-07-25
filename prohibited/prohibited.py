import json

proh = []

print("making prohibited words list...\n")

with open("prohibitet.txt", "r", encoding="utf-8") as file:
    for i in file:
        word = i.lower().split('\n')[0]
        if word != '':
            proh.append(word)

with open("prohibited.json", "w", encoding="utf-8") as file:
    json.dump(proh, file)

print("Completed!\n")
