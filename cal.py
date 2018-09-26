from tkinter import *
import time
calculator = Tk()
calculator.title("Calculator")
class App(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.createwidgets()
	def replace(self,text):
		self.display.delete(0,END)
		self.display.insert(0,text)
	def addtodisplay(self,text):
		if(self.display.get()=="0" and (text=="*" or text=="/" or text=="%")):
			self.display.insert(1,text)
		elif(self.display.get()=="0"):	
			self.replace(text)
		else:
			self.display.insert(len(self.display.get()),text)
	def calculate(self):
		self.expression=self.display.get()
		self.expression=self.expression.replace("%","/100")
		self.replace(eval(self.expression))
	def clearscr(self):
		self.replace("0")
	def negative(self):
		self.neg= -1*int(eval(self.display.get()))
		self.replace(str(self.neg))
	def createwidgets(self):
		self.display=Entry(self, width=18, font=("Arial", 18), justify=RIGHT, borderwidth=0, highlightcolor='white')
		self.display.insert(0, "0")
		self.display.grid(row=0, column=0, columnspan=4, pady=5)
		self.clear=Button(self, text="C", width=6, height=2, command=lambda: self.clearscr()).grid(row=1, column=0)
		self.plusminus=Button(self, text="+/-", width=6, height=2, command=lambda: self.negative()).grid(row=1, column=1)
		self.percent=Button(self, text="%", width=6, height=2, command=lambda: self.addtodisplay("%")).grid(row=1, column=2)
		self.divide=Button(self, text="÷", width=6, height=2, command=lambda: self.addtodisplay("/")).grid(row=1, column=3)
		self.seven=Button(self, text="7", width=6, height=2, command=lambda: self.addtodisplay("7")).grid(row=2, column=0)
		self.eight=Button(self, text="8", width=6, height=2, command=lambda: self.addtodisplay("8")).grid(row=2, column=1)
		self.nine=Button(self, text="9", width=6, height=2, command=lambda: self.addtodisplay("9")).grid(row=2, column=2)
		self.multi=Button(self, text="x", width=6, height=2, command=lambda: self.addtodisplay("*")).grid(row=2, column=3)
		self.four=Button(self, text="4", width=6, height=2, command=lambda: self.addtodisplay("4")).grid(row=3, column=0)
		self.five=Button(self, text="5", width=6, height=2, command=lambda: self.addtodisplay("5")).grid(row=3, column=1)
		self.six=Button(self, text="6", width=6, height=2, command=lambda: self.addtodisplay("6")).grid(row=3, column=2)
		self.minus=Button(self, text="-", width=6, height=2, command=lambda: self.addtodisplay("-")).grid(row=3, column=3)
		self.one=Button(self, text="1", width=6, height=2, command=lambda: self.addtodisplay("1")).grid(row=4, column=0)
		self.two=Button(self, text="2", width=6, height=2, command=lambda: self.addtodisplay("2")).grid(row=4, column=1)
		self.three=Button(self, text="3", width=6, height=2, command=lambda: self.addtodisplay("3")).grid(row=4, column=2)
		self.plus=Button(self, text="+", width=6, height=2, command=lambda: self.addtodisplay("+")).grid(row=4, column=3)
		self.zero=Button(self, text="0", width=12, height=2, command=lambda: self.addtodisplay("0")).grid(row=5, column=0, columnspan=2)
		self.dot=Button(self, text=".", width=6, height=2, command=lambda: self.addtodisplay(".")).grid(row=5, column=2)
		self.equal=Button(self, text="=", width=6, height=2, command=lambda: self.calculate()).grid(row=5, column=3)

app=App(calculator)
app.grid()
calculator.mainloop()
