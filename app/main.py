class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    person_instances: list[Person] = []


    for person_dict in people:
        person_obj = Person(name = person_dict["name"], age = person_dict["age"])
        person_instances.append(person_obj)


    for person_dict in people:

        spouse_key = "wife" if "wife" in person_dict else "husband"
        spouse_name = person_dict.get(spouse_key)


        if spouse_name is not None:
            current_person = Person.people[person_dict["name"]]
            spouse_object = Person.people[spouse_name]


            setattr(current_person, spouse_key, spouse_object)

            inverse_key = "husband" if spouse_key == "wife" else "wife"
            setattr(spouse_object, inverse_key, current_person)


    return person_instances