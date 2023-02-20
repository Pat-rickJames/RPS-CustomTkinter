from customtkinter import *
from tkinter import *
from random import choice
from time import sleep

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class App(CTk):
        
    def __init__(self):
        super().__init__()
        self.pscore = 0
        self.cscore = 0
        self.geometry("600x300")
        self.title("RPS")

        self.textbox = CTkTextbox(self,width=400,height=40, font=CTkFont(size=20, weight="bold"))
        self.textbox.grid(padx=(100,0),pady=(30,0),sticky='nsew')

        self.lebel = CTkLabel(self, text=f"Score\n{self.pscore}\t\t\t{self.cscore}", font=CTkFont(size=20, weight="bold"))
        self.lebel.grid(padx=(100,0),pady=(22,0))

        self.butt = CTkButton(master=self,fg_color="black", text="START", text_color="silver", command=self.start)
        self.butt.place(relx=0.5,rely=0.7,anchor=CENTER)

        self.butt1 = CTkButton(master=self,fg_color="black", text="ROCK", text_color="silver", command=self.butt1, state="disabled")
        self.butt1.place(relx=0.2,rely=0.9,anchor=CENTER)

        self.butt2 = CTkButton(master=self,fg_color="black", text="PAPER", text_color="silver", command=self.butt2, state="disabled")
        self.butt2.place(relx=0.5,rely=0.9,anchor=CENTER)

        self.butt3 = CTkButton(master=self,fg_color="black", text="SCISSORS", text_color="silver", command=self.butt3, state="disabled")
        self.butt3.place(relx=0.8,rely=0.9,anchor=CENTER)

    def start(self):
        self.butt.destroy()
        self.geometry("600x230")
        self.butt1.configure(state="normal")
        self.butt1.place(relx=0.2,rely=0.8,anchor=CENTER)
        self.butt2.configure(state="normal")
        self.butt2.place(relx=0.5,rely=0.8,anchor=CENTER)
        self.butt3.configure(state="normal")
        self.butt3.place(relx=0.8,rely=0.8,anchor=CENTER)

    def check_winner(self, comp):
        
        text = self.textbox.get("0.0", "end").strip()
        self.textbox.delete("0.0","end")

        if text == "ROCK" and comp == "SCISSORS":
            self.textbox.insert("0.0", "\t          YOU WIN!")
            self.pscore+=1
        elif text == "PAPER" and comp == "ROCK":
            self.textbox.insert("0.0", "\t          YOU WIN!")
            self.pscore+=1
        elif text == "SCISSORS" and comp == "PAPER":
            self.textbox.insert("0.0", "\t          YOU WIN!")
            self.pscore+=1
        elif text == comp:
            self.textbox.insert("0.0", "\t              TIE!")
        else:
            self.textbox.insert("0.0", "\t          YOU LOSE!")
            self.cscore+=1

        self.lebel.configure(text=f"Score\n{self.pscore}\t\t\t{self.cscore}")

        self.butt1.configure(state="normal")
        self.butt2.configure(state="normal")
        self.butt3.configure(state="normal")
        
    def butt1(self):
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0", "\t              ROCK")
        self.butt1.configure(state="disabled")
        self.butt2.configure(state="disabled")
        self.butt3.configure(state="disabled")
        comp = choice(("ROCK", "PAPER", "SCISSORS"))
        print(comp)
        self.check_winner(comp)

    def butt2(self):
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0", "\t              PAPER")
        self.butt1.configure(state="disabled")
        self.butt2.configure(state="disabled")
        self.butt3.configure(state="disabled")
        comp = choice(("ROCK", "PAPER", "SCISSORS"))
        print(comp)
        self.check_winner(comp)

    def butt3(self):
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0", "\t              SCISSORS")
        self.butt1.configure(state="disabled")
        self.butt2.configure(state="disabled")
        self.butt3.configure(state="disabled")
        comp = choice(("ROCK", "PAPER", "SCISSORS"))
        print(comp)
        self.check_winner(comp)

if __name__ == "__main__":
    app = App()
    app.mainloop()


    
