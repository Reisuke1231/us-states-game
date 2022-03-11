import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f'{len(guessed_states)}/50 Guess the States',
        prompt='What\'s another state\'s name?'
    ).title()

    if answer_state in data.state.to_list():
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        state_data = data[data['state'] == answer_state]

        label.goto(int(state_data.x), int(state_data.y))
        label.write(state_data.state.item())

        guessed_states.append(answer_state)

screen.exitonclick()