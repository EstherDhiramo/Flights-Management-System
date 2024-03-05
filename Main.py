
import tkinter as tk
import datetime
admin={"samrit":"samrit","nimral":"nimral",'admin':'admin'}
supervis={"samrit1":"samrit1","nimral1":"nimral1",'supervis':'supervis'}
standard={"samrit2":"samrit2","nimral2":"nimral2",'standard':'standard'}
scheduled={'MH370':["10:10",'Delhi',"Delayed"],'KI784':['1:20','Pune','Delayed'],'PH169':['12:20','Seattle','Scheduled'],'BH234':['15:20','Bangalore','Scheduled'],'PH234':['15:00','Prayagraj','Delayed'],'BT452':['18:30','Malaysia','Scheduled'],'KR234':['15:20','Cuba','Scheduled']}
cancelled={'AI169':["11:30","Bombay","Cancelled"]}
def reminder():    #This is the reminder function, takes current time from the system and compares it to the list of flights, if the time is greater it creates a pop up with the flight number
    now=datetime.datetime.now()    
    for i in scheduled:
        l=scheduled[i][0].split(":")
        time=now.replace(hour=int(l[0]),minute=int(l[1]),second=0,microsecond=0)        
        if now>time:
            remindersc=tk.Tk()
            remindersc.title("Reminder!")
            tk.Label(master=remindersc,text="Flight Number "+i+" Not Updated").grid(row=0,column=0)
            remindersc.mainloop()
