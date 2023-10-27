import tkinter as tk
from tkinter import ttk

def calculate_calories():
    age = int(age_entry.get())
    gender = gender_var.get()
    weight_kg = float(weight_entry.get())
    height_cm = float(height_entry.get())
    activity_level = activity_var.get()

    if gender == "Male":
        bmr = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    elif gender == "Female":
        bmr = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    else:
        result_label.config(text="Invalid gender")
        return

    activity_factors = {
        "Sedentary": 1.2,
        "Lightly active": 1.375,
        "Moderately active": 1.55,
        "Very active": 1.725,
        "Super active": 1.9
    }

    if activity_level in activity_factors:
        calories = bmr * activity_factors[activity_level]
        result_label.config(text=f"Your estimated daily calorie needs are {calories:.2f} calories.")
    else:
        result_label.config(text="Invalid activity level")

app = tk.Tk()
app.title("Calorie Calculator")

age_label = ttk.Label(app, text="Age:")
age_entry = ttk.Entry(app)

gender_label = ttk.Label(app, text="Gender:")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(app, textvariable=gender_var, values=["Male", "Female"])

weight_label = ttk.Label(app, text="Weight (kg):")
weight_entry = ttk.Entry(app)

height_label = ttk.Label(app, text="Height (cm):")
height_entry = ttk.Entry(app)

activity_label = ttk.Label(app, text="Activity Level:")
activity_var = tk.StringVar()
activity_combobox = ttk.Combobox(app, textvariable=activity_var,
    values=["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])

calculate_button = ttk.Button(app, text="Calculate Calories", command=calculate_calories)
result_label = ttk.Label(app, text="")

age_label.pack()
age_entry.pack()
gender_label.pack()
gender_combobox.pack()
weight_label.pack()
weight_entry.pack()
height_label.pack()
height_entry.pack()
activity_label.pack()
activity_combobox.pack()
calculate_button.pack()
result_label.pack()

app.mainloop()