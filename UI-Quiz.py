import sys
from os import strerror
import customtkinter
import random
import configparser


Conf = configparser.ConfigParser()
Conf.read('Conf.txt')
rand = Conf.getint('Settings', 'Random-mode')
Max = Conf.getint('Settings', 'Max-Questions')
debug = Conf.getint('Settings', 'Debug')
app = customtkinter.CTk()
app.title(Conf.get('Settings', 'Appname'))
app.geometry("480x240")
app.resizable(0, 0)
rand_list = [1,2,3,4,5,6,7,8,9,10]
Q = 1
cor = 0
incc = 0

frame = customtkinter.CTkFrame(app)
frame.grid(row=1, padx=100, pady=0)


#Labels
label = customtkinter.CTkLabel(app, text="tmp",height=20, text_color="white")
label.grid(row=0, column=0, padx=0, pady=0, sticky="new")
label1 = customtkinter.CTkLabel(app, text="test", height=20, text_color="white")
label1.grid(row=0, column=0, padx=0, pady=20, sticky="new")
label2 = customtkinter.CTkLabel(frame, text="Some random text to test sum", width=200, text_color="white")
label2.grid(row=1, column=2, padx=10, pady=(10, 5), sticky="new")
label3 = customtkinter.CTkLabel(frame, text="Some random text to test sum", width=200, text_color="white")
label3.grid(row=2, column=2, padx=10, pady=5, sticky="new")
label4 = customtkinter.CTkLabel(frame, text="Some random text to test sum", width=200, text_color="white")
label4.grid(row=3, column=2, padx=10, pady=5, sticky="new")
label5 = customtkinter.CTkLabel(frame, text="Some random text to test sum", width=200, text_color="white")
label5.grid(row=4, column=2, padx=10, pady=(5, 10), sticky="new")

#Selection system
def selection():
  global debug
  label.configure(text="Question " +str(Q)+ " :")
  label2.configure(text_color="white")
  label3.configure(text_color="white")
  label4.configure(text_color="white")
  label5.configure(text_color="white")
  if rand == 1:
    if Q > Max:
      print("rand END")
      end()

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
      end()
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
      

#shows end results
def end():
  Hide_all()
  label.configure(text="End of Quiz")
  label1.configure(text="Results :", pady=40)
  label6 = customtkinter.CTkLabel(app, text=str(cor)+ "/" +str(Max), height=20, text_color="white")
  label6.grid(row=0, column=0, padx=0, pady=100, sticky="new")
  btn5 = customtkinter.CTkButton(app, text="Quit", command=quit, width=100, text_color="white")
  btn5.grid(row=0, column=0, padx=0, pady=150)
#hides main buttons and labels
def Hide_all():
  label2.grid_forget()
  label3.grid_forget()
  label4.grid_forget()
  label5.grid_forget()
  btn1.grid_forget()
  btn2.grid_forget()
  btn3.grid_forget()
  btn4.grid_forget()



#Button 1 command
def button1():
  global cor
  global incc
  global Q
  if str(corr) == '1':
      label2.configure(text_color="#35f038")
      Q = Q+1
      print("cor")
      print("button 1 pressed")
      app.after(1000, selection)
      cor = cor+1
  else:
    label2.configure(text_color="#fa1511")
    print("inc")
    Q = Q+1
    print("button 1 pressed")
    app.after(1000, selection)
    incc = incc+1

#Button 2 command
def button2():
  global cor
  global incc
  global Q
  if str(corr) == '2':
    label3.configure(text_color="#35f038")
    Q = Q+1
    print("cor")
    print("button 2 pressed")
    app.after(1000, selection)
    cor = cor+1
  else:
    label3.configure(text_color="#fa1511")
    Q = Q+1
    print("inc")
    print("button 2 pressed")
    app.after(1000, selection)
    incc = incc+1


#Button 3 command
def button3():
  global cor
  global incc
  global Q
  if str(corr) == '3':
    label4.configure(text_color="#35f038")
    Q = Q+1
    print("cor")
    print("button 3 pressed")
    app.after(1000, selection)
    cor = cor+1
  else:
    label4.configure(text_color="#fa1511")
    Q = Q+1
    print("inc")
    print("button 3 pressed")
    app.after(1000, selection)
    incc = incc+1


#Button 4 command
def button4():
  global cor
  global incc
  global Q
  if str(corr) == '4':
    label5.configure(text_color="#35f038")
    Q = Q+1
    print("cor")
    print("button 4 pressed")
    app.after(1000, selection)
    cor = cor+1
  else:
    label5.configure(text_color="#fa1511")
    Q = Q+1
    print("inc")
    print("button 4 pressed")
    app.after(1000, selection)
    incc = incc+1
    


#Buttons
btn1 = customtkinter.CTkButton(frame, text="1", command=button1, width=50, text_color="white")
btn1.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="new")

btn2 = customtkinter.CTkButton(frame, text="2", command=button2, width=50, text_color="white")
btn2.grid(row=2, column=0, padx=10, pady=5, sticky="new")

btn3 = customtkinter.CTkButton(frame, text="3", command=button3, width=50, text_color="white")
btn3.grid(row=3, column=0, padx=10, pady=5, sticky="new")

