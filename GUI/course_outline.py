import tkinter as tk

window = tk.Tk()
window.geometry("700x640")   #1080x640
window.title("COURSE OUTLINE FORM")

# scroll = tk.Scrollbar(window, orient = tk.VERTICAL)
# scroll.grid(row = 0, column = 1, sticky = tk.N + tk.S)
# #window.config(yscrollcomman = scroll.set)

scrollbar = tk.Scrollbar(window)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )

title_=tk.Label(window, text = "IZMIR UNIVERSITY OF ECONOMICS COURSE OUTLINE FORM", 
                font = "Times 14", justify = "center", wraplength = 350)
title_.place(x = 200, y = 10)

first_text = tk.Label(window, text = "1. GENERAL INFORMATION" , font = ("Times", 12, "bold"), 
                      bg = "orange",justify = "left",anchor = "w", width = 100)
first_text.place(x = 10, y = 70)

label1 = tk.Label(window, text = "Course Name", font = "Times 12", relief = tk.GROOVE)
label1.place(x = 10, y = 100, width = 150, height = 40)

course_name = tk.Entry(window)
course_name.place(x = 170, y = 100, width = 550, height = 40)

label2 = tk.Label(window, text = "Code", font = "Times 12", relief = tk.GROOVE)
label2.place(x = 10, y = 150, width = 100, height = 40 )

label3 = tk.Label(window, text = "Fall", font = "Times 12", relief = tk.GROOVE)
label3.place(x = 110, y = 150, width = 70, height = 40 )

label4 = tk.Label(window, text = "Spring", font = "Times 12", relief = tk.GROOVE)
label4.place(x = 180, y = 150, width = 70, height = 40 )

label5 = tk.Label(window, text = "Theory (hour/week)", font = "Times 12", wraplength = 100, relief = tk.GROOVE)
label5.place(x = 250, y = 150, width = 130, height = 40 )

label6 = tk.Label(window, text = "Application/Lab (hour/week)", font = "Times 12", wraplength = 100, relief = tk.GROOVE)
label6.place(x = 380, y = 150, width = 130, height = 40 )

label7 = tk.Label(window, text = "Local Credits", font = "Times 12", relief = tk.GROOVE)
label7.place(x = 510, y = 150, width = 100, height = 40 )

label8 = tk.Label(window, text = "ECTS", font = "Times 12", relief = tk.GROOVE)
label8.place(x = 610, y = 150, width = 70, height = 40 )

code = tk.Entry(window)
code.place(x = 10, y = 190, width = 100, height = 40 )

fall = tk.Radiobutton(window, value = "1", relief = tk.GROOVE)
fall.place(x = 110, y = 190, width = 70, height = 40 )

spring = tk.Radiobutton(window, value = "2", relief = tk.GROOVE)
spring.place(x = 180, y = 190, width = 70, height = 40 )

theory = tk.Entry(window)
theory.place(x = 250, y = 190, width = 130, height = 40 )

lab = tk.Entry(window)
lab.place(x = 380, y = 190, width = 130, height = 40 )

localCredits = tk.Entry(window)
localCredits.place(x = 510, y = 190, width = 100, height = 40 )

ects = tk.Entry(window)
ects.place(x = 610, y = 190, width = 70, height = 40 )


label9 = tk.Label(window, text = "Prerequisites", font = "Times 12", relief = tk.GROOVE)
label9.place(x = 10, y = 240, width = 150, height = 40)

prereq = tk.Entry(window)
prereq.place(x = 170, y = 240, width = 550, height = 40)

label10 = tk.Label(window, text = "Course Language", font = "Times 12", relief = tk.GROOVE)
label10.place(x = 10, y = 280, width = 150, height = 40)

lang1 = tk.Radiobutton(window, text = "English", value = "1", relief = tk.GROOVE)
lang1.place(x = 170, y = 280, width = 160, height = 40)
lang2 = tk.Radiobutton(window, text = "Turkish", value = "2", relief = tk.GROOVE)
lang2.place(x = 330, y = 280, width = 160, height = 40)
lang3 = tk.Radiobutton(window, text = "Second Foreign Language", value = "3", relief = tk.GROOVE)
lang3.place(x = 490, y = 280, width = 230, height = 40)

label11 = tk.Label(window, text = "Course Type", font = "Times 12", relief = tk.GROOVE)
label11.place(x = 10, y = 320, width = 150, height = 40)

type1 = tk.Radiobutton(window, text ="Required", value = "1", relief = tk.GROOVE)
type1.place(x = 170, y = 320, width = 275, height = 40)
type2 = tk.Radiobutton(window, text ="Elective", value = "2", relief = tk.GROOVE)
type2.place(x = 430, y = 320, width = 275, height = 40)

label12 = tk.Label(window, text = "Course Level", font = "Times 12", relief = tk.GROOVE)
label12.place(x = 10, y = 360, width = 150, height = 40)

level1 = tk.Radiobutton(window, text ="Short Cycle", value = "1", relief = tk.GROOVE)
level1.place(x = 170, y = 360, width = 135, height = 40)
level2 = tk.Radiobutton(window, text ="First Cycle", value = "2", relief = tk.GROOVE)
level2.place(x = 305, y = 360, width = 135, height = 40)
level3 = tk.Radiobutton(window, text ="Second Cycle", value = "3", relief = tk.GROOVE)
level3.place(x = 445, y = 360, width = 135, height = 40)
level4 = tk.Radiobutton(window, text ="Third Cycle", value = "4", relief = tk.GROOVE)
level4.place(x = 585, y = 360, width = 135, height = 40)

label13 = tk.Label(window, text = "Course Coordinator", font = "Times 12", relief = tk.GROOVE)
label13.place(x = 10, y = 410, width = 150, height = 40)
coor = tk.Entry(window)
coor.place(x = 170, y = 410, width = 550, height = 40)

label14 = tk.Label(window, text = "Course Lecturer(s)", font = "Times 12", relief = tk.GROOVE)
label14.place(x = 10, y = 450, width = 150, height = 40)
lect = tk.Entry(window)
lect.place(x = 170, y = 450, width = 550, height = 40)

label15 = tk.Label(window, text = "Assistant(s)", font = "Times 12", relief = tk.GROOVE)
label15.place(x = 10, y = 490, width = 150, height = 40)
assis = tk.Entry(window)
assis.place(x = 170, y = 490, width = 550, height = 40)


label16 = tk.Label(window, text = "Course Objectives", font = "Times 12", relief = tk.GROOVE)
label16.place(x = 10, y = 530, width = 150, height = 40)
obj = tk.Entry(window)
obj.place(x = 170, y = 530, width = 550, height = 40)

label17 = tk.Label(window, text = "Learning Outcomes", font = "Times 12", relief = tk.GROOVE)
label17.place(x = 10, y = 570, width = 150, height = 40)
outc = tk.Entry(window)
outc.place(x = 170, y = 570, width = 550, height = 40)

label18 = tk.Label(window, text = "Course Description", font = "Times 12", relief = tk.GROOVE)
label18.place(x = 10, y = 610, width = 150, height = 40)
desc = tk.Entry(window)
desc.place(x = 170, y = 610, width = 550, height = 40)




































window.mainloop()