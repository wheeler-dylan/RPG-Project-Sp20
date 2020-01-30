class Adventurer():
    def __init__(self, name, fate, hitpoints, onTheMind):
        self.name = name
        self.fate = fate
        self.hitpoints = hitpoints
        self.onTheMind = onTheMind
    
    def think(self):
        self.onTheMind = input("Enter what you wish to say.")
    
    def speak(self):
        print(self.onTheMind)
    
    def introduce(self):
        print("Hello, I am " + self.name + ", and I am a " + self.fate + ".")