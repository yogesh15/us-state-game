import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#Get mouse click coordinates in Python turtle

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# #keep open screen
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 States Correct", prompt="What's another states name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        #https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html
        #t.write(state_data.state.item())
        t.write(answer_state)


screen.exitonclick()