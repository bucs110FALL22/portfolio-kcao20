import time


class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.id = id(time.strftime("%d%m%M%S"))
        self.arrived = time.strftime("%d/%m/%Y")
        self.adopted = None

    def setAdopted(self, date=time.strftime("%d/%m/%Y")):
        self.adopted = date

    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, ID: {self.id}, Arrival Date: {self.arrived}, Adoption Date: {self.adopted}"


def main():
    fido = Animal("fido", "cat")
    print(fido)
    fido.setAdopted()
    print(fido)


main()
