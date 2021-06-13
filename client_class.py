#Class for a client object, along with its properties
class Client:

    def __init__(self, name, age, talk, smoke, lang,startP, endP):
        self.name = name
        self.age = age
        self.talk = talk
        self.address = startP
        self.destination = endP
        self.smoke = smoke
        self.lang = lang