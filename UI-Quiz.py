import sys
from os import strerror
import tkinter as tk
from tkinter import filedialog, Text
import random
import configparser
#!!CURRENTLY IMPLEMENTING CONF FILE!!
#!!MANT THINGS MAY NOT WORK DUE TO THIS!!


#This enitre code is extremely unoptimised and will most likley remain that way
#This is also an ongoing project so there may be new features if i do not give up
#This program isnt really easy to read to there will be some comments explaining what
#some things do

#main ui
Conf = configparser.ConfigParser()
Conf.read('Conf.txt')
debug = Conf.getint('Settings', 'Debug')
name = Conf.get('Settings', 'Appname')
rand = Conf.getint('Settings', 'Random-mode')
root = tk.Tk()
root.title(name)
sys.setrecursionlimit(3000) #If getting a error try increasing this value
frame = tk.Frame(root)
frame.place(relwidth=0.95, relheight=0.6, relx=0.025, rely=.4)

TmpQ = 0
cor = 0
corr= 3
incc = 0
Max = Conf.getint('Settings', 'Max-Questions')
Q = 1
rand_list = [1,2,3,4,5,6,7,8,9,10]
print(rand)
#Selection code
def selection():
  global debug
  if rand == 1:
    if Q > Max:
      print("rand END")
      score()

    else:
      #Random question selection 
      #Works and has been optimised 
      num = random.choice(rand_list)
      if debug == 1:
        print(rand_list) 
        print(num)
        if num == 1:
          q1()
          print("Q1")
          rand_list.remove(1)

        elif num == 2:
          q2()
          print("Q2")
          rand_list.remove(2)

        elif num == 3:
          q3()
          print("Q3")
          rand_list.remove(3)
        
        elif num == 4:
          q4()
          print("Q4")
          rand_list.remove(4)
        
        elif num == 5:
          q5()
          print("Q5")
          rand_list.remove(5)
        
        elif num == 6:
          q6()
          print("Q6")
          rand_list.remove(6)
        
        elif num == 7:
          q7()
          print("Q7")
          rand_list.remove(7)
        
        elif num == 8:
          q8()
          print("Q8")
          rand_list.remove(8)
        
        elif num == 9:
          q9()
          print("Q9")
          rand_list.remove(9)
        
        elif num == 10:
          q10()
          print("Q10")
          rand_list.remove(10)
      #Debug disabled ver of rand
      else:
        if num == 1:
          q1()
          print("Q1")
          rand_list.remove(1)

        elif num == 2:
          q2()
          print("Q2")
          rand_list.remove(2)

        elif num == 3:
          q3()
          print("Q3")
          rand_list.remove(3)
        
        elif num == 4:
          q4()
          print("Q4")
          rand_list.remove(4)
        
        elif num == 5:
          q5()
          print("Q5")
          rand_list.remove(5)
        
        elif num == 6:
          q6()
          print("Q6")
          rand_list.remove(6)
        
        elif num == 7:
          q7()
          print("Q7")
          rand_list.remove(7)
        
        elif num == 8:
          q8()
          print("Q8")
          rand_list.remove(8)
        
        elif num == 9:
          q9()
          print("Q9")
          rand_list.remove(9)
        
        elif num == 10:
          q10()
          print("Q10")
          rand_list.remove(10)





  # Sequential Question selection 
  else:
    if Q > Max:
      score()
    else:
      if str(Q) == '1':
          q1()

      elif str(Q) == '2':
          q2()

      elif str(Q) == '3':
          q3()

      elif str(Q) == '4':
          q4()

      elif str(Q) == '5':
          q5()
        
      elif str(Q) == '6':
        q6()
        
      elif str(Q) == '7':
        q7()
        
      elif str(Q) == '8':
        q8()
        
      elif str(Q) == '9':
        q9()
        
      elif str(Q) == '10':
        q10()
      


    

