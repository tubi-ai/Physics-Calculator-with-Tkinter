import tkinter as tk
from tkinter import ttk

# Global variables
current_number = ""
active_entry = None  # Active Entry (to track which Entry data was entered into)
label_result = None

# Number adding function when clicking the button
def button_click(symbol):
    global current_number
    if symbol == 'delete':
        current_number = current_number[:-1]
    else:
        current_number += str(symbol)

    if active_entry is not None:
        active_entry.delete(0, tk.END)
        active_entry.insert(0, current_number)

# Active Entry selection function
def select_entry(entry):
    global current_number, active_entry
    current_number = ""  # We reset it for new entry every time
    active_entry = entry

# ButtonPad class to create a number pad
class ButtonPad(ttk.Frame):
    def __init__(self, app, parent, command_callback):
        super().__init__(parent)
        self.app = app  # Store reference to the CalculatorApp instance        
        self.command_callback = command_callback
        self.create_buttons()
                
    def create_buttons(self):
        # First row's buttons
        button_1 = ttk.Button(self, text='1', command=lambda: self.command_callback(1), takefocus=False)
        button_2 = ttk.Button(self, text='2', command=lambda: self.command_callback(2), takefocus=False)
        button_3 = ttk.Button(self, text='3', command=lambda: self.command_callback(3), takefocus=False)
        button_del = ttk.Button(self, text='delete', command=lambda: self.command_callback('delete'), takefocus=False)
        
        button_1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        button_2.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        button_3.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
        button_del.grid(row=0, column=3, sticky="nsew", padx=2, pady=2)
    
        # Second row's buttons
        button_4 = ttk.Button(self, text='4', command=lambda: self.command_callback(4), takefocus=False)
        button_5 = ttk.Button(self, text='5', command=lambda: self.command_callback(5), takefocus=False)
        button_6 = ttk.Button(self, text='6', command=lambda: self.command_callback(6), takefocus=False)
        button_eq = ttk.Button(self, text='=', command=lambda: self.command_callback('='), takefocus=False)
    
        button_4.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        button_5.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        button_6.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        button_eq.grid(row=1, column=3, sticky="nsew", padx=2, pady=2)
    
        # Third row's buttons
        button_7 = ttk.Button(self, text='7', command=lambda: self.command_callback(7), takefocus=False)
        button_8 = ttk.Button(self, text='8', command=lambda: self.command_callback(8), takefocus=False)
        button_9 = ttk.Button(self, text='9', command=lambda: self.command_callback(9), takefocus=False)
        button_dot = ttk.Button(self, text='.', command=lambda: self.command_callback('.'), takefocus=False)
    
        button_7.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        button_8.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        button_9.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        button_dot.grid(row=2, column=3, sticky="nsew", padx=2, pady=2)
    
        # Fourth row's button
        button_0 = ttk.Button(self, text='0', command=lambda: self.command_callback(0), takefocus=False)
        button_0.grid(row=3, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
    
        # Reset Button
        button_reset = ttk.Button(self, text='Reset', command=self.app.reset, takefocus=False)
        button_reset.grid(row=4, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        
    
        # Configure rows and columns to expand equally
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for j in range(5):
            self.grid_rowconfigure(j, weight=1)

class CalculatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.setup_notebook_and_tabs()
                
    def setup_notebook_and_tabs(self):
        # Setup notebook and tabs (move this part from __init__ for clarity)
        self.notebook = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Ohm's Law")
        self.notebook.add(self.tab2, text="Ampère's Law")
        self.notebook.add(self.tab3, text="Faraday's Law")
        self.notebook.pack(expand=True, fill='both')

        # Add ButtonPad to each tab, passing the parent app (self)
        button_pad1 = ButtonPad(self, self.tab1, self.button_click)
        button_pad2 = ButtonPad(self, self.tab2, self.button_click)
        button_pad3 = ButtonPad(self, self.tab3, self.button_click)

        button_pad1.pack(pady=10, padx=10, fill='x')
        button_pad2.pack(pady=10, padx=10, fill='x')
        button_pad3.pack(pady=10, padx=10, fill='x')
        
    def reset(self):
        """Reset all entries across tabs."""
        for entry in [self.entry_ohm, self.entry_volt, self.entry_current]:
            entry.config(state='normal')
            entry.delete(0, tk.END)
    
        self.label_result.config(text=' ')
        self.combobox_ohm.set("Voltage (V) & Resistance (R)")
        self.entry_volt.focus_set()
        
        # Number adding function when clicking the button
    def button_click(symbol):
        global current_number
        if symbol == 'delete':
            current_number = current_number[:-1]
        else:
            current_number += str(symbol)
    
        if active_entry is not None:
            active_entry.delete(0, tk.END)
            active_entry.insert(0, current_number)        
        
        ## Notebook widget'ını oluştur
        #self.notebook = ttk.Notebook(self)
        #self.notebook.pack(expand=True, fill='both')

        ## Sekme 1 ve Sekme 2'yi oluştur
        #self.tab1 = ttk.Frame(self.notebook)
        #self.tab2 = ttk.Frame(self.notebook)
        #self.tab3 = ttk.Frame(self.notebook)

        #self.notebook.add(self.tab1, text="Ohm's Law: V = I * R")
        #self.notebook.add(self.tab2, text="Ampère's Law: B = μ * I / (2 * π * r)")
        #self.notebook.add(self.tab3, text="Faraday's Law: E = - ΔΦ / Δt")
        
        ## Add ButtonPads to tabs
        #button_pad1 = ButtonPad(self, self.tab1, button_click)
        #button_pad1.pack(pady=10, padx=10, fill='x')
    
        #button_pad2 = ButtonPad(self, self.tab2, button_click)
        #button_pad2.pack(pady=10, padx=10, fill='x')
    
        #button_pad3 = ButtonPad(self, self.tab3, button_click)
        #button_pad3.pack(pady=10, padx=10, fill='x')
            
        self.combobox_ohm = ttk.Combobox(self.tab1, values=["Voltage (V) & Resistance (R)", "Voltage (V) & Current (I)", "Resistance (R) & Current (I)"])
        self.combobox_ohm.set("Voltage (V) & Resistance (R)")
        self.combobox_ohm.pack(fill='both')
        
        self.combobox_ohm = ttk.Combobox(self.tab2, values=["Magnetic Field (B) & Current (I)", "Radius (r) & Current (I)", "Magnetic Field (B) & Radius (r)"])
        self.combobox_ohm.set("Magnetic Field (B) & Current (I)")
        self.combobox_ohm.pack(fill='both')
        
        self.combobox_ohm = ttk.Combobox(self.tab3, values=["Electromotive Force EMK (E) & Magnetic Flux (ΔΦ)","Magnetic Flux (ΔΦ) & Time Interval (Δt)","Electromotive Force EMK (E) ve Time Interval (Δt)"])
        self.combobox_ohm.set("Electromotive Force EMK (E) & Magnetic Flux (ΔΦ)")
        self.combobox_ohm.pack(fill='both')
        
        # Entries for Tab1 
        self.entry_ohm = self.create_entry_with_label(self.tab1, 'R = ', 'Ω')
        self.entry_volt = self.create_entry_with_label(self.tab1, 'V = ', 'V')
        self.entry_current = self.create_entry_with_label(self.tab1, 'I = ', 'A')

        # Entries for Tab2
        self.entry_B = self.create_entry_with_label(self.tab2, 'B = ', 'T')
        self.entry_I = self.create_entry_with_label(self.tab2, 'I = ', 'A')
        self.entry_r = self.create_entry_with_label(self.tab2, 'r = ', 'm')
        self.entry_mu = self.create_entry_with_label(self.tab2, 'μ = ', 'H/m')

        # Entries for Tab3
        self.entry_df = self.create_entry_with_label(self.tab3, 'ΔΦ = ', 'Wb')
        self.entry_dt = self.create_entry_with_label(self.tab3, 'Δt = ', 's')
        self.entry_E = self.create_entry_with_label(self.tab3, 'E = ', 'V')
        
        # Add ButtonPads to tabs
        button_pad1 = ButtonPad(self, self.tab1, button_click)
        button_pad1.pack(pady=10, padx=10, fill='x')
    
        button_pad2 = ButtonPad(self, self.tab2, button_click)
        button_pad2.pack(pady=10, padx=10, fill='x')
    
        button_pad3 = ButtonPad(self, self.tab3, button_click)
        button_pad3.pack(pady=10, padx=10, fill='x')    
    
        # Reset entries for Tab 3
        self.entry_df.delete(0, tk.END)
        self.entry_dt.delete(0, tk.END)
        self.entry_E.delete(0, tk.END)
    
        # Reset the result label
        self.label_result.config(text='')
    
        # Optionally set focus to a specific entry
        self.entry_volt.focus_set()
        

        # "=" button
        equal_button = ttk.Button(self, text='=', command=self.calculate)
        equal_button.pack(pady=10)

        # Label to show results
        self.label_result = ttk.Label(self.tab1, text='')
        self.label_result.pack()

    def create_entry_with_label(self, parent, label_text, unit_text):
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text=label_text)
        entry = ttk.Entry(frame)
        unit_label = ttk.Label(frame, text=unit_text)

        label.pack(side='left', padx=5, pady=5)
        entry.pack(side='left', padx=5, pady=5)
        unit_label.pack(side='left', padx=5, pady=5)

        frame.pack(pady=5)
        return entry  # Return the entry field for further manipulation

    def calculate(self):
        # Aktif sekmeyi kontrol et
        current_tab = self.notebook.select()

        # Hangi sekme aktifse ona göre hesaplama fonksiyonunu çağır
        if current_tab == str(self.tab1):
            self.calculate_tab1()
        elif current_tab == str(self.tab2):
            self.calculate_tab2()
        elif current_tab == str(self.tab3):
            self.calculate_tab3()        

    def calculate_tab1(self):
        global label_result
        try:
            selection = self.combobox_ohm.get()
            if selection == "Voltage (V) ve Resistance (R)":
                r = float(self.entry_ohm.get())
                v = float(self.entry_volt.get())
                if r != 0:
                    result = v / r
                    self.entry_current.config(state='normal')
                    self.entry_current.delete(0, tk.END)
                    self.entry_current.insert(0, str(result))
                    self.entry_current.config(state='disabled')
                    self.label_result.config(text=f"I = {result:.2f} A")
                else:
                    self.label_result.config(text="Resistance cannot be zero!")
            elif selection == "Voltage (V) ve Current (I)":
                v = float(self.entry_volt.get())
                i = float(self.entry_current.get())
                result = v / i
                self.entry_ohm.config(state='normal')
                self.entry_ohm.delete(0, tk.END)
                self.entry_ohm.insert(0, str(result))
                self.entry_ohm.config(state='disabled')
                self.label_result.config(text=f"R = {result:.2f} Ω")
            elif selection == "Resistance (R) ve Current (I)":
                r = float(self.entry_ohm.get())
                i = float(self.entry_current.get())
                result = r * i
                self.entry_volt.config(state='normal')
                self.entry_volt.delete(0, tk.END)
                self.entry_volt.insert(0, str(result))
                self.entry_volt.config(state='disabled')
                self.label_result.config(text=f"V = {result:.2f} V")
        except ValueError:
            self.label_result.config(text="Please enter valid numbers.")

    def calculate_tab2(self):
        try:
            B = float(self.entry_B.get())
            mu = float(self.entry_mu.get())
            I = float(self.entry_I.get())
            r = float(self.entry_r.get())
            result = (mu * I) / (2 * 3.14 * r)
            self.entry_B.config(state='normal')
            self.entry_B.delete(0, tk.END)
            self.entry_B.insert(0, str(result))
            self.entry_B.config(state='disabled')
        except ValueError:
            self.label_result.config(text="Please enter valid numbers.")

    def calculate_tab3(self):
        try:
            df = float(self.entry_df.get())
            dt = float(self.entry_dt.get())
            result = -df / dt
            self.entry_E.config(state='normal')
            self.entry_E.delete(0, tk.END)
            self.entry_E.insert(0, str(result))
            self.entry_E.config(state='disabled')
        except ValueError:
            self.label_result.config(text="Please enter valid numbers.")

if __name__ == "__main__":
    app = CalculatorApp()
    app.geometry("400x400")
    app.mainloop()
