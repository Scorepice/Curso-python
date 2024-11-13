animal = "   chanCHito feliz  "
print(animal.upper()) # CHANCHITO FELIZ
print(animal.lower()) # chanchito feliz
print(animal.capitalize()) # Chanchito feliz
print(animal.title()) # Chanchito Feliz
print(animal.strip()) # elimina los espacios en blanco
print(animal.strip().capitalize()) # Chanchito feliz
print(animal.find("feliz")) # 10
print(animal.replace("feliz", "triste")) # Chanchito triste
print("nCH" in animal) # True
print("nCH" not in animal) # False