#answer labels
def score():
  refresh()
  print("Quiz end")
  print("You got " + str(cor))
  print("out of " + str(Q-1))
  Per = (100 / Max)
  label8 = tk.Label(root, text=("Results : "))
  canvas.create_window(240, 190, window=label8)
  label8 = tk.Label(root, text=("You got " + str(cor) + " out of " + str(Q-1)))
  canvas.create_window(240, 220, window=label8)
  label8.config(font=('Arial', 15))
  label12 = tk.Label(root, text=("Percentage : " + str(cor * Per) + "%"))
  canvas.create_window(240, 250, window=label12)
  button = tk.Button(text='Exit', command=quit)
  canvas.create_window(240, 290, window=button)

def ans():
  label8 = tk.Label(root, text=('Correct'))
  canvas.create_window(240, 220, window=label8)
  label8.config(font=('Arial', 15))

def inc():
  label8 = tk.Label(root, text=('Incorrect'))
  canvas.create_window(240, 220, window=label8)
  label8.config(font=('Arial', 15))

#redraws question box
def refresh():
  frame = tk.Frame(root, bg='light gray')
  frame.place(relwidth=0.95, relheight=0.6, relx=0.025, rely=.4)

# current score display code
def Show_curr():
  global TmpQ
  global debug
  refresh()
  if debug == 1:
    print("showing current results")
    Per = (100 / Max)
    label10 = tk.Label(root, text=("Results : "))
    canvas.create_window(240, 190, window=label10)
    label11 = tk.Label(root, text=("You have " + str(cor) + " out of " + str(Q-1)))
    canvas.create_window(240, 220, window=label11)
    label12 = tk.Label(root, text=("Percentage : " + str(cor * Per) + "%"))
    canvas.create_window(240, 250, window=label12)
    button = tk.Button(text='Hide Results ', command=back)
    canvas.create_window(100, 60, window=button)
  else:
    Per = (100 / Max)
    label10 = tk.Label(root, text=("Results : "))
    canvas.create_window(240, 190, window=label10)
    label11 = tk.Label(root, text=("You have " + str(cor) + " out of " + str(Q-1)))
    canvas.create_window(240, 220, window=label11)
    label12 = tk.Label(root, text=("Percentage : " + str(cor * Per) + "%"))
    canvas.create_window(240, 250, window=label12)
    button = tk.Button(text='Hide Results ', command=back)
    canvas.create_window(100, 60, window=button)
    

# return to last question
def back():
  print(TmpQ)
  print("Returning...")
  button = tk.Button(text='Show Results', command=Show_curr)
  canvas.create_window(100, 60, window=button)
  if str(TmpQ) == '1':
          q1()

  elif str(TmpQ) == '2':
          q2()

  elif str(TmpQ) == '3':
          q3()

  elif str(TmpQ) == '4':
          q4()

  elif str(TmpQ) == '5':
          q5()
        
  elif str(TmpQ) == '6':
        q6()
        
  elif str(TmpQ) == '7':
        q7()
        
  elif str(TmpQ) == '8':
        q8()
        
  elif str(TmpQ) == '9':
        q9()
        
  elif str(TmpQ) == '10':
        q10()
  else:
    print("Unable to return")
    print("Ending Program")
    quit()
  

#Button 1 command
def button1():
  global cor
  global incc
  global Q
  if str(corr) == '1':
      ans()
      Q = Q+1
      print("cor")
      print("button 1 pressed")
      root.after(1000, selection)
      cor = cor+1
  else:
    inc()
    print("inc")
    Q = Q+1
    print("button 1 pressed")
    root.after(1000, selection)
    incc = incc+1

#Button 2 command
def button2():
  global cor
  global incc
  global Q
  if str(corr) == '2':
    ans()
    Q = Q+1
    print("cor")
    print("button 2 pressed")
    root.after(1000, selection)
    cor = cor+1
  else:
    inc()
    Q = Q+1
    print("inc")
    print("button 2 pressed")
    root.after(1000, selection)
    incc = incc+1


