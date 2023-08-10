from tkinter import *
from PIL import ImageTk

#functionality part

def signup_page():
    login_window.destroy()
    import signup
def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0,END)


def password_enter(event):
    if passwordEntry.get() == 'password':
        passwordEntry.delete(0,END)



#GUI part

login_window=Tk()
login_window.geometry('990x660+230+50')
login_window.resizable(False,False)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),
              bg='white',fg='red')
heading.place(x=605,y=120)

#username designing ------

usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0 ,fg='red')
usernameEntry.place(x=590,y=190)
usernameEntry.insert(0,'Username')

usernameEntry.bind('<FocusIn>',user_enter)

Frame1=Frame(login_window,width=250,height=2,bg='red')
Frame1.place(x=590,y=212)

#password designing  ------

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0 ,fg='red')
passwordEntry.place(x=590,y=240)
passwordEntry.insert(0,'password')

passwordEntry.bind('<FocusIn>',password_enter)

Frame2=Frame(login_window,width=250,height=2,bg='red')
Frame2.place(x=590,y=262)


#eye Button -----

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',
                 cursor='hand2',command=hide)
eyeButton.place(x=810,y=235)

#forget password Button ------

forgetButton=Button(login_window,text='Forget Password?',bd=0,bg='white',activebackground='white',cursor='hand2'
                    ,font=('Microsoft Yahei UI Light',10,'bold'),fg='red',activeforeground='red')
forgetButton.place(x=703,y=275)


#login Button -----
loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='red'
                   ,activeforeground='white',activebackground='red',cursor='hand2',bd=0,width=19)
loginButton.place(x=582,y=320)


orLabel=Label(login_window,text='------------------- OR ------------------',font=('Open Sans',12),fg='red',bg='white')
orLabel.place(x=591,y=380)


facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=600,y=420)


googlek_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=googlek_logo,bg='white')
googleLabel.place(x=685,y=420)


twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=770,y=420)


signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='red',bg='white')
signupLabel.place(x=590,y=490)


newaccountButton=Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white'
                   ,activeforeground='blue',activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=730,y=490)

login_window.mainloop()