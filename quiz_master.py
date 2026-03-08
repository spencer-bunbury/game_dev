import pgzrun

WIDTH = 800
HEIGHT = 650

questions = []

question_box = Rect(20,100,600,150)
answer_box1 = Rect(20,300,270,150)
answer_box2 = Rect(350,300,270,150)
answer_box3 = Rect(20,490,270,150)
answer_box4 = Rect(350,490,270,150)
skip_box = Rect(650,300,140,300)
time_box = Rect(650,110,150,150)

answer_boxes = [answer_box1,answer_box2,answer_box3,answer_box4]
question_count = 0
question_index = 0

is_game_over = False
time_left = 10

def draw():
    screen.fill(color= "medium aquamarine")
    screen.draw.filled_rect(question_box,"blue")
    screen.draw.filled_rect(answer_box1,"pink")
    screen.draw.filled_rect(answer_box2,"pink")
    screen.draw.filled_rect(answer_box3,"pink")
    screen.draw.filled_rect(answer_box4,"pink")
    screen.draw.filled_rect(skip_box,"orange")
    screen.draw.filled_rect(time_box,"green")
    screen.draw.textbox(question[0].strip(),question_box,color= "pink")
    

def update():
    pass
def read_question():
    global question_count,questions
    file = open("question.txt","r")
    for i in file:
        questions.append(i)
        question_count += 1
    file.close()

def read_next_question():
    global question_index
    question_index +=1
    return questions.pop(0).split(",")

read_question()
question = read_next_question()
print(question)

pgzrun.go()