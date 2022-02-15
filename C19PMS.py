from tkinter import *
import tkinter.messagebox as tkMessageBox # Not necessary to provide an alias i.e, tkMessageBox
import tkinter.ttk as ttk
import csv
import os
root = Tk() #creation of the main root window
root.title("Covid-19 Patient Management System")
root.geometry("950x400")
root.resizable(0, 0)

Name = StringVar()
Age = StringVar()
Gender = StringVar()
BloodGroup = StringVar()
Symptoms = StringVar()
AdmissionStatus = StringVar()
AadharNumber = StringVar()
DateOfEntry = StringVar()


#FUNCTIONS_MAIN
def add_btn():
    add_win = Toplevel(bg="black")
    add_win.geometry('800x680')
    add_win.title("ADD PATIENT RECORD")
    # LAYOUT_MAIN
    Top_add = Frame(add_win, width=800, height=100, bd=8, relief="raise", bg='black')
    Top_add.pack(side=TOP)
    top_add_title = Label(Top_add, width=800, font=('constantia', 32), fg='misty rose', bg='black',
                      text="ADD PATIENT RECORD")
    top_add_title.pack()

    Bottom_add = Frame(add_win, width=800, height=50, bd=8, relief="raise", bg='black')
    Bottom_add.pack(side=BOTTOM, anchor="nw")
    Bottom_add.propagate(0)

    Left_add = Frame(add_win, width=800, height=580, bd=8, relief="raise", bg='black')
    Left_add.pack(side=LEFT,anchor = "nw")
    Left_add.propagate(0)
    Forms_add = Frame(Left_add, width=800, height=580, bg='black')
    Forms_add.pack(side=TOP)
    Forms_add.propagate(0)
    #Right_add = Frame(add_win, width=450, height=500, bd=8, relief="raise", bg='black')
    #Right_add.pack(side=LEFT, anchor = "nw")
    #Right_add.propagate(0)

    # LABELS_MAIN
    label0 = Label(Forms_add, text="Name:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label0.grid(row=0,stick="w")
    label1 = Label(Forms_add, text="Age:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label1.grid(row=1,stick="w")
    label2 = Label(Forms_add, text="Gender:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label2.grid(row=2,stick="w")
    label3 = Label(Forms_add, text="Blood Group:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label3.grid(row=3,stick="w")
    label4 = Label(Forms_add, text="Symptoms:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label4.grid(row=4,stick="w")
    label5 = Label(Forms_add, text="Admission Status:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label5.grid(row=5,stick="w")
    label6 = Label(Forms_add, text="Aadhar Number:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label6.grid(row=6,stick="w")
    label7 = Label(Forms_add, text="Date Of Entry:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label7.grid(row=7,stick="w")

    global entry0, entry1, entry2, entry3, entry4, entry5, entry6, entry7

    entry0 = Entry(Forms_add, textvariable=Name, width=30)  # Forms => parent window(left side)
    entry0.grid(row=0, column=1)
    entry1 = Entry(Forms_add, textvariable=Age, width=30)
    entry1.grid(row=1, column=1)
    entry2 = Entry(Forms_add, textvariable=Gender, width=30)
    entry2.grid(row=2, column=1)
    entry3 = Entry(Forms_add,textvariable=BloodGroup, width=30)
    entry3.grid(row=3, column=1)
    entry4 = Entry(Forms_add,textvariable=Symptoms, width=30)  # Forms => parent window(left side)
    entry4.grid(row=4, column=1)
    entry5 = Entry(Forms_add, textvariable=AdmissionStatus, width=30)
    entry5.grid(row=5, column=1)
    entry6 = Entry(Forms_add,textvariable=AadharNumber, width=30)
    entry6.grid(row=6, column=1)
    entry7= Entry(Forms_add,textvariable=DateOfEntry, width=30)
    entry7.grid(row=7, column=1)



    # BUTTONS_ADD
    btn_save = Button(Bottom_add, width=800, height=50, text="SAVE", font=('constantia', 21), bd=5, fg='lemon chiffon',
                      bg='black',relief="flat",command=save)
    btn_save.pack(anchor="w")

    #SAVE FUNCTION



def save():
    global s0, s1, s2, s3, s4, s5, s6, s7
    s0 = entry0.get()
    s1 = entry1.get()
    s2 = entry2.get()
    s3 = entry3.get()
    s4 = entry4.get()
    s5 = entry5.get()
    s6 = entry6.get()
    s7 = entry7.get()

    if entry0.get() == "" and entry1.get() == "" and entry2.get() == "" and entry3.get() == "" and entry4.get() == "" and entry5.get() == "" and entry6.get() == "" and entry7.get() == "":

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")
        entry0.delete(0, END)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)

    else:
        result = tkMessageBox.askquestion("Submit",
                                          "You are about to enter following details\n" + s0 + "\n" + s1 + "\n" + s2 + "\n" + s3 + "\n" + s4 + "\n" + s5 + "\n" + s6 + "\n" + s7)
        entry0.delete(0, END)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        if (result == "yes"):
            print("here")
            with open("C19PMS.csv", 'a') as csvfile:
                csvfile.write('{0}, {1}, {2}, {3},{4},{5},{6},{7}\n'.format(str(s0), str(s1), str(s2), str(s3), str(s4), str(s5), str(s6), str(s7)))
                print(s1,s2,s3,s4,s5)
            csvfile.close()
        else:
            entry0.set("")
            entry1.set("")
            entry2.set("")
            entry3.set("")
            entry4.set("")
            entry5.set("")
            entry6.set("")
            entry7.set("")

def update_btn():
    update_win = Toplevel(bg="Misty rose")
    update_win.geometry('800x680')
    update_win.title("UPDATE PATIENT RECORD")

    # LAYOUT_UPDATE
    Top_update = Frame(update_win, width=800, height=100, bd=8, relief="raise", bg='black')
    Top_update.pack(side=TOP)
    top_update_title = Label(Top_update, width=800, font=('constantia', 32), fg='misty rose', bg='black',
                      text="ADD UPDATE RECORD")
    top_update_title.pack()

    Bottom_update = Frame(update_win, width=800, height=50, bd=8, relief="raise", bg='black')
    Bottom_update.pack(side=BOTTOM, anchor="nw")
    Bottom_update.propagate(0)

    Left_update = Frame(update_win, width=800, height=580, bd=8, relief="raise", bg='black')
    Left_update.pack(side=TOP,anchor = "nw")
    Left_update.propagate(0)
    Forms_update = Frame(Left_update, width=800, height=580, bg='black')
    Forms_update.pack(side=TOP )
    Forms_update.propagate(0)
    #Right_add = Frame(add_win, width=450, height=500, bd=8, relief="raise", bg='black')
    #Right_add.pack(side=LEFT, anchor = "nw")
    #Right_add.propagate(0)

    # LABELS_UPDATE
    label0 = Label(Forms_update, text="Name:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label0.grid(row=0,stick="w")
    label1 = Label(Forms_update, text="Age:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label1.grid(row=1,stick="w")
    label2 = Label(Forms_update, text="Gender:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label2.grid(row=2,stick="w")
    label3 = Label(Forms_update, text="Blood Group:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label3.grid(row=3,stick="w")
    label4 = Label(Forms_update, text="Symptoms:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label4.grid(row=4,stick="w")
    label5 = Label(Forms_update, text="Admission Status:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label5.grid(row=5,stick="w")
    label6 = Label(Forms_update, text="Aadhar Number:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label6.grid(row=6,stick="w")
    label7 = Label(Forms_update, text="Date Of Entry:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label7.grid(row=7,stick="w")

    global entry_u0, entry_u1, entry_u2, entry_u3, entry_u4, entry_u5, entry_u6, entry_u7

    entry_u0 = Entry(Forms_update, width=30)  # Forms => parent window(left side)
    entry_u0.grid(row=0, column=1)
    entry_u1 = Entry(Forms_update,  width=30)
    entry_u1.grid(row=1, column=1)
    entry_u2 = Entry(Forms_update, width=30)
    entry_u2.grid(row=2, column=1)
    entry_u3 = Entry(Forms_update, width=30)
    entry_u3.grid(row=3, column=1)
    entry_u4 = Entry(Forms_update, width=30)  # Forms => parent window(left side)
    entry_u4.grid(row=4, column=1)
    entry_u5 = Entry(Forms_update, width=30)
    entry_u5.grid(row=5, column=1)
    entry_u6 = Entry(Forms_update, width=30)
    entry_u6.grid(row=6, column=1)
    entry_u7= Entry(Forms_update, width=30)
    entry_u7.grid(row=7, column=1)

    # BUTTONS_UPDATE
    btn_update = Button(Bottom_update, width=800, height=50, text="UPDATE", font=('constantia', 21), bd=5, fg='lemon chiffon',
                      bg='black',relief="flat",command=update)
    btn_update.pack(anchor="w")


def update():
    global u0, u1, u2, u3, u4, u5, u6, u7
    u0 = entry_u0.get()
    u1 = entry_u1.get()
    u2 = entry_u2.get()
    u3 = entry_u3.get()
    u4 = entry_u4.get()
    u5 = entry_u5.get()
    u6 = entry_u6.get()
    u7 = entry_u7.get()

    if entry_u0.get() == "" and entry_u1.get() == "" and entry_u2.get() == "" and entry_u3.get() == "" and entry_u4.get() == "" and entry_u5.get() == "" and entry_u6.get() == "" and entry_u7.get() == "":

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")
        entry_u0.delete(0, END)
        entry_u1.delete(0, END)
        entry_u2.delete(0, END)
        entry_u3.delete(0, END)
        entry_u4.delete(0, END)
        entry_u5.delete(0, END)
        entry_u6.delete(0, END)
        entry_u7.delete(0, END)

    else:
        result = tkMessageBox.askquestion("Submit",
                                          "You are about to update following details\n" + u0 + "\n" +u1 + "\n" + u2 + "\n" + u3 + "\n" + u4 + "\n" + u5 + "\n" + u6 + "\n" + u7)
        entry_u0.delete(0, END)
        entry_u1.delete(0, END)
        entry_u2.delete(0, END)
        entry_u3.delete(0, END)
        entry_u4.delete(0, END)
        entry_u5.delete(0, END)
        entry_u6.delete(0, END)
        entry_u7.delete(0, END)
        if (result == "yes"):
            print("here")
            with open("C19PMS.csv", "r") as f1, open("C19PMS1.csv", "w") as working:
                for line in f1:
                    if str(u6) not in line:
                        working.write(line)
                    else:
                        working.write('{0}, {1}, {2}, {3},{4} ,{5},{6},{7}\n'.format(str(u0),str(u1), str(u2), str(u3), str(u4), str(u5), str(u6),str(u7)))
            os.remove("C19PMS.csv")
            os.rename("C19PMS1.csv", "C19PMS.csv")
            entry_u0.delete(0, END)
            entry_u1.delete(0, END)
            entry_u2.delete(0, END)
            entry_u3.delete(0, END)
            entry_u4.delete(0, END)
            entry_u5.delete(0, END)
            entry_u6.delete(0, END)
            entry_u7.delete(0, END)



def del_btn():
    del_win = Toplevel(bg="Misty rose")
    del_win.geometry('800x680')
    del_win.title("DELETE PATIENT RECORD")

    # LAYOUT_DELETE
    Top_del = Frame(del_win, width=800, height=100, bd=8, relief="raise", bg='black')
    Top_del.pack(side=TOP)
    top_del_title = Label(Top_del, width=800, font=('constantia', 32), fg='misty rose', bg='black',
                      text="ADD DELETE RECORD")
    top_del_title.pack()

    Bottom_del = Frame(del_win, width=800, height=50, bd=8, relief="raise", bg='black')
    Bottom_del.pack(side=BOTTOM, anchor="nw")
    Bottom_del.propagate(0)

    Left_del = Frame(del_win, width=800, height=580, bd=8, relief="raise", bg='black')
    Left_del.pack(side=TOP,anchor = "nw")
    Left_del.propagate(0)
    Forms_del = Frame(Left_del, width=800, height=580, bg='black')
    Forms_del.pack(side=TOP )
    Forms_del.propagate(0)
    #Right_add = Frame(add_win, width=450, height=500, bd=8, relief="raise", bg='black')
    #Right_add.pack(side=LEFT, anchor = "nw")
    #Right_add.propagate(0)

    # LABELS_DELETE
    label0 = Label(Forms_del, text="Name:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label0.grid(row=0,stick="w")
    label1 = Label(Forms_del, text="Age:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label1.grid(row=1,stick="w")
    label2 = Label(Forms_del, text="Gender:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label2.grid(row=2,stick="w")
    label3 = Label(Forms_del, text="Blood Group:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label3.grid(row=3,stick="w")
    label4 = Label(Forms_del, text="Symptoms:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label4.grid(row=4,stick="w")
    label5 = Label(Forms_del, text="Admission Status:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label5.grid(row=5,stick="w")
    label6 = Label(Forms_del, text="Aadhar Number:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label6.grid(row=6,stick="w")
    label7 = Label(Forms_del, text="Date Of Entry:", fg='salmon', bg='black', font=('constantia', 22), bd=15)
    label7.grid(row=7,stick="w")

    global entry_d0, entry_d1, entry_d2, entry_d3, entry_d4, entry_d5, entry_d6, entry_d7

    entry_d0 = Entry(Forms_del, width=30)  # Forms => parent window(left side)
    entry_d0.grid(row=0, column=1)
    entry_d1 = Entry(Forms_del,  width=30)
    entry_d1.grid(row=1, column=1)
    entry_d2 = Entry(Forms_del, width=30)
    entry_d2.grid(row=2, column=1)
    entry_d3 = Entry(Forms_del, width=30)
    entry_d3.grid(row=3, column=1)
    entry_d4 = Entry(Forms_del, width=30)  # Forms => parent window(left side)
    entry_d4.grid(row=4, column=1)
    entry_d5 = Entry(Forms_del, width=30)
    entry_d5.grid(row=5, column=1)
    entry_d6 = Entry(Forms_del, width=30)
    entry_d6.grid(row=6, column=1)
    entry_d7= Entry(Forms_del, width=30)
    entry_d7.grid(row=7, column=1)

    # BUTTONS_DELETE
    btn_del = Button(Bottom_del, width=800, height=50, text="DELETE", font=('constantia', 21), bd=5, fg='lemon chiffon',
                      bg='black',relief="flat",command=delete)
    btn_del.pack(anchor="w")


def delete():
    global d0, d1, d2, d3, d4, d5, d6, d7
    d0 = entry_d0.get()
    d1 = entry_d1.get()
    d2 = entry_d2.get()
    d3 = entry_d3.get()
    d4 = entry_d4.get()
    d5 = entry_d5.get()
    d6 = entry_d6.get()
    d7 = entry_d7.get()

    if entry_d0.get() == "" and entry_d1.get() == "" and entry_d2.get() == "" and entry_d3.get() == "" and entry_d4.get() == "" and entry_d5.get() == "" and entry_d6.get() == "" and entry_d7.get() == "":

        print("Error")
        tkMessageBox.showerror("error", "there is issue with some information")
        entry_d0.delete(0, END)
        entry_d1.delete(0, END)
        entry_d2.delete(0, END)
        entry_d3.delete(0, END)
        entry_d4.delete(0, END)
        entry_d5.delete(0, END)
        entry_d6.delete(0, END)
        entry_d7.delete(0, END)

    else:
        result = tkMessageBox.askquestion("Submit",
                                          "You are about to update following details\n" + d0 + "\n" +d1 + "\n" + d2 + "\n" + d3 + "\n" + d4 + "\n" + d5 + "\n" + d6 + "\n" + d7)
        entry_d0.delete(0, END)
        entry_d1.delete(0, END)
        entry_d2.delete(0, END)
        entry_d3.delete(0, END)
        entry_d4.delete(0, END)
        entry_d5.delete(0, END)
        entry_d6.delete(0, END)
        entry_d7.delete(0, END)
        if (result == "yes"):
            print("here")
            with open("C19PMS.csv", 'r') as f, open("C19PMS1.csv", "w") as w1:
                for line in f:
                    if d6 not in line:
                        w1.write(line)
            os.remove("C19PMS.csv")
            os.rename("C19PMS1.csv", "C19PMS.csv")
            f.close()
            w1.close()
            entry_d0.delete(0, END)
            entry_d1.delete(0, END)
            entry_d2.delete(0, END)
            entry_d3.delete(0, END)
            entry_d4.delete(0, END)
            entry_d5.delete(0, END)
            entry_d6.delete(0, END)
            entry_d7.delete(0, END)




def view_btn():
    view_win = Toplevel(bg="Misty rose")
    view_win.geometry('1200x600')
    view_win.title("VIEW PATIENT RECORD")

    Top_view = Frame(view_win, width=1000, height=100, bd=8, relief="raise", bg='black')
    Top_view.pack(side=TOP)
    top_view_title = Label(Top_view, width=1000, font=('constantia', 32), fg='misty rose', bg='black',
                          text="VIEW RECORD")
    top_view_title.pack()

    # VIEW_TREE_MAIN

    scrollbary = Scrollbar(Top_view, orient=VERTICAL)
    scrollbarx = Scrollbar(Top_view, orient=HORIZONTAL)
    tree = ttk.Treeview(Top_view, columns=(
        "Name", "Age", "Gender", "BloodGroup", "Symptoms", "AdmissionStatus", "AadharNumber", "DateOfEntry"),
                        selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set , )
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Age', text="Age", anchor=W)
    tree.heading('Gender', text="Gender", anchor=W)
    tree.heading('BloodGroup', text="BloodGroup", anchor=W)
    tree.heading('Symptoms', text="Symptoms", anchor=W)
    tree.heading('AdmissionStatus', text="AdmissionStatus", anchor=W)
    tree.heading('AadharNumber', text="AadharNumber", anchor=W)
    tree.heading('DateOfEntry', text="DateOfEntry", anchor=W)

    tree.column('#0', stretch=NO, minwidth=20, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=80)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=130)
    tree.column('#6', stretch=NO, minwidth=0, width=120)
    tree.column('#7', stretch=NO, minwidth=0, width=120)

    tree.pack()

    tree.delete(*tree.get_children())
    with open('C19PMS.csv', "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        print(reader)
        for row in reader:
            print(row)
            Name = row['Name']
            Age = row['Age']
            Gender = row['Gender']
            BloodGroup = row['BloodGroup']
            Symptoms = row['Symptoms']
            AdmissionStatus = row['AdmissionStatus']
            AadharNumber = row['AadharNumber']
            DateOfEntry = row['DateOfEntry']

            tree.insert("", 0, values=(Name, Age, Gender, BloodGroup, Symptoms, AdmissionStatus,AadharNumber,DateOfEntry))
    f.close()








#LAYOUT_MAIN
Top = Frame(root, width=950, height=100 ,bd=8, relief="raise" ,bg='black')
Top.pack(side=TOP)
top_title = Label(Top, width=950, font=('constantia', 32),fg='misty rose' ,bg='black',text = "Covid-19 Patient Management System")
top_title.pack()

Left = Frame(root, width=650, height =600, bd=8 , relief = "raise" ,bg='black')
Left.pack(side=LEFT)
Forms = Frame(Left, width=650, height=600,bg='black')
Forms.pack(side=LEFT, anchor = "nw")
Left.propagate(0)
Buttons = Frame(root, width=300, height =600, bd=8 , relief = "raise" ,bg='black' )
Buttons.pack(side=LEFT,anchor="nw")
Buttons.propagate(0)

#LABELS_MAIN
label0 = Label(Forms, text="To add patient record:", fg='salmon' ,bg='black',font=('constantia', 22), bd=15)
label0.pack(anchor="w")
label1 = Label(Forms, text="To update patient record:",fg='salmon',bg='black', font=('constantia', 22), bd=15)
label1.pack(anchor="w")
label2 = Label(Forms, text="To delete patient record:",fg='salmon',bg='black', font=('constantia', 22), bd=15)
label2.pack(anchor="w")
label3 = Label(Forms, text="To view patient record:",fg='salmon', bg='black',font=('constantia', 22), bd=15)
label3.pack(anchor="w")


#BUTTONS_MAIN

btn_add = Button(Buttons, width=300, text="ADD", font=('constantia', 21) ,bd=5 ,fg='lemon chiffon', bg='black', command=add_btn )
btn_add.pack(anchor="w")
btn_update = Button(Buttons, width=300, text="UPDATE", font=('constantia', 21), bd=5 ,fg='lemon chiffon', bg='black', command=update_btn )
btn_update.pack(anchor="w")
btn_delete = Button(Buttons, width=300, text="DELETE",font=('constantia', 21) ,bd=5 ,fg='lemon chiffon', bg='black',command=del_btn)
btn_delete.pack(anchor="w")
btn_view = Button(Buttons, width=300, text="VIEW",font=('constantia', 21), bd=5 ,fg='lemon chiffon', bg='black',command=view_btn)
btn_view.pack(anchor="w")


"""
    VARIABLES DEFINATION
"""
#ADD_SAVE
s0 , s1 , s2 , s3 , s4 , s5 , s6 , s7 = "","","","","","","",""
#UPDATE
u0,u1,u2,u3,u4,u5,u6,u7="","","","","","","",""
#DELETE
d0,d1,d2,d3,d4,d5,d6,d7="","","","","","","",""

root.mainloop()
