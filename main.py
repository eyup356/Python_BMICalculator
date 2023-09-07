from tkinter import *

def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height) / 100
        bmi = weight / (height ** 2)
        return bmi
    except ValueError:
        return None

def evaluate_bmi(bmi):
    if bmi is None:
        return "Error: Please enter valid numeric values"
    elif bmi < 18.5:
        return f"Body Mass Index (BMI): {bmi:.2f} - Underweight"
    elif 18.5 <= bmi < 24.9:
        return f"Body Mass Index (BMI): {bmi:.2f} - Normal Weight"
    elif 25 <= bmi < 29.9:
        return f"Body Mass Index (BMI): {bmi:.2f} - Overweight"
    else:
        return f"Body Mass Index (BMI): {bmi:.2f} - Obesity"

def button_clicked():
    weight = entry.get()
    height = entry2.get()

    bmi = calculate_bmi(weight, height)
    result_text = evaluate_bmi(bmi)
    result_label.config(text=result_text, fg="black")

window = Tk()
window.title("Body Mass Index Calculator")
window.minsize(width=300, height=300)
window.config(padx=10, pady=30)

label = Label(text="Enter Your Weight (kg)")
label.config(padx=10, pady=5)
label.pack()
entry = Entry(width=20)
entry.pack()

label2 = Label(text="Enter Your Height (cm)")
label2.config(padx=10, pady=5)
label2.pack()
entry2 = Entry(width=20)
entry2.pack()

result_label = Label(text="", fg="black")
result_label.config(pady=10)
result_label.pack()

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.config(padx=5, pady=5)
calculate_button.pack()

window.mainloop()
