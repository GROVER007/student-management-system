from tkinter import *
from tkinter import ttk,messagebox
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title("informatics practices project")
root.geometry("800x567")
root.maxsize("800","567")
root.minsize("790","567")
root.config(bg = "lightgrey",borderwidth = 5,relief = "sunken")

def import_data():
    import_btn.config(state = "disabled")
    global df
    df = pd.read_csv("data.csv")
    length = len(df)
    global list1
    list1 = []

    for i in range(length):
        list1.append([])
        c = df.iloc[i]
        for j in c :
            list1[i].append(j)
    for a in list1:
        tree.insert(parent = "",index= "end",values = a)
    notebook.tab(1,state = "normal")
    notebook.tab(2,state = "normal")
    notebook.tab(3,state = "normal")
    notebook.tab(4,state = "normal")

def add_record():
    adm_no = admno_entry.get()
    f_name = fname_entry.get()
    l_name = lname_entry.get()
    marks = marks_entry.get()
    
    list2 = []
    exist1 = False
    number = True
    adm_int = True

    try:
        int(adm_no)
    except:
        adm_int = False
    
    for check in range(len(list1)):
        list2.append(str(list1[check][0]))

    try :
        a = int(marks)
        number = True
    except:
        number = False

        
    if str(adm_no) in list2:
        exist1 = True
    else:
        exist1 = False


    if len(adm_no)<1 or len(f_name)<1 or len(l_name)<1 or len(marks)<1:
        messagebox.showerror("empty cell","you can`t leave any cell empty")
    elif len(adm_no) != 5 :
        messagebox.showerror("admission number","your admission number should is 5 numbers")
    elif adm_int == False:
        messagebox.showerror("admission number","your admission number should be in numbers")
    elif exist1 == True:
        messagebox.showerror("admission number","admission number already exists")
    elif number == False:
        messagebox.showerror("marks","enter marks in numbers not in words")
    else:
        df.loc[len(df.index)] = [adm_no,f_name,l_name,marks]
        admno_entry.delete(0,END)
        fname_entry.delete(0,END)
        lname_entry.delete(0,END)
        marks_entry.delete(0,END)
        for i in tree.get_children():
            tree.delete(i)
        df.to_csv("data.csv",index = False)
        import_data()

def delete_all():
    for change in tree.get_children():
        tree.delete(change)

    dataf = pd.DataFrame(columns = ["adm_no","f_name","l_name","marks"])

    dataf.to_csv("data.csv",index = False)
    messagebox.showinfo("deleted successfully","your changes has been done successfully")
    import_data()

def delete_selected():
    x = tree.selection()
    if len(x) == 0:
        messagebox.showerror("error","nothing is selected")
    else:
        for count in x:
            tree.delete(count)
        
        raw_data = []
        data = []
    
        no = len(tree.get_children())
    
        for i in tree.get_children():
            raw_data.append(tree.item(i))

        for j in range(no):
            data.append(raw_data[j]["values"])
        
        if len(data) < 1:
            dataf = pd.DataFrame(columns = ["adm_no","f_name","l_name","marks"])

            dataf.to_csv("data.csv",index = False)
            messagebox.showerror("deleted successfully","your changes has been done successfully")
            import_data()
        else:
            dataf = pd.DataFrame(data)
            dataf.to_csv("data.csv",index = False)
            messagebox.showinfo("deleted successfully","your changes has been done successfully")
            for i in tree.get_children():
                tree.delete(i)
            import_data()

        

def verify():
    adm_no = frame3_entry1.get()
    exist = True
    adm_int = True

    try:
        int(adm_no)
    except:
        adm_int = False

    for b in range(len(list1)):
        if str(adm_no) in str(list1[b]):
            a = b
            exist = True
            break
            
        else:
            exist = False

            
    if len(adm_no)<1:
        messagebox.showerror("Admission Number","please enter admission number to proceed")
    elif adm_int == False:
        messagebox.showerror("Admission Number","admission number should be in numbers")
    elif exist == False:
        messagebox.showerror("Admission Number","admission number does`nt exist")
    else:
        frame3_entry2.config(state = "normal")
        frame3_entry3.config(state = "normal")
        frame3_entry4.config(state = "normal")

        frame3_entry1.config(state = "disabled")
        verify_btn.config(state = "disabled")
        
        frame3_entry2.insert(0,str(list1[a][1]))
        frame3_entry3.insert(0,str(list1[a][2]))
        frame3_entry4.insert(0,str(list1[a][3]))
        submit2.config(state = "normal")
        

