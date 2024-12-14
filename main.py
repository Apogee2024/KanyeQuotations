from tkinter import *
import requests
URL = "https://api.kanye.rest/"





window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=" I'm thinking...", width=250, font=("Arial", 12, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
def get_quote():
    response = requests.get(url=URL)
    response.raise_for_status()
    response = response.json()
    quotation = response['quote']
    canvas.itemconfig(quote_text, text=quotation)



kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()