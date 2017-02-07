class Player():
    def __init__(self):
        self.health = 10.0
        self.items = []
        self.alive = True
        
    def check_state(self):
        if self.health == 0.0:
            print "You are dead."
    
    def harm(self, amount):
        self.health -= amount






class Interface():
    def __init__(self):
       self.user_input = ''
       
    def get_input(self):
        self.user_input = raw_input()
        self.user_input = self.user_input.split()
        
    def recognize(self):
        pass
        

def main():
    interface = Interface()
    interface.get_input()
    player = Player()
    while player.alive == True:
        player.check_state()
        player.harm(10.0)
    
        
main()