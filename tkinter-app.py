import customtkinter
import json
customtkinter.set_default_color_theme("blue")
customtkinter.set_appearance_mode("dark")
app=customtkinter.CTk()
app.title("tkinter")
app.geometry("600x400")
app.columnconfigure(0,weight=1)

subjects=["history","science","gk","cricket","movies","entertainment"]
currentWidgets=[]
correctAns=[]
choosenAns=[]
data={}

def getRandomQ(arr):
    return arr[0:5]

index=0
title=customtkinter.CTkLabel(text="Quiz App in Tkinter",master=app,font=customtkinter.CTkFont(size=30))
title.grid(pady=30,padx=30,row=0,column=0)
# title=customtkinter.CTkLabel(text="This quiz contains 6 genre. You can choose any genre you like.",master=app,font=customtkinter.CTkFont(size=20))
# title.grid(pady=30,padx=30,row=0,column=0)
selectedQuestion=[]


def destroyWidgets():
    if(len(currentWidgets)):
        for c in currentWidgets:
            c.destroy()

def exitFn():
        destroyWidgets()
        renderChoices()
        selectedQuestion.clear()
        global index
        index=0
        choosenAns.clear()
        correctAns.clear()

def choosenAnsFn(ans):
    choosenAns.append(ans)
    renderQuestion()

def checkAns():
    print(choosenAns)
    print(correctAns)
    destroyWidgets()
    tempFrame=customtkinter.CTkFrame(master=app,width=300,height=200)
    tempFrame.grid(row=1,column=0)
    currentWidgets.append(tempFrame)
    score=0
    for ans in correctAns:
        if ans in choosenAns:
            score+=1
    result=customtkinter.CTkLabel(master=tempFrame,text=f"You got {score} out of 5 questions correct !!")
    result.grid(row=0,column=0,padx=20,pady=20)
    exitBtn=customtkinter.CTkButton(master= tempFrame,text="exit",command=exitFn)
    exitBtn.grid(row=1,column=0,padx=10,pady=20)
            



def renderQuestion():
    global index
    if(index>len(selectedQuestion)-1):
        checkAns()
        return
    destroyWidgets()
    tempFrame=customtkinter.CTkFrame(master=app)
    tempFrame.grid(row=1,column=0)
    currentWidgets.append(tempFrame)
    q=customtkinter.CTkLabel(text=f"Question {index+1}: {selectedQuestion[index]["q"]}",master=tempFrame,font=customtkinter.CTkFont(size=15))
    q.grid(row=0,column=0,padx=50,pady=20)
    for i,ans in enumerate(selectedQuestion[index]["a"]):
        selectBtn=customtkinter.CTkButton(text=f"{ans}",master=tempFrame,width=100,command=lambda ans=ans:choosenAnsFn(ans))
        selectBtn.grid(row=i+1,column=0,pady=5)
    index+=1
    paginationFrame=customtkinter.CTkFrame(master=tempFrame)
    paginationFrame.grid(row=6,column=0,pady=10)
    exitBtn=customtkinter.CTkButton(master=paginationFrame,text="exit",command=exitFn)
    exitBtn.grid(row=0,column=0,padx=30,pady=10)

    submitBtn=customtkinter.CTkButton(text="submit",master=paginationFrame,command=checkAns)
    submitBtn.grid(row=0,column=1,padx=30,pady=10)


def renderQuestions(subject):
    allQ=data[subject]
    selectedQuestion.extend(getRandomQ(allQ))
    for q in selectedQuestion:
        correctAns.append(q["c"])
    renderQuestion()


def renderChoices():
    for widget in currentWidgets:
        widget.destroy()
    tempFrame=customtkinter.CTkFrame(master=app,corner_radius=10)
    tempFrame.grid(padx=30,pady=20,row=1,column=0)
    currentWidgets.append(tempFrame)
    for i,subject in enumerate(subjects):
        choiceFrame=customtkinter.CTkFrame(master=tempFrame,corner_radius=20)
        nameFont=customtkinter.CTkFont(size=30)
        name=customtkinter.CTkLabel(text=subject.upper(),master=choiceFrame,font=nameFont)
        name.grid(row=0,column=0,padx=10,pady=5)
        startBtn=customtkinter.CTkButton(master=choiceFrame,text="Start quiz",command=lambda subject=subject:renderQuestions(subject))
        startBtn.grid(row=1,column=0,padx=10,pady=20)
        choiceFrame.grid(row=i%2,column=i%3,padx=20,pady=20)
    
    f=open("data.json")
    fileData=json.load(f)
    global data
    data=fileData
    f.close()


def renderInputName():
    


renderChoices()

app.mainloop()

