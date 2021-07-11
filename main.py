import turtle

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

answer_state = screen.textinput(title="Guess the State", prompt="What's another states name?")
print(answer_state)



# screen.exitonclick()