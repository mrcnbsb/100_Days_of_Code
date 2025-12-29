import tkinter as tk

def miles_to_km_converter():
    miles = float(miles_input.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f}")

#Creating a new window and configurations
window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=50)
window.config(padx=20, pady=20) # distância da borda

# Labels
miles_label = tk.Label(text="Miles", font=("Arial", 15, "bold"))
miles_label.grid(column=2, row=0)

is_equal_to_label = tk.Label(text="is equal to", font=("Arial", 15, "bold"))
is_equal_to_label.grid(column=0, row=1)

km_label = tk.Label(text="Km", font=("Arial", 15, "bold"))
km_label.grid(column=2, row=1)

result_label = tk.Label(text="0", font=("Arial", 15, "bold"))
result_label.grid(column=1, row=1)

# Buttons
calculate_button = tk.Button(text="Calculate", command=miles_to_km_converter, font=("Arial", 10, "bold"))
calculate_button.grid(column=1, row=2)

# Entry
miles_input = tk.Entry(width=10, font=("Arial", 15, "bold"))
miles_input.insert(tk.END, string="0")
miles_input.grid(column=1, row=0)



# sempre no final
window.mainloop()

