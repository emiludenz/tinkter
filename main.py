import tkinter as tk

def main():

	
	win = tk.Tk()
<<<<<<< HEAD
	win.title("Welcome")
	win.geometry("500x300")

	# Functions
	def disp_name():
		name = str(ent1.get())
		txt = tk.Text(master=win, height=20,width=25)
		txt.grid(column=0,row=1, columnspan=2)
		txt.insert(tk.END, name)

	# Labels
	lb1 = tk.Label(text="Give me a name")
	lb1.grid(column=0,row=0)

	# Entry
	ent1 = tk.Entry()
	ent1.grid(column=1,row=0)

	# Button
	btn = tk.Button(text="Push Me",command=disp_name)
	btn.grid(column=2,row=0)




=======

	# Major Change
	lableName = tk.Label(text="Heello")
	lableName.grid(row=0,column=0)
>>>>>>> refs/remotes/origin/master

	win.mainloop()



if __name__ == "__main__":
	main()
