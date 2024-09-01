import sys
from os import strerror
import customtkinter
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
Settingsicon = customtkinter.CTkImage(light_image=Image.open("Settings-icon.png"), size=(30, 30))

Q = 1
cor = 0
incc = 0
Tmp = 0
Comp = 0
def change_appearance_mode(new_mode):
    customtkinter.set_appearance_mode(new_mode)

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

def List_load():
  global Tmp
  global Max
  global rand_list
  global Comp
  Comp = 0
  rand_list = []
  while Tmp < Max:
    Tmp = Tmp+1
    rand_list.append(Tmp)
    print("Added " +str(Tmp))
    print("Curr list " +str(rand_list))

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

def settings():
    global entry
    global settings_window
    global option_menu
    try:
        if settings_window.winfo_exists():
            settings_window.focus()  # If window exists, focus it
    except NameError:
        settings_window = customtkinter.CTkToplevel(app)
        settings_window.title("Settings")
        settings_window.geometry("480x240")
        settings_window.resizable(0, 0)  # Create window if it doesn't exist
        label = customtkinter.CTkLabel(settings_window, text="Enter the config path", text_color="white")
        label.grid(row=0, column=0, padx=0, pady=0)
        settings_window.grid_columnconfigure(0, weight=1)
        entry = customtkinter.CTkEntry(settings_window, placeholder_text="Config Path")
        entry.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        update_button = customtkinter.CTkButton(settings_window, text="Update Path", command=conf_upd)
        update_button.grid(row=1, column=0, padx=20, pady=0, sticky="nsew")
        appearance_mode_menu = customtkinter.CTkOptionMenu(settings_window, values=["Light", "Dark", "System"], command=change_appearance_mode)
        appearance_mode_menu.grid(row=3, column=0, padx=0, pady=(20, 10))
        




#Selection system
def selection():
    global Comp
    if Comp != Max:
        label2.configure(text_color="white")
        label3.configure(text_color="white")
        label4.configure(text_color="white")
        label5.configure(text_color="white")
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

btn_settings = customtkinter.CTkButton(app, image=Settingsicon, text="", width=60, command=settings)
btn_settings.grid(row=0, column=0, padx=15, pady=5, sticky="ne")

List_load()
selection()
app.mainloop()
