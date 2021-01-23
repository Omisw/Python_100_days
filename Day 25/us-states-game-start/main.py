import pandas
from turtle import Turtle, Screen
import turtle


screen = Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
# states = data.state.to_list()
# answer = data[data.state == answer_state]
# print(answer)
# state = answer.state
# print(state)
# x_cor = answer.x.to_list()
# print(x_cor)
# y_cor = answer.y.to_list()
# print(y_cor)

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
x_cor = [139, -204, -203, 57, -297, -112, 297, 275, 220, 182, -317, -216, 95, 133, 38, -17, 149, 59, 319, 288, 312, 148, 23, 94, 49, -141, -61, -257, 302, 282, -128, 236, 239, -44, 176, -8, -278, 238, 318, 218, -44, 131, -38, -189, 282, 234, -257, 200, 83, -134]
y_cor = [-77, -170, -40, -53, 13, 20, 96, 42, -145, -75, -143, 122, 37, 39, 65, 5, 1, -114, 164, 27, 112, 101, 135, -78, 6, 150, 66, 56, 127, 65, -43, 104, -22, 158, 52, -41, 138, 72, 94, -51, 109, -34, -106, 34, 154, 12, 193, 20, 113, 90]


def write_name(x_c, y_c):
    state_name = Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(x_c, y_c)
    state_name.write(answer_state , align="left", font=("Arial", 8, "normal"))


def write_win():
    state_name = Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.color("blue")
    state_name.goto(0, 0)
    state_name.write("You win!", align="center", font=("Arial", 22, "bold"))


total_answer_states = []
complete_states = 0
while len(total_answer_states) != 50:
    answer_state = screen.textinput(title=f"Guess the state {complete_states}/50", prompt="What's another state's names?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in total_answer_states:
                missing_states.append(state)
        new_file_with_missing_states = pandas.DataFrame(missing_states)
        new_file_with_missing_states.to_csv("missing_states.csv")
        break
    if answer_state in states:
        if answer_state not in total_answer_states:
            complete_states += 1
            total_answer_states.append(answer_state)
            index_state = states.index(answer_state)
            write_name(x_cor[index_state], y_cor[index_state])
    if len(total_answer_states) == 50:
        write_win()


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()