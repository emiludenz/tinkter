import tkinter as tk

def main():

	win = tk.Tk()

	# Major Change
	lableName = tk.Label(text="Heello")
	lableName.grid(row=0,column=0)

	win.mainloop()

if __name__ == "__main__":
	main()
