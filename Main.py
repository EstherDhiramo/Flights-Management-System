
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
deluser(): #This function is responsible for deleting users
    def deluserback():
        u=uname.get()        
        if not(u in admin or u in supervis or u in cancelled):
            popup=tk.Tk()
            popup.title("Username Not Found!")
            tk.Label(master=popup,text="Username not found! Please try again!").grid(row=1,column=1)
            
        else:
            if uname.get()=='admin':
                    re=tk.Tk()
                    re.title("Can't Delete Superuser!")
                    tk.Label(master=re,text="Cannot Delete Superuser!").grid(row=1,column=1)
                    re.mainloop()
            elif u in admin:
                if u!='admin':
                    del admin[u]
                    r1=tk.Tk()
                    r1.title("Success!")
                    tk.Label(master=r1,text="Admin User Successfully Deleted!").grid(row=1,column=1)
                    
 elif u in supervis:
                del supervis[u]
                r1=tk.Tk()
                r1.title("Success!")
                tk.Label(master=r1,text=" Supervisor Successfully Deleted!").grid(row=1,column=1)
            if u in standard:
                del standard[u]
                r1=tk.Tk()
                r1.title("Success!")
                tk.Label(master=r1,text="Standard User Successfully Deleted!").grid(row=1,column=1)                
    delusersc=tk.Tk()
    delusersc.title("Delete A User")
    tk.Label(master=delusersc,text="Enter the Username").grid(row=1,column=0)
    uname=tk.Entry(master=delusersc)
    unamne.grid(row=1,column=1)
    r2=tk.Button(master=delusersc,text="Confirm Deletion",width=25,command=deluserback).grid(row=1,column=2)
    
def manageuser():#this function is responsible for adding users
    def adduser():
        def addadmin():
            def adminusname():
                def adminuserback():
                    p=passw.get()                                                             
                    admin[u]=p
                    popup=tk.Tk()
                    popup.title("Success")
                    tk.Label(master=popup,text="Admin Successfully Added!").grid(row=1,column=1)
                u=usname.get()
                if u in admin or u in supervis or u in standard:
                        popup=tk.Tk()
                        popup.title("Username Already Exists!")
                        tk.Label(master=popup,text="Username Already Exists! Please Try Again").grid(row=1,column=1)
                        manageusersc.destroy()
                        aa.destroy()
                    
                
