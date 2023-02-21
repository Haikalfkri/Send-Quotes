from tkinter import *
import smtplib
import random



BACKGROUND = "#2596BE"
MY_EMAIL = "your email"
PASSWORD = "your password this is the app password of your email"
RECEIVER = "other email or your email"
current_quotes = []

with open("quotes.txt") as quotes_file:
    content = quotes_file.readlines()
    quotes = [quotes.rstrip() for quotes in content]

def next_word():
    global current_quotes
    current_quotes = random.choice(quotes)
    canvas.itemconfig(word_text, text=current_quotes, fill="black")

def send_quotes():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, RECEIVER, msg=f"Subject:Quotes Of the Day\n\n{current_quotes}")

window = Tk()
window.title("Send Quotes")
window.config(padx=50, pady=50, bg=BACKGROUND)


canvas = Canvas(width=800, height=526, bg=BACKGROUND, highlightthickness=0)
back_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=back_img)
canvas.create_text(400, 150, text="Quotes", font=("Ariel", 20, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 14, "normal"))
canvas.grid(column=0, row=0, columnspan=2)

#Button
next_button = Button(text="Next", width=8, command=next_word)
next_button.grid(column=0, row=1)

send_button = Button(text="Send", width=8, command=send_quotes)
send_button.grid(column=1, row=1)

next_word()

window.mainloop()