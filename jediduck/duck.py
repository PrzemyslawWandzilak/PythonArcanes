#Jedi Duck in Action

class Duck():
    def __init__(self, name="Duck"):
        self.name = name
    
    def quack(self):
        print "Quack!"

class JediDuck(Duck):
    def force(self):
        print "Light Whaaam"
    def jedi_modulus(self, inlist):
        return filter(lambda x: x % 108 == 0, inlist)

class DarkDuck(JediDuck):
    def force(self):
        print "Evil Whaaam"
    def cheat(self):
        print "Hahaha"
        
class Actor():
    def __init__(self, name="Harrison"):
        self.name = name
    def quack(self):
        print "Acting Quack!"