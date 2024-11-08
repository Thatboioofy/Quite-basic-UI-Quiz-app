# Quite-basic-UI-Quiz-app
(Also sorry for the bad spelling)
A fairly basic and badly written Quiz app with somwhat working customisations

This program is really badly written and will be broken sometimes when im adding new features but it also now has a conf file making it easier to make your own quiz using it.

This also requires both CustomTKinter and configparser to be installed to work (You can search up on how to install them)

Most of the bugs have been fixed please report them if they occur

#Instructions to run the program:

1st you need python 3.10 (one I tested it on may work on other idrk)
Use `pip3 install customtkinter` and `pip3 install configparser` to install the required modules
Then extract both New-UI-Quiz.py and conf.txt to the same folder as otherwise the program will not run
Lastly run the python file and it should work (report any problems)

#Editing the conf.txt file:

to make your own quiz you need to edit the conf to change the questions
all questions should look something like this
`[Q1]
Title = What does UO stand for?
Op1 = 1) Underlying OS
Op2 = 2) Unplanned override
Op3 = 3) Unplanned overload
Op4 = 4) Uni OS
Correct-ans = 3`
where you change the Title to the question you want to be shown
the Op1/2/3/4 as the options the user has to select from 
the Correct-ans just tells the program what the correct Op would be 

Goals : 
- [ ] add True/False question type
- [x] add multiple choice question type (In beta release also still broken)
- [x] add settings
- [x] add new selection system
- [x] add streak system
- [x] Compile to singular exe for ease of use
- [ ] make monitoring website for mass questionaire


(Streak system and exe are only in pre-release for now)
 
