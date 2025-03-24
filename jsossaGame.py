class Player:
    def __init__(self,gender,health,name,defaultWeapon,credits):
        self.gender=gender
        self.health=health
        self.name=name
        self.weapon=defaultWeapon
        self.credits=credits
        print("Player Object Created",self.gender,self.health)

    def playerHurt(self,damage):
        self.health=self.health-damage
        print("Damage=",damage,"New Health=",self.health)

    def playerDead(self):
        if self.health >= 0:
            print("You have Died")
            return True
        else:
            return False

p1=Player("F",110)
p2=Player("M",100)
p1.playerHurt(20)
p2.playerHurt(10.5)
