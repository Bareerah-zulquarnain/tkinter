from Tkinter import*
window = TK()
window.title('Tkinter Sample Window')
window.geomatery('300x300')

greeting = label(text="hello user" fg ="black" bg="white")
button = button(text = "click me "fg ="white" bg="black")
entry = entry(fg ="white" bg="black"withd=50)
greeting.pack()
button.pack()
entry.pack()

frame = frame(master=window , relief = RAISED ,boderwith =5 )
frame.pack()
label = labe(master = frame , text = sample frame)
label.pack()

textbox = text(fg ="black" bg="white")
textbox.pack()