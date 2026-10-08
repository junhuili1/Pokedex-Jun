import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def all_names():
    i=0
    while i<809:
        print(data[i]["name"])
        i+=1
# Add a language choice feature and print the pokemons name based on the user input
def allNamesLanguage(language):
    i=0
    while i<809:
        print(data[i]['name'][language])
        i+=1
language = input("What language would you like to use?").lower()
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
def allNamesLanguageType(language,type):
    found = False
    for i in range(len(data)):
        if type in data[i]["type"]:
            print(data[i]["name"][language])
            found = True
    if found == False:
        print(f"No pokemon was found with the type: {type}")

# Type = input("What type of pokemon would you like to find?").capitalize()
# allNamesLanguageType(language, Type)
#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
def named(language,name):
    found = False
    for i in range(len(data)):
        if name in data[i]["name"][language]:
            print(data[i]["name"][language])
            found = True
    if found == False:
        print(f"No pokemon was found with the name: {name}")

name = input("What is the name of the pokemon you would like to find?").capitalize()
named(language,name)
#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

