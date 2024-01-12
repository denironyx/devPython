## Dictionary of similar objects
favourite_languages = {
    'jen': 'python',
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python',
} # leaving a comma at the end so, I am ready to add new value or pair

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")


## looping through
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
    
for name in favourite_languages.keys():
    print(name.title())
    
for value in favourite_languages.keys():
    print(value)
    
##
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")