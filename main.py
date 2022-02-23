from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import time
from plyer import notification
from threading import *


class Student:
    def __init__(self, root):
        # ==> Main Body of Root and Title <==
        self.root = root
        self.flag = False
        self.flag_another = False
        self.Sub = False
        self.Name = ""
        self.Weight = 0
        self.root.title("Water Reminder System")
        self.root.geometry("500x500+0+0")
        self.root.resizable(0, 0)
        root.wm_iconbitmap('.\water.ico')
        title = Label(self.root, text="Welcome to Water Reminder !!", bd=10, relief=SOLID,
                      font=("Times New Roman", 25, "bold"), bg="#404040", fg="White")
        title.pack(side=TOP, fill=X)

        Management_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#333945")
        Management_Frame.place(x=20, y=85, width=455, height=388)

        m_title = Label(Management_Frame, text='"Drink Water as much as you can !!"',
                        font=("Times New Roman", 20, "bold"), bg="#758AA2", fg="black")
        m_title.grid(row=0, column=0, pady=0, padx=2)

        # ====> Button Section <====
        Label(Management_Frame, text="Click on This Button", font=("Arial", 15, "bold"),
              bg="#333945", fg="white").grid(row=1, column=0)

        Submit_btn = Button(Management_Frame, command=self.SubmitBTN, text="Enter Name and Weight", width=20, bd=4,
                            relief=SOLID, font=("Arial", 15, "bold"), bg="#ff9933", fg="Black")
        Submit_btn.grid(row=4, column=0, pady=10, padx=45)

        Start_Reminder = Button(Management_Frame, command=self.StartBTN, text="Start Reminder", width=20, bd=4,
                                relief=SOLID, font=("Arial", 20, "bold"), bg="#ff9933", fg="Black")
        Start_Reminder.grid(row=5, column=0, pady=35, padx=45)

        Stop_Reminder = Button(Management_Frame, command=self.StopBTN, text="Stop Reminder", width=20, bd=4,
                               relief=SOLID, font=("Arial", 20, "bold"), bg="#ff9933", fg="Black")
        Stop_Reminder.grid(row=6, column=0, pady=10, padx=45)

    def SubmitBTN(self):
        try:
            self.Name = simpledialog.askstring("Enter Name", "What is your Name?")
        except ValueError:
            messagebox.showerror("Error", "Name Must be Text")
        try:
            self.Weight = int(simpledialog.askstring("Enter Weight", "What is your Weight?"))
        except ValueError:
            messagebox.showerror("Error", "Weight Must be Value")

        if self.Name == "" or self.Name == " ":
            messagebox.showerror("Invalid Name", " Invalid Name, Please Enter Again !!!")
            self.Name = ""
        elif self.Weight <= 0 or self.Weight == " " or len(str(self.Weight)) == 0:
            messagebox.showerror("Invalid Weight", " Invalid Weight, Please Enter Again !!!")
            self.Weight = 0
        else:
            Final_Name = "Your Name is " + self.Name + ", And Weight " + str(self.Weight) + ", Right?"
            messagebox.showinfo("Conformation", Final_Name)

    def StopBTN(self):
        self.flag = False

    def StartBTN(self):

        if self.Name == "":
            self.flag_another = False
            messagebox.showerror("Something went Wrong ",
                                 "Please Provide Details Click on Name And Weight Button !!!")
        elif self.Weight == 0:
            self.flag_another = False
            messagebox.showerror("Something went Wrong ", "Please Provide Details Click on Name And Weight Button !!!")
        else:
            if self.flag == False:
                self.flag = True
                thread = Thread(target=self.StartNotify)
                thread.start()
            elif self.flag_another == False:
                messagebox.showerror("Something went Wrong ",
                                     "Please Provide Details Click on Name And Weight Button !!!")
            else:
                messagebox.showwarning("Activated", "Notification Already Activated")

    def StartNotify(self):

        if __name__ == "__main__":
            self.flag_another = True
            while self.flag:
                notification.notify(
                    title="Hey " + self.Name + ", Please Drink A Glass of Water Now !!",
                    message="Now, It's time to drink Water because It's Require as per your Weight...",
                    app_icon=".\water.ico",
                    timeout=3
                )
                if self.Weight <= 30:
                    time.sleep(90 * 50)
                elif self.Weight <= 40:
                    time.sleep(60 * 60)
                elif self.Weight <= 50:
                    time.sleep(50 * 60)
                elif self.Weight <= 60:
                    time.sleep(45 * 60)
                elif self.Weight <= 70:
                    time.sleep(40 * 60)
                elif self.Weight <= 80:
                    time.sleep(35 * 60)
                elif self.Weight <= 90:
                    time.sleep(30 * 60)
                elif self.Weight > 90:
                    time.sleep(30 * 60)
                else:
                    time.sleep(30 * 60)


root = Tk()
ob = Student(root)
root.mainloop()
