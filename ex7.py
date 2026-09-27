'''
    Ex7 - our_pets = [{"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
                      {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]}]

    1 - Write a function that receives the array shown above and prints only
    animalType: cat.
    2 - Write a function that receives the array shown above and the animal type.
    The function should print all names of that animal type if this type exists in the
    object.
    3 - Write a function that that receives the array shown above and animal name
    The function should add the specified animal name to each ‘names’ array in
    each animal_type if that name does not exist in the ‘names’ array.
'''


def print_cats(pets: list[dict]) -> None:
    for pet in pets:
        if pet.get("animal_type") == "cat":
            print(f"animalType: {pet['animal_type']}")


def print_animal_names_by_type(pets: list[dict], animal_type: str) -> None:
    for pet in pets:
        if pet.get("animal_type") == animal_type:
            print(f"{animal_type} names: {', '.join(pet['names'])}")


def add_animal_name(pets: list[dict], animal_name: str) -> None:
    for pet in pets:
        if animal_name not in pet.setdefault('names', []):
            pet['names'].append(animal_name)


if __name__ == "__main__":
    our_pets = [{"animal_type": "cat", "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
                {"animal_type": "dog", "names": ["Spot", "Bowser", "Frankie"]},
                {"animal_type": "bird"}]
    
    print_cats(our_pets)
    print_animal_names_by_type(our_pets, "dog")
    add_animal_name(our_pets, "Musia")

    print("\nAfter adding Musia:")
    print_animal_names_by_type(our_pets, "cat")
    print_animal_names_by_type(our_pets, "dog")
    print_animal_names_by_type(our_pets, "bird")
