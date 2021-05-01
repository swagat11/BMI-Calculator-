from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="bmi"
)
mycursor = mydb.cursor()



def calculate():
    try:
        a = float(txt1.get())
        b = float(txt2.get())
        mtr = (a / 100)
        res = b / mtr ** 2
        txt5.delete(0, END)
       # lbl3.configure(text=round(res, 2))  # round function is for limiting the decimal point
        txt5.insert(0,round(res,2))
        if (res <= 18.5):
            c_check_Label.config(text="UnderWeight")
        elif (res <= 25):
            c_check_Label.config(text="Normal")
        elif (res >= 30):
            c_check_Label.config(text="Obese")



    except Exception:
       # lbl3.configure(text='Error')
        print("Enter Proper Data")
       # txt5.delete(0,END)
        pass




def getdata():
    try:
        name = txt3.get()
        height = txt1.get()
        weight = txt2.get()
        #bmi= lbl3.cget("text")  # to get the value of bmi label
        bmi = float(txt5.get())
        status = c_check_Label.cget("text")
        if (name and height and weight and bmi):
            print("1")
            mycursor.execute("create table if not exists person(Name varchar(10),Height varchar(3),Weight varchar(3),BMI float,Status varchar(10))")
            print("2")
            mycursor.execute("insert into person(Name,Height,Weight,BMI,Status) values('" + name + "','" + height + "','" + weight + "','"+ str(bmi) +"','"+status +"')")
            print("3")
            mydb.commit()
            print("4")
            lbl9.config(text=" ")
            clr()
        else:
            print("Enter Details")

    except:
        print("Enter Values")


def show_record():
    cleardata()
    lbl9.config(text=" ")
    try:
        mycursor.execute("select * from person")
        data = mycursor.fetchall()

        for y in data:
            st.insert(INSERT, y)
            st.insert(INSERT, "\n")

    except:
        st.insert(INSERT, 'Error..Table Not exist')

def delete_record():
    dn = str(txt4.get())
    if (dn):
        mycursor.execute("select name from person where name like '%s'" % (dn))
        fn = mycursor.fetchone()
        if (fn):
            mycursor.execute("delete from person where name ='%s'" % (fn))
            mydb.commit()
            lbl9.config(text="deleted")
            print("deleted")
            txt4.delete(0, END)
        else:
            print("Record Not exist")
            lbl9.config(text="Record Not exist")
    else:
        print("Please Enter The Name")
        lbl9.config(text="Enter name")


def cleardata():
    st.delete(1.0, END)

def clr():
    txt1.delete(0, END)
    # txt1.configure(bg='red')
    txt2.delete(0, END)
    txt3.delete(0, END)
   # lbl3.configure(text='_____')
    txt5.delete(0, END)
    c_check_Label.config(text=" ")


root = Tk()
root.title("BMI Catlog System")  # set title of window
root.configure(bg='white')  # set bg color of window
root.geometry("600x600+100+100")  # set the size of window and position
#root.minsize(255, 250)  # for minimun window size
#root.maxsize(255, 250)  # for maximum window size

lbl7 = Label(root, text='Name', bg='white')
lbl1 = Label(root, text='Height', bg='white')
lbl2 = Label(root, text='Weight', bg='white')
txt5 = Entry(width=10, bg='white')           # lbl3
lbl4 = Label(root, text='BMI', bg='white')
lbl5 = Label(root, text='Cm', bg='white')
lbl6 = Label(root, text='Kg', bg='white')
lbl9 = Label(root, text='enter name', bg='white')

txt1 = Entry(width=10, bg='white')
txt2 = Entry(width=10, bg='white')
txt3 = Entry(width=10, bg='white') #name entry
txt4 = Entry(width=15, bg='white')

c_check_Label = Label(root, text='--', bg='white')
c_check_Label.grid(row = 3,column=2)
btn1 = ttk.Button(root, text='calculate', command=calculate)
btn2 = ttk.Button(root, text='clear', command=clr)
btn3 = ttk.Button(root, text='save', command=getdata)
btn4 = ttk.Button(root, text='Show', command=show_record)
btn5 = ttk.Button(root, text='Delete Record', command=delete_record)

lbl8 = Label(root,text ="Show Record",font="bold 10",bg='white')
lbl8.grid(row=7 ,column =0,sticky='w')
lbl10 = Label(root,text ="Name    Height   Weight  BMI  Status",font="bold 10",bg='white')
lbl10.grid(row=6 ,column =1,sticky='w')
st=scrolledtext.ScrolledText(root,width=30,height=8)
st.grid(row=9,column=1)

# we use here sticky option for positioning the grid cell
lbl7.grid(row=0, column=0, padx=15, pady=20)
txt3.grid(row=0, column=1)
lbl1.grid(row=1, column=0, padx=15, pady=20)
lbl2.grid(row=2, column=0, padx=15, pady=20)
txt1.grid(row=1, column=1)
txt2.grid(row=2, column=1)
btn1.grid(row=4, column=1, pady=20, padx=20)
txt5.grid(row=3, column=1, pady=20)              #lbl3
lbl4.grid(row=3, column=0)
btn2.grid(row=4, column=0, pady=20, padx=20)
btn3.grid(row=4, column=2, pady=20, padx=20)  # save record
btn4.grid(row=9, column=0, pady=20, padx=20) # show record
btn5.grid(row=10, column=0, pady=20, padx=20)   # delete record
txt4.grid(row=10, column=1, pady=20, padx=20)
lbl5.grid(row=1, column=2)
lbl6.grid(row=2, column=2)
lbl9.grid(row=11, column=1)

root.mainloop()
