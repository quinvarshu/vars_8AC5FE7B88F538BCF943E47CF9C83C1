class player:
    def play(self):
        print("The player is playing cricket.")

# Define the Batsman class, deriverd from player 

class Batsman(player):
   def play(self):

       print("the batsman is batting.")

# Define the Bowler class, derived from player

class Bower(player):

     def play(self):
         
         print("The bowler is bowling.")

# create objects of Batsman and Bowler classes 

batsman = Batsman()

batsman = Batsman()

# call the play() method for each object

batsman.play()

batsman.play()
