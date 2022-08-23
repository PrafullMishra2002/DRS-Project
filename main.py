import tkinter #gui(graphical user interface for desktop based applications)
from tkinter import messagebox
import cv2  #real time image processing
import win32com.client as wincl  #text to speach
import PIL.Image, PIL.ImageTk #python image library
from functools import partial
import threading
import imutils #image processing function 
import time


root =tkinter.Tk()
SET_WIDTH = 830
SET_HEIGHT = 600
root.geometry("830x600")
root.maxsize(900,700)
root.title("Cricket Decision review System")

var=tkinter.IntVar()
var.set(11)
stream = cv2.VideoCapture("Lbw.mp4")
stream1 = cv2.VideoCapture("runout.mp4")
stream2 = cv2.VideoCapture("stump.mp4")
stream4 = cv2.VideoCapture("catch.mp4")
def help():
    messagebox.showinfo("How to use this application","First click on any of the options you want to check ")
with open("facts.txt","a") as f:
    f.write("1. The first cricket ball was made of wool.\n\n2. The longest cricket match was 14 days long.\n\n3. Cricket bats are made from white willow.\n\n4. Alec Stewart was one of the best England cricket players of all time.\n\n5.  Mahela Jayawardene is the only batsman to have scored centuries in both the Semi-Final and Final of a World Cup.\n\n 6. Inzamam Ul Haq took a wicket off the very first ball he bowled in International Cricket.\n\n7. Sachin Tendulkar got out for a duck only once in his Ranji career. Bhuvaneshwar Kumar got him.\n\n8. Saeed Ajmal has never won a Man of the Match award in One Day International Cricket.\n\n9. A cricket ball must measure exactly 163g (5.75oz).\n\n10. Cricket started with two stumps, not three.\n\n11. 111 is said to be an unlucky score.\n\12.The best place to watch cricket live, is at Lord’s in London.")
    