def update():
    adm_no = frame3_entry1.get()
    f_name = frame3_entry2.get()
    l_name = frame3_entry3.get()
    marks = frame3_entry4.get()

    list2 = [adm_no,f_name,l_name,marks]

    inti = True

    try:
        a = int(marks)
    except:
        inti = False



    for b in range(len(list1)):
        if str(adm_no) in str(list1[b]):
            a = b
            break
            

    if  len(f_name)<1 or len(l_name)<1 or len(marks)< 1:
        messagebox.showerror("empty cell","you can`t leave any cell empty")  
    elif inti == False:
        messagebox.showerror("marks","marks should be in numbers")
    else:
        list1[a] = list2
        dataf = pd.DataFrame(list1)
        dataf.to_csv("data.csv",index = False)
        frame3_entry1.config(state = "normal")
        verify_btn.config(state = "normal")
        frame3_entry1.delete(0,END)
        frame3_entry2.delete(0,END)
        frame3_entry3.delete(0,END)
        frame3_entry4.delete(0,END)
        
        for i in tree.get_children():
            tree.delete(i)
        for a in list1:
            tree.insert(parent = "",index= "end",values = a)
        frame3_entry2.config(state = "disabled")
        frame3_entry3.config(state = "disabled")
        frame3_entry4.config(state = "disabled")
        submit2.config(state = "disabled")
        messagebox.showinfo("updated","the given data is updated now")

def compare():
    raw_data = []
    data = []
    items = []
    names = []
    
    x = tree.selection()
    for count in x:
        tree.focus(count)
        values = tree.item(count)
        raw_data.append(values)

    for j in range(len(raw_data)):
        data.append(raw_data[j]["values"])

    for a in range(len(data)):
        items.append(data[a][1])
        names.append(data[a][3])

    plt.style.use('dark_background')
    plt.bar(items,names)
    plt.ylabel("Marks")
    plt.xlabel("Names")
    plt.show()
    
    

s = ttk.Style()
s.theme_use("alt")

tree_frame = Frame(root,borderwidth = 5,bg = "lightgrey")
tree_frame.pack()

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side = "right",fill = "y")

tree = ttk.Treeview(tree_frame,selectmode = "extended", yscrollcommand = tree_scroll.set)

tree_scroll.config(command  = tree.yview)

tree["columns"] = ["adm_no","f_name","l_name","marks"]

tree.column("#0",width = 0,stretch = "no")
tree.column("adm_no",width = 180,anchor = "w")
tree.column("f_name",width = 180,anchor = "center")
tree.column("l_name",width = 180,anchor = "center")
tree.column("marks",width = 180,anchor = "center")

tree.heading("adm_no",text = "Admission Number",anchor = 'w')
tree.heading("f_name",text = "First Name",anchor = 'center')
tree.heading("l_name",text = "Last Name",anchor = 'center')
tree.heading("marks",text = "Marks",anchor = 'center')

tree.pack()

notebook = ttk.Notebook(root)
notebook.pack(fill = "both")

frame0 = Frame(notebook,width = 2000,height = 300,borderwidth = 7,relief = "sunken")
frame0.pack(fill = "both")

#stuff in frame0:
import_label = Label(frame0,text = "press import button to open file here :",font = ("verdana",17,"bold"))
import_label.pack(anchor = "center",pady = 30)
import_btn = Button(frame0,text = "Import File",command = import_data,padx = 10,pady = 5,bg = "lightgrey",font = ("verdana",12),borderwidth = 5,relief = "raised")
import_btn.pack(pady = 30)

frame1 = Frame(notebook,width = 2000,height = 300,borderwidth = 7,relief = "sunken")
frame1.pack(fill = "both")

#stuff in frame1:
form_frame = Frame(frame1,padx = 10)
form_frame.pack(pady = 35,padx = 70)

admno_label = Label(form_frame,text = "Admission Number",pady = 10,padx = 10,font = ("verdana",13,"bold"))
admno_label.grid(row = 0,column = 1,sticky = "w")
admno_entry = Entry(form_frame,font = ("ariel",12))
admno_entry.grid(row = 0,column = 2)

fname_label = Label(form_frame,text = "First Name",padx = 10,font = ("verdana",13,"bold"))
fname_label.grid(row = 1,column = 1,sticky = "w")
fname_entry = Entry(form_frame,font = ("ariel",12))
fname_entry.grid(row = 1,column = 2)

lname_label = Label(form_frame,text = "Last Name",pady = 10,padx = 10,font = ("verdana",13,"bold"))
lname_label.grid(row = 2,column = 1,sticky = "w")
lname_entry = Entry(form_frame,font = ("ariel",12))
lname_entry.grid(row = 2,column = 2)