btn4 = customtkinter.CTkButton(frame, text="4", command=button4, width=50, text_color="white")
btn4.grid(row=4, column=0, padx=10, pady=(5, 10), sticky="new")

#Questions
def q1():
  global corr
  global Q
  corr = Conf.get('Q1', 'Correct-ans')
  global TmpQ
  TmpQ = 1
  label1.configure(text=Conf.get('Q1', 'Title'))
  label2.configure(text=Conf.get('Q1', 'Op1'))
  label3.configure(text=Conf.get('Q1', 'Op2'))
  label4.configure(text=Conf.get('Q1', 'Op3'))
  label5.configure(text=Conf.get('Q1', 'Op4'))

def q2():
  global corr
  global Q
  corr = Conf.get('Q2', 'Correct-ans')
  global TmpQ
  TmpQ = 2
  label1.configure(text=Conf.get('Q2', 'Title'))
  label2.configure(text=Conf.get('Q2', 'Op1'))
  label3.configure(text=Conf.get('Q2', 'Op2'))
  label4.configure(text=Conf.get('Q2', 'Op3'))
  label5.configure(text=Conf.get('Q2', 'Op4'))

def q3():
  global corr
  global Q
  corr = Conf.get('Q3', 'Correct-ans')
  global TmpQ
  TmpQ = 3
  label1.configure(text=Conf.get('Q3', 'Title'))
  label2.configure(text=Conf.get('Q3', 'Op1'))
  label3.configure(text=Conf.get('Q3', 'Op2'))
  label4.configure(text=Conf.get('Q3', 'Op3'))
  label5.configure(text=Conf.get('Q3', 'Op4'))

def q4():
  global corr
  global Q
  corr = Conf.get('Q4', 'Correct-ans')
  global TmpQ
  TmpQ = 4
  label1.configure(text=str(Conf.get('Q4', 'Title')))
  label2.configure(text=str(Conf.get('Q4', 'Op1')))
  label3.configure(text=str(Conf.get('Q4', 'Op2')))
  label4.configure(text=str(Conf.get('Q4', 'Op3')))
  label5.configure(text=str(Conf.get('Q4', 'Op4')))

def q5():
  global corr
  global Q
  corr = Conf.get('Q5', 'Correct-ans')
  global TmpQ
  TmpQ = 5
  label1.configure(text=Conf.get('Q5', 'Title'))
  label2.configure(text=Conf.get('Q5', 'Op1'))
  label3.configure(text=Conf.get('Q5', 'Op2'))
  label4.configure(text=Conf.get('Q5', 'Op3'))
  label5.configure(text=Conf.get('Q5', 'Op4'))

def q6():
  global corr
  global Q
  corr = Conf.get('Q6', 'Correct-ans')
  global TmpQ
  TmpQ = 6
  label1.configure(text=Conf.get('Q6', 'Title'))
  label2.configure(text=Conf.get('Q6', 'Op1'))
  label3.configure(text=Conf.get('Q6', 'Op2'))
  label4.configure(text=Conf.get('Q6', 'Op3'))
  label5.configure(text=Conf.get('Q6', 'Op4'))

def q7():
  global corr
  global Q
  corr = Conf.get('Q7', 'Correct-ans')
  global TmpQ
  TmpQ = 7
  label1.configure(text=Conf.get('Q7', 'Title'))
  label2.configure(text=Conf.get('Q7', 'Op1'))
  label3.configure(text=Conf.get('Q7', 'Op2'))
  label4.configure(text=Conf.get('Q7', 'Op3'))
  label5.configure(text=Conf.get('Q7', 'Op4'))

def q8():
  global corr
  global Q
  corr = Conf.get('Q8', 'Correct-ans')
  global TmpQ
  TmpQ = 8
  label1.configure(text=Conf.get('Q8', 'Title'))
  label2.configure(text=Conf.get('Q8', 'Op1'))
  label3.configure(text=Conf.get('Q8', 'Op2'))
  label4.configure(text=Conf.get('Q8', 'Op3'))
  label5.configure(text=Conf.get('Q8', 'Op4'))

def q9():
  global corr
  global Q
  corr = Conf.get('Q9', 'Correct-ans')
  global TmpQ
  TmpQ = 9
  label1.configure(text=Conf.get('Q9', 'Title'))
  label2.configure(text=Conf.get('Q9', 'Op1'))
  label3.configure(text=Conf.get('Q9', 'Op2'))
  label4.configure(text=Conf.get('Q9', 'Op3'))
  label5.configure(text=Conf.get('Q9', 'Op4'))

def q10():
  global corr
  global Q
  corr = Conf.get('Q10', 'Correct-ans')
  global TmpQ
  TmpQ = 10
  label1.configure(text=Conf.get('Q10', 'Title'))
  label2.configure(text=Conf.get('Q10', 'Op1'))
  label3.configure(text=Conf.get('Q10', 'Op2'))
  label4.configure(text=Conf.get('Q10', 'Op3'))
  label5.configure(text=Conf.get('Q10', 'Op4'))

selection()
app.mainloop()
