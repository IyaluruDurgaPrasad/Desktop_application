from tkinter import *
import tkinter.messagebox as msg
import pymysql as p
root=Tk()
root.title('Hospital Management')
root.geometry('4250x280')
#Creating patient registration form.
def register():
    def patient_add():
        id=p_id.get()
        name=p_name.get()
        age=p_age.get()
        gender=p_gender.get()
        address=p_address.get()
        mobile=p_mobile.get()
        disease=p_disease.get()

        if (id=='' or name=='' or age=='' or gender=='' or address=='' or mobile=='' or disease==''):
            msg.showwarning('Insert Status','Required All Fields.......')
        else:
            connection=p.connect(host='localhost',user='root',password='',db='hospital')
            cursor=connection.cursor()
            query="insert into hms values({},'{}',{},'{}','{}','{}','{}')".format(id,name,age,gender,address,mobile,disease)
            cursor.execute(query)
            connection.commit()
            msg.showinfo('insert status','Record inserted successfullyy....')
            p_id.delete(0,END)
            p_name.delete(0,END)
            p_age.delete(0,END)
            p_gender.delete(0,END)
            p_address.delete(0,END)
            p_mobile.delete(0,END)
            p_disease.delete(0,END)
            connection.close()
    root.title('Patient Registration Form')
    f1=Frame()
    f1.place(width=4250,height=2080)
    title=Label(f1,text='Patient Registration Form',bg='grey',fg='black',font=('bold',20),width=40)
    title.place(x=350,y=80)
    #field names
    id=Label(f1,text="Patient Id :",font=('bold',15))
    id.place(x=350,y=150)
    name=Label(f1,text="Patient Name :",font=('bold',15))
    name.place(x=350,y=200)
    age=Label(f1,text="Patient Age :",font=('bold',15))
    age.place(x=350,y=250)
    gender=Label(f1,text="Patient Gender :",font=('bold',15))
    gender.place(x=350,y=300)
    address=Label(f1,text="Patient Address :",font=('bold',15))
    address.place(x=350,y=350)
    mobile=Label(f1,text="Patient Phone No. :",font=('bold',15))
    mobile.place(x=350,y=450)
    disease=Label(f1,text="Patient Disease :",font=('bold',15))
    disease.place(x=350,y=400)

    #text fields
    p_id=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_id.place(x=620,y=150)
    p_name=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_name.place(x=620,y=200)
    p_age=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_age.place(x=620,y=250)
    p_gender=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_gender.place(x=620,y=300)
    p_address=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_address.place(x=620,y=350)
    p_disease=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_disease.place(x=620,y=400)
    p_mobile=Entry(f1,bg='pink',fg='black',width=30,bd=5,font=('bold',15))
    p_mobile.place(x=620,y=450)

    #Add patient Button
    add=Button(f1,text='Submit',bg='blue',fg='black',bd=4,font=('bold',15),command=patient_add)
    add.place(x=400,y=550)


    #Update 
    def update():
        id=p_id.get()
        name=p_name.get()
        age=p_age.get()
        gender=p_gender.get()
        address=p_address.get()
        mobile=p_mobile.get()
        disease=p_disease.get()
        if (id=='' or name=='' or age=='' or gender=='' or address=='' or mobile=='' or disease==''):
            msg.showinfo('Update Status','Patient ID is Required.....')
        else:
            connection=p.connect(host='localhost',user='root',password='',db='hospital')
            cursor=connection.cursor()
            query2=f"update hms set name=('{name}'),age=({age}),gender=('{gender}'),address=('{address}'),mobile=('{mobile}'),disease=('{disease}') where id=({id})"
            cursor.execute(query2)
            cursor.execute('commit')
            msg.showinfo('update status','Record Updated successfullyy....')
            p_id.delete(0,END)
            p_name.delete(0,END)
            p_age.delete(0,END)
            p_gender.delete(0,END)
            p_address.delete(0,END)
            p_mobile.delete(0,END)
            p_disease.delete(0,END)
            connection.close()



    #Update button
    update=Button(f1,text='Update',bg='green',fg='black',bd=4,font=('bold',15),command=update)
    update.place(x=500,y=550)





    def delete():
        id=p_id.get()
        if id=='':
            msg.showwarning('Delete Status','ID is required......')
        else:
            connection=p.connect(host='localhost',user='root',password='',db='hospital')
            cursor=connection.cursor()
            query1="delete from hms where id={}".format(id)
            cursor.execute(query1)
            cursor.execute('commit')
            p_id.delete(0,END)
            p_name.delete(0,END)
            p_age.delete(0,END)
            p_gender.delete(0,END)
            p_address.delete(0,END)
            p_mobile.delete(0,END)
            p_disease.delete(0,END)
            msg.showerror('Delete status','Record  Deleted Successfully......')
            
            
            
    #Delete Button 
    delete=Button(f1,text='Delete',bg='red',fg='black',bd=4,font=('bold',15),command=delete)
    delete.place(x=600,y=550)


    #display data
    def display():
        root.title('Patient Records')
        root.geometry('700x800')
        f3=Frame()
        f3.place(width=4250,height=2800)
        l1=Label(f3,text='Patient Records',font=('bold',15),bd=2,bg='grey',width=40)
        l1.place(x=400,y=90)
        list=Listbox(f3,width=200,height=100,bd=2,font=('bold',15))
        list.place(x=10,y=150)
        connection=p.connect(host='localhost',user='root',password='',db='hospital')
        cursor=connection.cursor()
        query3='select * from hms'
        cursor.execute(query3)
        rows=cursor.fetchall()
        for i in rows:     
            data=f"{str(i[0])}   |   {str(i[1])}     |        {str(i[2])}   |   {str(i[3])}   |   {str(i[4])}   |   {str(i[5])}    |     {str(i[6])}"
            list.insert(list.size(),data)
        connection.close()

    

    #display button
    display=Button(f1,text="Patient Records",font=('bold',15),bd=2,bg='cyan',fg='black',command=display)
    display.place(x=700,y=550)

#View the patients data

def show():
    f2=Frame()
    f2.place(width=4250,height=280)
    l=Label(f2,text='Patients Record', font=('bold',15),bd=3,bg='grey',fg='black',width=50)
    l.place(x=400,y=90)
    list=Listbox(f2,width=200,height=100,bd=2,font=('bold',15))
    list.place(x=100,y=150)
    connection=p.connect(host='localhost',user='root',password='',db='hospital')
    cursor=connection.cursor()
    query="select * from hms"
    cursor.execute(query)
    rows=cursor.fetchall()
    list.delete(0,list.size())
    for i in rows:
        data=f"{str(i[0])}   |   {str(i[1])}     |        {str(i[2])}   |   {str(i[3])}   |   {str(i[4])}   |   {str(i[5])}    |     {str(i[6])}"
        list.insert(list.size(),data)
    connection.close()






#Creating Home Page buttons
f=Frame()
f.place(width=4250,height=280)      
dashBoard=Label(f,text='DashBoard Of Hospital Management',font=('bold',30),justify=CENTER)
dashBoard.place(x=350,y=50)
register=Button(f,text='Registration',bg='aqua',fg='black',font=('bold',15),padx=1,pady=1,command=register)
register.place(x=400,y=200)
medical=Button(f,text='Medical Bill',bg='chocolate',fg='black',font=('bold',15),padx=1,pady=1)
medical.place(x=590,y=200)
patient=Button(f,text='Patients Data',bg='darkolivegreen',fg='black',font=('bold',15),padx=1,pady=1,command=show)
patient.place(x=780,y=200)  



root.mainloop()