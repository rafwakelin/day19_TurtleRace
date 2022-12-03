from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)

race_start = False
play_again = True

while play_again:
    all_turtles = []
    winner = ""
    user_guess = screen.textinput(title="Pick the winner", prompt="Who will win the race? Maya, Pandora, Pedro, Tina, "
                                                                  "Manfred or Margot?").lower()
    maya = Turtle(shape="turtle")
    maya.penup()
    maya.color("orange")
    maya.goto(-230, -100)
    all_turtles.append(maya)

    pandora = Turtle(shape="turtle")
    pandora.penup()
    pandora.color("gray")
    pandora.goto(-230, -50)
    all_turtles.append(pandora)

    pedro = Turtle(shape="turtle")
    pedro.penup()
    pedro.color("blue")
    pedro.goto(-230, 0)
    all_turtles.append(pedro)

    tina = Turtle(shape="turtle")
    tina.penup()
    tina.color("magenta")
    tina.goto(-230, 50)
    all_turtles.append(tina)

    manfred = Turtle(shape="turtle")
    manfred.penup()
    manfred.color("red")
    manfred.goto(-230, 100)
    all_turtles.append(manfred)

    margot = Turtle(shape="turtle")
    margot.penup()
    margot.color("green")
    margot.goto(-230, 150)
    all_turtles.append(margot)

    if user_guess:
        race_start = True
    while race_start:
        for turtle in all_turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() > 250:
                winner_colour = (turtle.pencolor())
                if winner_colour == "orange":
                    winner = "maya"
                elif winner_colour == "gray":
                    winner = "pandora"
                elif winner_colour == "blue":
                    winner = "pedro"
                elif winner_colour == "magenta":
                    winner = "tina"
                elif winner_colour == "red":
                    winner = "manfred"
                elif winner_colour == "green":
                    winner = "margot"
                race_start = False
                if winner == user_guess:
                    play_again = screen.textinput(title="Congratulations", prompt=f"{winner.title()} won the race. "
                                                                                  f"Play again? Y or N").lower()
                    if play_again == 'y':
                        screen.clearscreen()
                    else:
                        play_again = False
                else:
                    play_again = screen.textinput(title="You lost!", prompt=f"{winner.title()} won the race. "
                                                                            f"Play again? Y or N").lower()
                    if play_again == 'y':
                        screen.clearscreen()
                    else:
                        play_again = False

                print(winner)
screen.exitonclick()
