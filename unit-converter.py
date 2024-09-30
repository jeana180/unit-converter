import tkinter as tk
from tkinter import ttk

def convert_units():
    try:
        input_value = float(input_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        
        # Conversion factors (simplified for demonstration)
        conversions = {
            'meters': {'feet': 3.28084, 'inches': 39.3701},
            'feet': {'meters': 0.3048, 'inches': 12},
            'inches': {'meters': 0.0254, 'feet': 1/12}
        }
        
        if from_unit == to_unit:
            result = input_value
        else:
            result = input_value * conversions[from_unit][to_unit]
        
        result_label.config(text=f"Result: {result:.4f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")
    except KeyError:
        result_label.config(text="Conversion not supported.")

# Create main window
root = tk.Tk()
root.title("Unit Converter")

# Create and place widgets
input_label = ttk.Label(root, text="Enter value:")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = ttk.Entry(root)
input_entry.grid(row=0, column=1, padx=5, pady=5)

from_unit_label = ttk.Label(root, text="From unit:")
from_unit_label.grid(row=1, column=0, padx=5, pady=5)

from_unit_var = tk.StringVar()
from_unit_combo = ttk.Combobox(root, textvariable=from_unit_var, values=['meters', 'feet', 'inches'])
from_unit_combo.grid(row=1, column=1, padx=5, pady=5)
from_unit_combo.set('meters')

to_unit_label = ttk.Label(root, text="To unit:")
to_unit_label.grid(row=2, column=0, padx=5, pady=5)

to_unit_var = tk.StringVar()
to_unit_combo = ttk.Combobox(root, textvariable=to_unit_var, values=['meters', 'feet', 'inches'])
to_unit_combo.grid(row=2, column=1, padx=5, pady=5)
to_unit_combo.set('feet')

convert_button = ttk.Button(root, text="Convert", command=convert_units)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = ttk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