def submit():
    def facts():
         messagebox.showinfo("Some of the intresting facts in Cricket","1. The first cricket ball was made of wool.\n\n2. The longest cricket match was 14 days long.\n\n3. Cricket bats are made from white willow.\n\n4. Alec Stewart was one of the best England cricket players of all time.\n\n5.  Mahela Jayawardene is the only batsman to have scored centuries in both the Semi-Final and Final of a World Cup.\n\n 6. Inzamam Ul Haq took a wicket off the very first ball he bowled in International Cricket.\n\n7. Sachin Tendulkar got out for a duck only once in his Ranji career. Bhuvaneshwar Kumar got him.\n\n8. Saeed Ajmal has never won a Man of the Match award in One Day International Cricket.\n\n9. A cricket ball must measure exactly 163g (5.75oz).\n\n10. Cricket started with two stumps, not three.\n\n11. 111 is said to be an unlucky score.\n\n12. The best place to watch cricket live, is at Lord’s in London.")
        
    
    def play(speed):
        if var.get()==1:
            print(f"you clicked on out.speed is{speed}")
            frame = stream.get(cv2.CAP_PROP_POS_FRAMES)
            stream.set(cv2.CAP_PROP_POS_FRAMES, frame + speed)
            grabbed,frame=stream.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0,0, image=frame, anchor=tkinter.NW)
        elif var.get()==2:  
            print(f"you clicked on out.speed is{speed}")
            frame1 = stream1.get(cv2.CAP_PROP_POS_FRAMES)
            stream1.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed,frame=stream1.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0,0, image=frame, anchor=tkinter.NW)
        elif var.get()==3:  
            print(f"you clicked on out.speed is{speed}")
            frame1 = stream2.get(cv2.CAP_PROP_POS_FRAMES)
            stream2.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed,frame=stream2.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0,0, image=frame, anchor=tkinter.NW)
        elif var.get()==4:  
            print(f"you clicked on out.speed is{speed}")
            frame1 = stream4.get(cv2.CAP_PROP_POS_FRAMES)
            stream4.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
            grabbed,frame=stream4.read()
            frame = imutils.resize(frame, width=900, height=SET_HEIGHT)
            frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            cv.image = frame
            cv.create_image(0,0, image=frame, anchor=tkinter.NW)
    def pending(decision):
        frame = cv2.cvtColor(cv2.imread("pending.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=730, height=400)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        cv.image = frame
        cv.create_image(0,0, image=frame, anchor=tkinter.NW)
        #waiting for 1 seccond
        time.sleep(1)
        
        frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=730, height=400)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        cv.image = frame
        cv.create_image(0,0, image=frame, anchor=tkinter.NW)
        time.sleep(1)
        #display out or not out image
        if decision=="out":
           
            decisionImg="out.png"
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("Decision has been made and the player is out")
        else:
            decisionImg="notout.png"
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("Decision has been made and the player is not out")
            
        frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
        frame = imutils.resize(frame, width=730, height=400)
        frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
        cv.image = frame
        cv.create_image(0,0, image=frame, anchor=tkinter.NW)
        
        
    def out():
        thread = threading.Thread(target=pending, args=("out",))
        thread.daemon = 1
        thread.start()
        print("Player is out")
    def not_out():
        thread=threading.Thread(target=pending,args=("not out",))
        thread.daemon=1
        thread.start()
        print("player is not out")

# Tkinter gui starts here
    window = tkinter.Toplevel()
    window.geometry("730x730")
    window.title("Cricket DRS")
    window.maxsize(830,830)
    window.configure(bg="light blue")
    cv=tkinter.Canvas(window,height=400,width=730,bg="black",bd=0)
    img=PIL.ImageTk.PhotoImage(file="wel.png")
    cv.create_image(0,0,anchor=tkinter.NW,image=img)
    cv.place(x=0,y=0)
    
    if var.get()==1:
        print("LBW")
        btn = tkinter.Button(window, text="<< Previous (fast)",bg="DarkOliveGreen2" ,command=partial(play, -15),font="verdana 13 bold",width=35)
        btn.place(x=150,y=420)

        btn = tkinter.Button(window, text="<< Previous (slow)",bg="DarkOliveGreen2" ,command=partial(play, -2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=465)

        btn = tkinter.Button(window, text="Next (slow) >>",bg="DarkOliveGreen2" ,command=partial(play, 2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=510)

        btn = tkinter.Button(window, text="Next (fast) >>",bg="DarkOliveGreen2" ,command=partial(play, 25),font="verdana 13 bold",width=35)
        btn.place(x=150,y=555)

        btn = tkinter.Button(window, text="Give Out",command=out,bg="Red" ,font="verdana 13 bold",width=35)
        btn.place(x=150,y=600)


        btn = tkinter.Button(window, text="Give Not Out",bg="Green2" ,command=not_out,font="verdana 13 bold",width=35)
        btn.place(x=150,y=645)
        btn = tkinter.Button(window, text="Intresting Facts", command=facts,bg="chocolate1" ,padx=5,pady=7)
        btn.place(x=600,y=640)
        
        window.mainloop()
        
        
    elif var.get()==2:
        print("Run Out")
        btn = tkinter.Button(window, text="<< Previous (fast)",bg="DarkOliveGreen2" ,command=partial(play, -15),font="verdana 13 bold",width=35)
        btn.place(x=150,y=420)

        btn = tkinter.Button(window, text="<< Previous (slow)",bg="DarkOliveGreen2" ,command=partial(play, -2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=465)

        btn = tkinter.Button(window, text="Next (slow) >>",bg="DarkOliveGreen2" ,command=partial(play, 2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=510)

        btn = tkinter.Button(window, text="Next (fast) >>",bg="DarkOliveGreen2" ,command=partial(play, 25),font="verdana 13 bold",width=35)
        btn.place(x=150,y=555)

        btn = tkinter.Button(window, text="Give Out",command=out,bg="Red" ,font="verdana 13 bold",width=35)
        btn.place(x=150,y=600)


        btn = tkinter.Button(window, text="Give Not Out",bg="Green2" ,command=not_out,font="verdana 13 bold",width=35)
        btn.place(x=150,y=645)
        btn = tkinter.Button(window, text="Intresting Facts", command=facts,bg="chocolate1" ,padx=5,pady=7)
        btn.place(x=600,y=640)
        
        window.mainloop()
    elif var.get()==3:
        print("Stump Out")
        btn = tkinter.Button(window, text="<< Previous (fast)",bg="DarkOliveGreen2" ,command=partial(play, -15),font="verdana 13 bold",width=35)
        btn.place(x=150,y=420)

        btn = tkinter.Button(window, text="<< Previous (slow)",bg="DarkOliveGreen2" ,command=partial(play, -2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=465)

        btn = tkinter.Button(window, text="Next (slow) >>",bg="DarkOliveGreen2" ,command=partial(play, 2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=510)

        btn = tkinter.Button(window, text="Next (fast) >>",bg="DarkOliveGreen2" ,command=partial(play, 25),font="verdana 13 bold",width=35)
        btn.place(x=150,y=555)

        btn = tkinter.Button(window, text="Give Out",command=out,bg="Red" ,font="verdana 13 bold",width=35)
        btn.place(x=150,y=600)


        btn = tkinter.Button(window, text="Give Not Out",bg="Green2" ,command=not_out,font="verdana 13 bold",width=35)
        btn.place(x=150,y=645)
        btn = tkinter.Button(window, text="Intresting Facts", command=facts,bg="chocolate1" ,padx=5,pady=7)
        btn.place(x=600,y=640)
        
        window.mainloop()
        
    elif var.get()==4:
        print("Low Catch")
        btn = tkinter.Button(window, text="<< Previous (fast)",bg="DarkOliveGreen2" ,command=partial(play, -15),font="verdana 13 bold",width=35)
        btn.place(x=150,y=420)

        btn = tkinter.Button(window, text="<< Previous (slow)",bg="DarkOliveGreen2" ,command=partial(play, -2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=465)

        btn = tkinter.Button(window, text="Next (slow) >>",bg="DarkOliveGreen2" ,command=partial(play, 2),font="verdana 13 bold",width=35)
        btn.place(x=150,y=510)

        btn = tkinter.Button(window, text="Next (fast) >>",bg="DarkOliveGreen2" ,command=partial(play, 25),font="verdana 13 bold",width=35)
        btn.place(x=150,y=555)

        btn = tkinter.Button(window, text="Give Out",command=out,bg="Red" ,font="verdana 13 bold",width=35)
        btn.place(x=150,y=600)


        btn = tkinter.Button(window, text="Give Not Out",bg="Green2" ,command=not_out,font="verdana 13 bold",width=35)
        btn.place(x=150,y=645)
        btn = tkinter.Button(window, text="Intresting Facts", command=facts,bg="chocolate1" ,padx=5,pady=7)
        btn.place(x=600,y=640)
        
        window.mainloop()
        


# var = IntVar()
var.set(11)
c=tkinter.Canvas(root,height=600,width=830,bg="black",bd=0)
img=PIL.ImageTk.PhotoImage(file="main.png")
c.create_image(0,0,anchor=tkinter.NW,image=img)
c.place(x=0,y=0)

tkinter.Label(root, text = "What do you wanna check?",bg="white",font="corba 19 bold", padx=14).place(x=250,y=80)
tkinter.Radiobutton(root, text="LBW", padx=14, variable=var, value=1,font="sanserif 13 bold").place(x=350,y=130)
tkinter.Radiobutton(root, text="Run out", padx=14, variable=var, value=2,font="sanserif 13 bold").place(x=350,y=180)
tkinter.Radiobutton(root, text="Stump out", padx=14, variable=var, value=3,font="sanserif 13 bold").place(x=350,y=230)
tkinter.Radiobutton(root, text="Low Catch", padx=14, variable=var, value=4,font="sanserif 13 bold").place(x=350,y=280)
tkinter.Button(text="Check Now", command=submit,activebackground='green', highlightcolor='yellow', bd=3, bg='black', fg='white', font=('Megrim', 20, 'bold'), relief='raised',height=1, width=15).place(x=300,y=370)
tkinter.Button(text="Exit",command=root.destroy,borderwidth=5,padx=15,pady=10,bg = "red",fg="black").place(x=13,y=500)
root.mainloop()

