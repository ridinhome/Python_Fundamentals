'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Sport():

    def __init__(self, players,team = True):
        self.team = team
        self.players = players

    def sport_type(self):
        if self.team == True:
            return "team sport"
        else:
            return "individual sport"

class Baseball(Sport):

    def __init__(self,players,team,sport,equipment,field):
        super().__init__(players,team)
        self.sport = sport
        self.equipment = equipment
        self.field = field

    def __str__(self):
        return (f"{self.sport} is a {self.sport_type()} played on a {self.field} with {self.players} using {self.equipment} players")

class BaseballTeam(Baseball):

    def __init__(self,players,team,sport,equipment,field,conference,teamname):
        super().__init__(players,team,sport,equipment,field)
        self.conference = conference
        self.teamname = teamname

    def __str__(self):
        return (f"The {self.teamname} are a {self.sport} team with {self.players} players in the {self.conference} conference")

base_ball = Baseball(11,True,"baseball","bat","diamond")
yankees = BaseballTeam(base_ball.players,base_ball.team,base_ball.sport,base_ball.equipment,base_ball.field,"National League","Yankees")

# print (base_ball)
print (yankees)