import sys
from os import strerror
import customtkinter
import tkinter as tk
import random
import configparser
from PIL import Image

Conf = configparser.ConfigParser()
Conf.read('Conf.ini')
Max = Conf.getint('Settings', 'Max-Questions')
debug = Conf.getint('Settings', 'Debug')
app = customtkinter.CTk()
app.title(Conf.get('Settings', 'Appname'))
app.geometry("480x240")
app.resizable(0, 0)

#Loads Icons
Settingsicon = customtkinter.CTkImage(light_image=Image.open("Icons/Settings-icon.png"), size=(25, 25))
Path_Upd = customtkinter.CTkImage(light_image=Image.open("Icons/Update-path.png"), size=(20, 20))
Streak0 = customtkinter.CTkImage(light_image=Image.open("Icons/Streak-lost.png"), size=(25, 25))
Streak1 = customtkinter.CTkImage(light_image=Image.open("Icons/Streak-start.png"), size=(25, 25))
Streak2 = customtkinter.CTkImage(light_image=Image.open("Icons/Streak-medium.png"), size=(25, 25))
Streak3 = customtkinter.CTkImage(light_image=Image.open("Icons/Streak-high.png"), size=(25, 25))
settings_window = None
Q = 1
cor = 0
incc = 0
Tmp = 0
Comp = 0
currstreak = 0
acccolour = str(Conf.get('Settings', 'Accent-colour'))
highlight = str(Conf.get('Settings', 'Highlight-col'))

#Accent colour updater
def accent_colour(new_col):
    global acccolour
    global highlight
    global btn5
    print("Colour has changed to " +str(new_col))
    if new_col == "Blue":
       acccolour = "#1F6AA5"
       highlight = "#164f7a"
    elif new_col == "Purple":
       acccolour = "#7a2cd4"
       highlight = "#581f99"
    elif new_col == "Red":
       acccolour = "#961a1a"
       highlight = "#7a1515"
    elif new_col == "Orange":
       acccolour = "#cf7d13"
       highlight = "#a3620d"
    elif new_col == "Green":
      acccolour = "#1b800b"
      highlight = "#146308"
    else:
      acccolour = new_col
    canvas.create_rectangle(0, 0, move, 30, fill=acccolour, width=2, outline="")
    btn1.configure(fg_color=acccolour, hover_color=highlight)
    btn2.configure(fg_color=acccolour, hover_color=highlight)
    btn3.configure(fg_color=acccolour, hover_color=highlight)
    btn4.configure(fg_color=acccolour, hover_color=highlight)
    btn_settings.configure(fg_color=acccolour, hover_color=highlight)
    update_button.configure(fg_color=acccolour, hover_color=highlight)
    accent_colour_menu.configure(fg_color=acccolour, button_color=acccolour, button_hover_color=highlight)

canvas = tk.Canvas(app, width=480, height=30, highlightthickness=0, bg="#2B2B2B")
canvas.grid(row=2, column=0, padx=0, pady=10, sticky="nw")
def Prog_Upd():
  global move
  move = permove * int(Comp+1)
  print("bottom bar width : " +str(move)+ "px")
  canvas.create_rectangle(0, 0, move, 30, fill=acccolour, width=2, outline="")


#streak system 
def streak():
   global label6
   global currstreak
   label6 = customtkinter.CTkLabel(app, text="streak: " +str(currstreak), width=30, height=20,  text_color="white" , font=("Ariel", 13,  "bold"))
   label6.grid(row=0, column=0, padx=10, pady=15, sticky="nw")
   if currstreak == 0:
      label6.configure(image=Streak0, compound="left")
   elif currstreak <= 3: 
      label6.configure(image=Streak1, compound="left")
   elif currstreak >=4 and currstreak <=6:
      label6.configure(image=Streak2, compound="left")
   elif currstreak > 6:
      label6.configure(image=Streak3, compound="left")
    

#changes the conf file path
def conf_upd():
   global Tmp
   global Max
   global debug
   conf_new = entry.get()
   print("New Config path is " +str(conf_new))
   Conf.read(conf_new)
   Max = Conf.getint('Settings', 'Max-Questions')
   debug = Conf.getint('Settings', 'Debug')
   app.title(Conf.get('Settings', 'Appname'))
   Tmp = 0
   List_load()
   app.after(100, None)
   selection()

#Creates a list to randomly choose questions
def List_load():
  global Tmp
  global Max
  global rand_list
  global Comp
  global permove
  global currstreak
  canvas.create_rectangle(0, 0, 480, 30, fill="#2B2B2B", width=2, outline="")
  Comp = 0
  currstreak = 0
  rand_list = []
  while Tmp < Max:
    Tmp = Tmp+1
    rand_list.append(Tmp)
    print("Added " +str(Tmp))
    print("Curr list " +str(rand_list))
  permove = 480 / int(Max)

#Creates frame 
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


#shows end results
def end():
  streak()
  Hide_all()
  global btn5
  label.configure(text="End of Quiz")
  label1.configure(text="Results :", pady=40)
  label6 = customtkinter.CTkLabel(app, text=str(cor)+ "/" +str(Max), height=20, text_color="white")
  label6.grid(row=0, column=0, padx=0, pady=100, sticky="new")
  btn5 = customtkinter.CTkButton(app, text="Quit", command=quit, width=100, text_color="white", fg_color=acccolour, hover_color=highlight)
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


