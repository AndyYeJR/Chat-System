from tkinter import *


class chatSystem:
    def __init__(self, parent):

        #heading 1
        self.title = Label(
            parent, 
            text="ICS Chat System",
            font=("Trebuchet MS", 20, "bold"),
            bg="darkblue",
            fg = "white"
            )
        self.title.place(relwidth=1, relheight=0.25,x=0,y=0)

        #button 1
        self.login_button = Button(parent, text="Login", command=self.login, justify="center",font=("Trebuchet MS", 20, "bold"),)
        self.login_button.place(relwidth = 0.5, relheight = 0.25, relx = 0, rely = 0.25)

        #button 2
        self.quit_button = Button(parent, text="Quit", fg="red", command=parent.destroy,font=("Trebuchet MS", 20, "bold"),)
        self.quit_button.place(relwidth = 0.5, relheight = 0.25, relx = 0.5, rely = 0.25)
             
        #entry_username
        self.entry_username = Entry(parent,font=("Trebuchet MS", 20, "bold"),)
        self.entry_username.insert(0, 'Username')
        self.entry_username.place(width = 400, height = 50, x = 200, y = 350)

        #entry_password
        self.entry_password = Entry(parent,font=("Trebuchet MS", 20, "bold"),)
        self.entry_password.insert(0, 'Password')
        self.entry_password.place(width = 400, height = 50, x = 200, y = 450)

        
    def login(self):
        flag=0
        f=open("login.txt","r")
        line_list=f.readlines()
        print(line_list)
        data_dict={}
        for item in line_list:
            if item[-1] == '\n':
                item = item[:-1]
            temp_list=item.split(",")
            print(temp_list)
            data_dict[temp_list[0]]=temp_list[1]
            print(data_dict)
        f.close()
        for keys,values in data_dict.items():
            print(keys,values)
            if keys==self.entry_username.get() and values==self.entry_password.get():
                flag=1

        print(flag)
#后面如果flag==1，就进行chat，不行就重新来，输错三次重启


def enter(event):
    print('Mouse Enter the Window')

def exit_(event):
    print('Mouse Leave the Window')

def button1Pressed(event):
    print('Button-1 pressed at x = % d, y = % d' % (event.x, event.y))


def button3Pressed(event):
    print('Button-3 pressed at x = % d, y = % d' % (event.x, event.y))

# def windowResize(event):
#     settingWidth = windowWidth
#
#     if settingWidth!= root.winfo_width():
#         windowWidth = root.winfo_width()
#         # windowHeight = root.winfo_height()




root = Tk()

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
windowWidth = 800
windowHeight = 600
x = (ws/2) - (windowWidth/2)
y = (hs/2) - (windowHeight/2)

#setting window size & position
root.geometry("%dx%d+%d+%d" % (windowWidth,windowHeight,x,y))#width x height + startX + startY

#window title
root.title("ICS Chat System")

root.bind('<Enter>', enter)
root.bind('<Leave>', exit_)
root.bind('<Button-1>', button1Pressed)
root.bind('<Button-3>', button3Pressed)
root.attributes("-alpha", 0.90)#window transparency
# root.bind('<Configure>', windowResize)
# root.resizable(0,0)#banned user zoom the window
app = chatSystem(root)
root.mainloop()