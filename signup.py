from tkinter import *
from tkinter import messagebox

# import con
import psycopg2
from PIL import ImageTk
from psycopg2 import  connect,extensions


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
def login_page():
    signup_window.destroy()
    import signin


def connect_database():
    if emailEntry.get() == '' or usernameEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error', 'Password Mismatch')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept Terms & Condition')
    else:
        try:
            host = 'localhost'
            user = 'postgres'
            password = '0000'
            port = '5432'
            connect_database = psycopg2.connect(
                host=host, user=user, password=password, port='5432'
            )
            connect_database.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            mycursor = connect_database.cursor()

            # query = 'CREATE DATABASE project'
            # mycursor.execute(query)
            # connect_database.close()  # Close the connection before creating the table

            connect_database = psycopg2.connect(
                host=host, user=user, password=password, port='5432', database='project'
            )
            connect_database.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)
            mycursor = connect_database.cursor()

            query = '''
            CREATE TABLE data1 (
                id SERIAL PRIMARY KEY,
                email VARCHAR(50),
                username VARCHAR(100),
                password VARCHAR(20)
            )
            '''
            mycursor.execute(query)
            connect_database.commit()  # Commit the changes

            messagebox.showinfo('Success', 'Database and Table Created Successfully')
            connect_database.close()  # Close the connection

        except psycopg2.Error as e:
            messagebox.showerror('Error', 'Database Error: ' + str(e))

    # ... (rest of your code)

        query='insert into data1(email,username,password) values(%s,%s,%s)'
        mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('success','done registration')
        clear()



# ... (rest of your code)


#GUI Part ---------

signup_window = Tk()
signup_window.geometry('990x660+230+50')
signup_window.title('signup  page')
signup_window.resizable(False,False)
background = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(signup_window,image=background)
bgLabel.place(x=0,y=0)

frame=Frame(signup_window,bg='white')
frame.place(x=557,y=105)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),
              bg='white',fg='red')
heading.grid(row=0,column=0,padx=10,pady=10,)

#Email button
emailLable=Label(signup_window,text='Email',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='red')
emailLable.place(x=570,y=160)

emailEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='red',fg='white')
emailEntry.place(x=575,y=189)


#user Button
usernameLable=Label(signup_window,text='Username',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='red')
usernameLable.place(x=570,y=215)

usernameEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='red',fg='white')
usernameEntry.place(x=575,y=245)

#password button
passwordLable=Label(signup_window,text='Password',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='red')
passwordLable.place(x=570,y=270)

passwordEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='red',fg='white')
passwordEntry.place(x=575,y=300)

#confirm password
confirmLable=Label(signup_window,text='Confirm Password',font=('Microsoft Yahei UI Light',12,'bold'),bg='white',fg='red')
confirmLable.place(x=570,y=325)

confirmEntry=Entry(signup_window,width=25,font=('Microsoft Yahei UI Light',12,'bold'),bg='red',fg='white')
confirmEntry.place(x=575,y=355)

#chech button
check=IntVar()
termsandcondition=Checkbutton(signup_window,text='I agree to the terms & condition',font=('Microsoft Yahei UI Light',10,'bold'),
                              bg='white',fg='red',activebackground='white',activeforeground='red',cursor='hand2',variable=check)
termsandcondition.place(x=570,y=398)

#SIGNUP button
signupButton=Button(signup_window,text='Signup',font=('Open Sans',14,'bold'),bd=0, bg='red',fg='white',
                    activebackground='red',activeforeground='white',width=17,command=connect_database)
signupButton.place(x=590,y=440)

#alredy have account
alredyaccount=Label(signup_window,text="Don't have an account?",font=('Open Sans','11','bold'),bg='white',fg='red')
alredyaccount.place(x=575,y=490)

#login Button
loginButton=Button(signup_window,text='Login in',font=('Open Sans','11','bold underline'),bg='white',
                   fg='blue',bd=0,cursor='hand2',activeforeground='blue',activebackground='white',command=login_page)
loginButton.place(x=745,y=488)


signup_window.mainloop()
