print("Hello World")
a=10
print(a)
name="Sahas"
print(name)
print(type(a))
print(type(name))
colors=["red","orange","yellow","green","blue","purple","pink","7 colors of the rainbow","Sahas made this var"]
print(colors)
print(type(colors))
from tkinter import*
root=Tk()
root.title("Identity Card")
root.geometry("300x400")
heading=Label(root,text="Identity Card")
heading.pack()

label_name=Label(root)

label_birthday=Label(root)

label_grade=Label(root)

label_subjects=Label(root)

label_vaccination=Label(root)

def mycarddetails():
    name="Sahas R. Etikyala"
    
    grade=6
    
    subjects=["Math",",ELA",",Social_Studies",",Science",",PE",",Computer_Science"]

    vaccination="1 dose taken on 11/15/2021"
    
    label_name["text"]=name
    
    label_birthday["text"]=" Born on 7/9/2010"
    
    label_grade["text"]=str(grade)+"th Grade"
    
    label_subjects["text"]=subjects
    
    label_vaccination["text"]="Covid Vaccine Status:"+vaccination

button_details=Button(root,text="Show Details",command=mycarddetails)
button_details.pack()
label_name.pack()
label_birthday.pack()
label_grade.pack()
label_subjects.pack()
label_vaccination.pack()
root.mainloop()