marks_label = Label(form_frame,text = "Marks",padx = 10,font = ("verdana",13,"bold"))
marks_label.grid(row = 3,column = 1,sticky = "w")
marks_entry = Entry(form_frame,font = ("ariel",12))
marks_entry.grid(row = 3,column = 2)

submit1 = Button(frame1,text = "Submit",bg = "light grey",padx = 10,pady = 5,font = ("verdana",10,"bold"),command = add_record,borderwidth = 5,relief = "raised")
submit1.pack()

frame2 = Frame(notebook, width = 2000,height = 300,borderwidth = 7,relief = "sunken")
frame2.pack(fill = "both")

#stuff in frame2:
frame2_label1 = Label(frame2,text = "Delete All Records : ",font = ("verdana",20,"bold"))
frame2_label1.pack(anchor = "center",pady = 20)
delall_btn = Button(frame2,text = "Delete All",font = ("verdana",12),bg = "light grey",command = delete_all,borderwidth = 5,relief = "raised")
delall_btn.pack(anchor = "center")

frame2_label2 = Label(frame2,text = "Delete Selected Items : ",font = ("verdana",20,"bold"))
frame2_label2.pack(anchor = "center",pady = 20)
delsel_btn = Button(frame2,text = "Delete Selected",font = ("verdana",12),bg = "light grey",command = delete_selected,borderwidth = 5,relief = "raised")
delsel_btn.pack()

frame3 = Frame(notebook, width = 2000,height = 300,borderwidth = 7,relief = "sunken")
frame3.pack(fill = "both")

#stuff in frame3:
frame3_label1 = Label(frame3,text = "Update your Records Here :",font = ("verdana",17,"bold"))
frame3_label1.pack(pady = 20)

update_frame = Frame(frame3)
update_frame.pack(anchor = "n")
frame3_label2 = Label(update_frame,text = "Adm number",font = ("verdana",12,"bold"),pady = 20)
frame3_label2.grid(row = 0,column = 0,rowspan = 1)
frame3_entry1 = Entry(update_frame,font = ("ariel",10))
frame3_entry1.grid(row = 0,column = 1)
verify_btn = Button(update_frame,text = "Verify",font = ("verdana",12,"bold"),bg = "lightgrey",command = verify,borderwidth = 5,relief = "raised")
verify_btn.grid(row = 0,column =2)

frame3_label3 = Label(update_frame,text = "First Name ",font = ("verdana",12,"bold"),pady = 10)
frame3_label3.grid(row = 1,column = 0,)
frame3_label4 = Label(update_frame,text = "Last Name ",font = ("verdana",12,"bold"),pady = 10)
frame3_label4.grid(row = 1,column =1,)
frame3_label5 = Label(update_frame,text = "Marks ",font = ("verdana",12,"bold"),pady = 10)
frame3_label5.grid(row = 1,column = 2,)

frame3_entry2 = Entry(update_frame,font = ("ariel",10),state = "disabled")
frame3_entry2.grid(row = 2,column = 0,rowspan = 2)
frame3_entry3 = Entry(update_frame,font = ("ariel",10),state = "disabled")
frame3_entry3.grid(row = 2,column = 1,rowspan = 2)
frame3_entry4 = Entry(update_frame,font = ("ariel",10),state = "disabled")
frame3_entry4.grid(row = 2,column = 2,rowspan = 2)

submit2 = Button(frame3,text = "submit",font = ("verdana",12,"bold"),bg = "lightgrey",command = update,state = "disabled",borderwidth = 5,relief = "raised")
submit2.pack(pady = 24)


frame4 = Frame(notebook, width = 2000,height = 300,borderwidth = 7,relief = "sunken")
frame4.pack(fill = "both")

#stuff in frame4:
comp_label = Label(frame4,text = "compare the marks of selected records : ",font = ("verdana",17,"bold"))
comp_label.pack(pady = 20)

comp_btn = Button(frame4,text = "Compare",padx = 10,pady = 5,bg = "lightgrey",font = ("verdana",12),command = compare,borderwidth = 5,relief = "raised")
comp_btn.pack(pady =30)



#adding tabs in notebook
notebook.add(frame0,text = "Import")
notebook.add(frame1,text = "Add Record")
notebook.add(frame2,text = "Delete Record")
notebook.add(frame3,text = "Update Record")
notebook.add(frame4,text = "Compare Marks")

notebook.tab(1,state = DISABLED)
notebook.tab(2,state = DISABLED)
notebook.tab(3,state = DISABLED)
notebook.tab(4,state = DISABLED)


root.mainloop()
