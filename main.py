import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states =  data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f'{len(guessed_states)}/50 Guess the States',
        prompt='What\'s another state\'s name?\nWhen you quit type \'Exit\''
    ).title()

    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()
        state_data = data[data['state'] == answer_state]
        label.goto(int(state_data.x), int(state_data.y))
        label.write(state_data.state.item())