#Button 3 command
def button3():
  global cor
  global incc
  global Q
  if str(corr) == '3':
    ans()
    Q = Q+1
    print("cor")
    print("button 3 pressed")
    root.after(1000, selection)
    cor = cor+1
  else:
    inc()
    Q = Q+1
    print("inc")
    print("button 3 pressed")
    root.after(1000, selection)
    incc = incc+1


#Button 4 command
def button4():
  global cor
  global incc
  global Q
  if str(corr) == '4':
    ans()
    Q = Q+1
    print("cor")
    print("button 4 pressed")
    root.after(1000, selection)
    cor = cor+1
  else:
    inc()
    Q = Q+1
    print("inc")
    print("button 4 pressed")
    root.after(1000, selection)
    incc = incc+1
    

#Window settings
canvas = tk.Canvas(root, height=320, width=480, bg='#474747')
canvas.pack()

#Options label
label1 = tk.Label(root, text=('Options :'))
canvas.create_window(240, 20, window=label1)
label1.config(font=('Arial', 12))

#buttons
button = tk.Button(text='1', command=button1)
canvas.create_window(200, 60, window=button)

button = tk.Button(text='2', command=button2)
canvas.create_window(230, 60, window=button)

button = tk.Button(text='3', command=button3)
canvas.create_window(260, 60, window=button)

button = tk.Button(text='Show Results', command=Show_curr)
canvas.create_window(100, 60, window=button)

button = tk.Button(text='4', command=button4)
canvas.create_window(290, 60, window=button)


#Question Sets
def q1():
  global corr
  global Q
  corr = Conf.get('Q1', 'Correct-ans')
  global TmpQ
  TmpQ = 1
  refresh()
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q1', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q1', 'Options')))
  canvas.create_window(240, 180, window=label4)
  label4.config(font=('Arial', 9))

def q2():
  global corr
  global Q
  corr = Conf.get('Q2', 'Correct-ans')
  global TmpQ
  TmpQ = 2
  refresh()
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q2', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q2', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q3():
  global corr
  global Q
  global TmpQ
  TmpQ = 3
  refresh()
  corr = Conf.get('Q3', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q3', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q3', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q4():
  global corr
  global Q
  global TmpQ
  TmpQ = 4
  refresh()
  corr = Conf.get('Q4', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q4', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q4', 'Options')))
  canvas.create_window(240, 180, window=label4)


def q5():
  global corr
  global Q
  global TmpQ
  TmpQ = 5
  refresh()
  corr = Conf.get('Q5', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q5', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q5', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q6():
  global corr
  global Q
  global TmpQ
  TmpQ = 6
  refresh()
  corr = Conf.get('Q6', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q6', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q6', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q7():
  global corr
  global Q
  global TmpQ
  TmpQ = 7
  refresh()
  corr = Conf.get('Q7', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q7', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q7', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q8():
  global corr
  global Q
  global TmpQ
  TmpQ = 8
  refresh()
  corr = Conf.get('Q8', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q8', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q8', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q9():
  global corr
  global Q
  global TmpQ
  TmpQ = 9
  refresh()
  corr = Conf.get('Q9', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q9', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q9', 'Options')))
  canvas.create_window(240, 180, window=label4)

def q10():
  global corr
  global Q
  global TmpQ
  TmpQ = 10
  refresh()
  corr = Conf.get('Q10', 'Correct-ans')
  label2 = tk.Label(root, text=('Question ' +str(Q)+ ' :' ))
  canvas.create_window(240, 140, window=label2)
  label3 = tk.Label(root, text=(Conf.get('Q10', 'Title')))
  canvas.create_window(240, 160, window=label3)
  label4 = tk.Label(root, text=(Conf.get('Q10', 'Options')))
  canvas.create_window(240, 180, window=label4)


selection()

root.mainloop()