#Settings menu popout window
def settings():
    global entry
    global settings_window

    def on_closing():
      global settings_window
      settings_window.destroy()
      settings_window = None
    
    if settings_window is None or not settings_window.winfo_exists():
        settings_window = customtkinter.CTkToplevel(app)
        settings_window.title("Settings")
        settings_window.geometry("480x240")
        settings_window.resizable(0, 0)
        settings_window.protocol("WM_DELETE_WINDOW", on_closing) 
        global update_button
        global accent_colour_menu

        label = customtkinter.CTkLabel(settings_window, text="Enter the config path", text_color="white")
        label.grid(row=0, column=0, padx=0, pady=0)
        settings_window.grid_columnconfigure(0, weight=1)

        entry = customtkinter.CTkEntry(settings_window, placeholder_text="Config Path")
        entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        update_button = customtkinter.CTkButton(settings_window, image=Path_Upd, text="Update Path", command=conf_upd, fg_color=acccolour, hover_color=highlight)
        update_button.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")

        accent_colour_menu = customtkinter.CTkOptionMenu(settings_window, values=["Blue", "Purple", "Red", "Orange", "Green"], command=accent_colour , fg_color=acccolour, button_color=acccolour, button_hover_color=highlight)
        accent_colour_menu.grid(row=3, column=0, padx=0, pady=(20, 10))
    else:
        settings_window.focus()




#Selection system
def selection():
    global Comp
    if Comp != Max:
        label2.configure(text_color="white")
        label3.configure(text_color="white")
        label4.configure(text_color="white")
        label5.configure(text_color="white")
        streak()
        Prog_Upd()
        global corr
        global TmpQ
        print("Curr comp = " +str(Comp))
        print("Current list " +str(rand_list))
        out = random.choice(rand_list)
        print(out)
        Q = "Q" +str(out)
        print(Q)
        TmpQ = Q
        corr = Conf.get(Q, 'Correct-ans')
        label.configure(text="Question " +str(Comp+1)+ ":")
        label1.configure(text=Conf.get(Q, 'Title'))
        label2.configure(text=Conf.get(Q, 'Op1'))
        label3.configure(text=Conf.get(Q, 'Op2'))
        label4.configure(text=Conf.get(Q, 'Op3'))
        label5.configure(text=Conf.get(Q, 'Op4'))
        rand_list.remove(out)
        Comp = Comp +1

    else:
        end()

#Button 1 command
def button1():
  global cor
  global incc
  global Q
  global currstreak
  if str(corr) == '1':
      label2.configure(text_color="#35f038")
      Q = Q+1
      print("cor")
      print("button 1 pressed")
      app.after(1000, selection)
      cor = cor+1
      currstreak = currstreak +1
  else:
    label2.configure(text_color="#fa1511")
    print("inc")
    Q = Q+1
    print("button 1 pressed")
    app.after(1000, selection)
    incc = incc+1
    currstreak = 0

#Button 2 command
def button2():
  global cor
  global incc
  global Q
  global currstreak
  if str(corr) == '2':
    label3.configure(text_color="#35f038")
    Q = Q+1
    print("cor")
    print("button 2 pressed")
    app.after(1000, selection)
    cor = cor+1
    currstreak = currstreak +1
  else:
    label3.configure(text_color="#fa1511")
    Q = Q+1
    print("inc")
    print("button 2 pressed")
    app.after(1000, selection)
    incc = incc+1
    currstreak = 0


#Button 3 command
def button3():
  global cor
  global incc
  global Q
  global currstreak
  if str(corr) == '3':
    label4.configure(text_color="#35f038")
    Q = Q+1
    print("cor")
    print("button 3 pressed")
    app.after(1000, selection)
    cor = cor+1
    currstreak = currstreak +1
  else:
    label4.configure(text_color="#fa1511")
    Q = Q+1
    print("inc")
    print("button 3 pressed")
    app.after(1000, selection)
    incc = incc+1
    currstreak = 0


#Button 4 command
def button4():
  global cor
  global incc
  global Q
  global currstreak
  if str(corr) == '4':
    label5.configure(text_color="#35f038")
    Q = Q+1
    print("cor")
    print("button 4 pressed")
    app.after(1000, selection)
    cor = cor+1
    currstreak = currstreak +1
  else:
    label5.configure(text_color="#fa1511")
    Q = Q+1
    print("inc")
    print("button 4 pressed")
    app.after(1000, selection)
    incc = incc+1
    currstreak = 0
    


#Buttons
btn1 = customtkinter.CTkButton(frame, text="1", command=button1, width=50, text_color="white", fg_color=acccolour, hover_color=highlight)
btn1.grid(row=1, column=0, padx=10, pady=(10, 5), sticky="new")

btn2 = customtkinter.CTkButton(frame, text="2", command=button2, width=50, text_color="white", fg_color=acccolour, hover_color=highlight)
btn2.grid(row=2, column=0, padx=10, pady=5, sticky="new")

btn3 = customtkinter.CTkButton(frame, text="3", command=button3, width=50, text_color="white", fg_color=acccolour, hover_color=highlight)
btn3.grid(row=3, column=0, padx=10, pady=5, sticky="new")

btn4 = customtkinter.CTkButton(frame, text="4", command=button4, width=50, text_color="white", fg_color=acccolour, hover_color=highlight)
btn4.grid(row=4, column=0, padx=10, pady=(5, 10), sticky="new")

btn_settings = customtkinter.CTkButton(app, image=Settingsicon, text="", width=60, command=settings, fg_color=acccolour, hover_color=highlight)
btn_settings.grid(row=0, column=0, padx=15, pady=5, sticky="ne")

List_load()
selection()
app.mainloop()
