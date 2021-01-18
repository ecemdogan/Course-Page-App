#libraries
import tkinter as tk
#from tkinter import PhotoImage
from tkinter import ttk
#from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("1080x640")   #1080x640
window.title("SYLLABI COURSE PAGE APP")

#toolbar
menubar = tk.Menu(window)
window.config(menu = menubar)
#help(manual)
help_ = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = help_)
help_.add_command(label = "Manual", command = None)

#panel windows
pw = ttk.Panedwindow(window, orient = tk.HORIZONTAL)
pw.pack(fill = tk.BOTH, expand = True)
m2 = ttk.Panedwindow(pw, orient = tk.VERTICAL)

frame_mtop = ttk.Frame(pw, width = 140, height = 240, relief = tk.RIDGE)
frame_mbottom = ttk.Frame(pw, width = 100, height = 400, relief = tk.RAISED)
m2.add(frame_mtop)
m2.add(frame_mbottom)

frame_left = ttk.Frame(pw, width = 240, height = 640, relief = tk.GROOVE) #for logo and app name
frame_right = ttk.Frame(pw, width = 700, height = 640, relief = tk.GROOVE) #for outline form
pw.add(frame_left)
pw.add(m2)
pw.add(frame_right)

# frame_right2 = ttk.Frame(pw, width = 700, height = 640, relief = tk.GROOVE)
# pw.add(frame_right2)

def buttonFunction():
    #when press the button, course outline will be seen.
    # frame_right2.get()
    # frame_right.configure(state = "disable")
    pass


#before press the button:
main_label1 = tk.Label(frame_right, text = "Syllabi - Course Page ", font = ("Times", 18, "italic"), bg = "#ffd9b3" )
main_label2 = tk.Label(frame_right, text = "Please create new syllabus or select the course code to edit.", 
                       font = ("Times", 14, "italic"), bg = "#ffd9b3" )
main_label1.pack(fill = tk.BOTH, expand = True)
main_label2.pack(fill = tk.BOTH, expand = True)

#create syllabus button

#photo = ImageTk.PhotoImage(file = Image.open('C:\Users\Elif\.spyder-py3\302_project\ieu_logo.png'))
#photoimage = photo.subsample(3, 3)
#button = tk.Button(window, text = "New Syllabus", image = photoimage,compound = LEFT).pack(side = TOP)

#ieu logo
# photo = PhotoImage(frame_left, file = r"C:\Users\Elif\.spyder-py3\302_project\ieu_logo.png")
# photoimage = photo.subsample(3, 3)

#Button(root, text = 'Click Me !', image = photoimage, compound = LEFT).pack(side = TOP) 
#img = ImageTk.PhotoImage(Image.open("ieu_logo.png"))
#img = tk.PhotoImage(file = "ieu_logo.png")
#panel = tk.Label(frame2, image = "ieu_logo.png")
#panel.pack(fill = tk.X, expand = True)

button = tk.Button(frame_mtop, text = "New Syllabus", font = ("Times",12, "bold"), height = 3, width = 20,
                   bg = "#004a8c", fg= "#e67300", activebackground = "#ffd9b3",
                   relief = tk.RAISED, command = buttonFunction)
#image = photoimage,
#button.place(x=0.5, y=0.5)
button.pack(fill = tk.X, expand = True)
#button.pack(side = tk.TOP)

#edit syllabus
edit_label = tk.Label(frame_mtop, text = "Syllabi", font = "Times 12", 
                      height = 2, width = 20,
                      bg = "#004a8c", fg= "#e67300", relief = tk.FLAT)
#label.place(x=0.5, y=45)
edit_label.pack(fill = tk.X, expand = True)

#search 
search_entry = tk.Entry(frame_mtop, text = "search")
search_entry.pack(side = tk.LEFT, fill = tk.X, expand = True) 
search_entry.focus_set() 
course_code = search_entry.get() 

search_button = tk.Button(frame_mtop, text = "Search")
search_button.pack(side = tk.RIGHT, fill = tk.X, expand = True)

text = tk.Text(frame_mbottom, width = 10)  
  
# text input area at index 1 in text window  
text.insert('1.0', '''Type your text here''')  
text.pack(fill = tk.BOTH, expand = True)

def search():  
      
    # remove tag 'found' from index 1 to END  
    text.tag_remove('found', '1.0', tk.END)  
      
    # returns to widget currently in focus  
    s = search_entry.get() 
      
    if (s):  
        idx = '1.0'
        while 1:  
            # searches for desried string from index 1  
            idx = text.search(s, idx, nocase = 1, stopindex = tk.END) 
              
            if not idx: break
              
            # last index sum of current index and length of text  
            lastidx = '% s+% dc' % (idx, len(s)) 
              
            # overwrite 'Found' at idx  
            text.tag_add('found', idx, lastidx)  
            idx = lastidx  
  
        # mark located string as red 
        text.tag_config('found', foreground ='red') 

search_button.config(command = search) 

#scroll
# scroll = tk.Scrollbar(frame_mbottom, orient = tk.VERTICAL)
#, command = text.yview
# scroll.grid(row = 0, column = 1, sticky = tk.N + tk.S)
# scroll.pack(side = tk.RIGHT, fill = tk.Y)
# text.config(yscrollcommand = scroll.set)

scrollbar = tk.Scrollbar(frame_mbottom)
scrollbar.pack( side = tk.RIGHT, fill = tk.Y )






window.mainloop()


