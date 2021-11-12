# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb


#-----game configuration----
spot_color = "blue"
spot_shape = "circle"
spot_size = 2
score = 0
font_setup = ("Arial", 20, "normal")
counter_color = "white"
score_writer_color = "white"

colors = ["red", "blue", "green", "purple", "orange", "yellow", "pink"]
size = [0.5, 1, 1.5, 2, 5]
#countdown variables
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#leaderboard variables
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name: ")
#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.fillcolor(spot_color)
spot.shapesize(spot_size)

score_writer = trtl.Turtle()
score_writer.color(score_writer_color)
score_writer.pu()
score_writer.goto(200,200)

counter = trtl.Turtle()
counter.color(counter_color)
counter.pu()
counter.goto(-200,200)

#-----game functions--------
spot.penup()


  
def spot_clicked(x, y):
  global timer_up
  if (not timer_up):
    update_score()
    color_change()
    change_size()
    change_position()
  else:
    score_writer.hideturtle()
    update_score()

def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def color_change():
  new_color = rand.choice(colors)
  spot.color(new_color)

def change_size():
  new_size = rand.choice(size)
  spot.shapesize(new_size)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)


#-----events----------------
wn = trtl.Screen()
wn.bgcolor("black")
wn.ontimer(countdown, counter_interval)
spot.onclick(spot_clicked)
wn.mainloop()