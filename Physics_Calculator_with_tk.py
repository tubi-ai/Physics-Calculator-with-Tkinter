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
    def __init__(self, parent, command_callback):
        super().__init__(parent)
        self.command_callback = command_callback
        self.create_buttons()
            
    def reset():
        global label_result
        entry_ohm.config(state='normal')
        entry_volt.config(state='normal')
        entry_current.config(state='normal')
    
        entry_ohm.delete(0, tk.END)
        entry_volt.delete(0, tk.END)
        entry_current.delete(0, tk.END)
    
        label_result.config(text=' ')
        combobox_ohm.set("Voltage (V) ve Resistance (R)")
        tab1_handler.update_entries(combobox_ohm.get())
    
        # Optionally set focus to a default entry
        entry_volt.focus_set()
                
    def create_buttons(self):
        # First row's buttons
        button_1 = ttk.Button(self, text='1', command=lambda: self.command_callback(1), takefocus=False)
        button_2 = ttk.Button(self, text='2', command=lambda: self.command_callback(2), takefocus=False)
        button_3 = ttk.Button(self, text='3', command=lambda: self.command_callback(3), takefocus=False)
        
        
        button_1.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        button_2.grid(row=0, column=1, sticky="nsew", padx=2, pady=2)
        button_3.grid(row=0, column=2, sticky="nsew", padx=2, pady=2)
    
        # Second row's buttons
        button_4 = ttk.Button(self, text='4', command=lambda: self.command_callback(4), takefocus=False)
        button_5 = ttk.Button(self, text='5', command=lambda: self.command_callback(5), takefocus=False)
        button_6 = ttk.Button(self, text='6', command=lambda: self.command_callback(6), takefocus=False)
            
        button_4.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
        button_5.grid(row=1, column=1, sticky="nsew", padx=2, pady=2)
        button_6.grid(row=1, column=2, sticky="nsew", padx=2, pady=2)
        
        # Third row's buttons
        button_7 = ttk.Button(self, text='7', command=lambda: self.command_callback(7), takefocus=False)
        button_8 = ttk.Button(self, text='8', command=lambda: self.command_callback(8), takefocus=False)
        button_9 = ttk.Button(self, text='9', command=lambda: self.command_callback(9), takefocus=False)
    
        button_7.grid(row=2, column=0, sticky="nsew", padx=2, pady=2)
        button_8.grid(row=2, column=1, sticky="nsew", padx=2, pady=2)
        button_9.grid(row=2, column=2, sticky="nsew", padx=2, pady=2)
        
        # Fourth row's button
        button_dot = ttk.Button(self, text='.', command=lambda: self.command_callback('.'), takefocus=False)
        button_0 = ttk.Button(self, text='0', command=lambda: self.command_callback(0), takefocus=False)
        button_del = ttk.Button(self, text='delete', command=lambda: self.command_callback('delete'), takefocus=False)
        
        button_dot.grid(row=3, column=0, sticky="nsew", padx=2, pady=2)
        button_0.grid(row=3, column=1, sticky="nsew", padx=2, pady=2)
        button_del.grid(row=3, column=2, sticky="nsew", padx=2, pady=2)
    
        # Configure rows and columns to expand equally
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for j in range(5):
            self.grid_rowconfigure(j, weight=1)

class CalculatorApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Notebook widget'ını oluştur
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Sekme 1 ve Sekme 2'yi oluştur
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        self.notebook.add(self.tab1, text="Ohm's Law: V = I * R")
        self.notebook.add(self.tab2, text="Ampère's Law: B = μ * I / (2 * π * r)")
        self.notebook.add(self.tab3, text="Faraday's Law: E = - ΔΦ / Δt")
        
        self.combobox_ohm = ttk.Combobox(self.tab1, values=["Voltage (V) & Resistance (R)", "Voltage (V) & Current (I)", "Resistance (R) & Current (I)"])
        self.combobox_ohm.set("Voltage (V) & Resistance (R)")
        self.combobox_ohm.pack(fill='both')
        
        self.combobox_amp = ttk.Combobox(self.tab2, values=["Magnetic Field (B) & Current (I) & Magnetic Permeability of the Medium (μ)", "Radius (r) & Current (I) & Magnetic Permeability of the Medium (μ)", "Magnetic Field (B) & Radius (r) & Magnetic Permeability of the Medium (μ)"])
        self.combobox_amp.set("Magnetic Field (B) & Current (I)  & Magnetic Permeability of the Medium (μ)")
        self.combobox_amp.pack(fill='both')
        
        self.combobox_far = ttk.Combobox(self.tab3, values=["Electromotive Force EMK (E) & Magnetic Flux (ΔΦ)","Magnetic Flux (ΔΦ) & Time Interval (Δt)","Electromotive Force EMK (E) ve Time Interval (Δt)"])
        self.combobox_far.set("Electromotive Force EMK (E) & Magnetic Flux (ΔΦ)")
        self.combobox_far.pack(fill='both')

        
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
        button_pad1 = ButtonPad(self.tab1, button_click)
        button_pad1.pack(pady=80, padx=10, fill='x')
    
        button_pad2 = ButtonPad(self.tab2, button_click)
        button_pad2.pack(pady=10, padx=10, fill='x')
    
        button_pad3 = ButtonPad(self.tab3, button_click)
        button_pad3.pack(pady=10, padx=10, fill='x')    
        
        # "=" button
        equal_button = ttk.Button(self, text='=', command=self.calculate)
        equal_button.pack(pady=10)
        
        # Reset Button
        button_reset = ttk.Button(self, text='Reset', command=self.reset, takefocus=False)
        button_reset.pack(padx=2, pady=2)        

        # Label to show results
        self.label_result = ttk.Label(self, text='')
        self.label_result.pack()
        
    def reset(self, event=None):
        #Reset all entries across tabs.
        for entry in [self.entry_ohm, self.entry_volt, self.entry_current, 
                      self.entry_df, self.entry_dt,self.entry_E, 
                      self.entry_B, self.entry_I, self.entry_r, self.entry_mu]:
            entry.config(state='normal')                                    
            entry.delete(0, tk.END)                                       
                                                                 
        self.label_result.config(text=' ')
        self.combobox_ohm.set(" ")
        self.entry_volt.focus_set()  

    def create_entry_with_label(self, parent, label_text, unit_text):
        frame = ttk.Frame(parent)
        label = ttk.Label(frame, text=label_text)
        entry = ttk.Entry(frame)
        unit_label = ttk.Label(frame, text=unit_text)

        label.pack(side='left', padx=5, pady=5)
        entry.pack(side='left', padx=5, pady=5)
        unit_label.pack(side='left', padx=5, pady=5)

        frame.pack(pady=5)
        # Bind focus event to track the active entry
        entry.bind("<FocusIn>", lambda event: select_entry(entry))
        
        return entry  # Return the entry field for further manipulation

    def calculate(self):
            # Calculate based on active tab
            if self.notebook.index(self.notebook.select()) == 0:  # Tab 1
                v_combobox = self.combobox_ohm.get()
                r = self.get_value(self.entry_ohm)
                i = self.get_value(self.entry_current)
                v = self.get_value(self.entry_volt) 
                if "Resistance (R) & Current (I)" in v_combobox:
                    result = i * r
                    self.entry_volt.config(state='normal')
                    self.entry_volt.delete(0, tk.END)
                    self.entry_volt.insert(0, result)
                    self.entry_volt.config(state='disabled')
                    #self.label_result.config(text=f'V = {result} V')
                    
                elif "Voltage (V) & Resistance (R)" in v_combobox:
                    if r != 0:
                        result = v / r
                        self.entry_current.config(state='normal')
                        self.entry_current.delete(0, tk.END)
                        self.entry_current.insert(0, result)
                        self.entry_current.config(state='disabled')
                        #elf.label_result.config(text=f"I = {result:.2f} A")
                    else:
                        self.label_result.config(text="Error: Resistance cannot be zero!")    
                        
                elif "Voltage (V) & Current (I)" in v_combobox:
                    if i != 0:
                        result = v / i
                        self.entry_ohm.config(state='normal')
                        self.entry_ohm.delete(0, tk.END)
                        self.entry_ohm.insert(0, result)
                        self.entry_ohm.config(state='disabled')
                        #self.label_result.config(text=f"R = {result:.2f} Ω")  
                    else:
                        self.label_result.config(text="Error: Current cannot be zero!")                        
            
            elif self.notebook.index(self.notebook.select()) == 1:  # Tab 2
                b_combobox = self.combobox_amp.get()
                I = self.get_value(self.entry_I)
                r = self.get_value(self.entry_r)
                mu = self.get_value(self.entry_mu)
                B = self.get_value(self.entry_B)
                if "Magnetic Field (B) & Current (I) & Magnetic Permeability of the Medium (μ)" in b_combobox:
                    if B != 0:
                        result = (mu * I) / (2 * 3.14159 * B)
                        self.entry_r.config(state='normal')
                        self.entry_r.delete(0, tk.END)
                        self.entry_r.insert(0, result)
                        self.entry_r.config(state='disabled')
                    else:
                        self.label_result.config(text="Error: Magnetic Field cannot be zero!")                      
                   
                elif "Radius (r) & Current (I) & Magnetic Permeability of the Medium (μ)" in b_combobox:
                    if r != 0:
                        result = (mu * I) / (2 * 3.14159 * r)
                        self.entry_B.config(state='normal')
                        self.entry_B.delete(0, tk.END)
                        self.entry_B.insert(0, result)
                        self.entry_B.config(state='disabled')
                    else:
                        self.label_result.config(text="Error: Radius cannot be zero!")                       
                    
                elif "Magnetic Field (B) & Radius (r) & Magnetic Permeability of the Medium (μ)" in b_combobox:
                    if mu != 0:
                        result = (B * (2 * 3.14159 * r)) / mu
                        self.entry_I.config(state='normal')
                        self.entry_I.delete(0, tk.END)
                        self.entry_I.insert(0, result)
                        self.entry_I.config(state='disabled')
                    else:
                        self.label_result.config(text="Error: Magnetic Permeability of the Medium cannot be zero!")                            
                        
                elif "Magnetic Field (B) & Radius (r) & Current (I)" in b_combobox:
                    if I != 0:
                        result = (B * (2 * 3.14159 * r)) / I
                        self.entry_mu.config(state='normal')
                        self.entry_mu.delete(0, tk.END)
                        self.entry_mu.insert(0, result)
                        self.entry_mu.config(state='disabled') 
                    else:
                        self.label_result.config(text="Error: Current cannot be zero!")                            
                    
            elif self.notebook.index(self.notebook.select()) == 2:  # Tab 3
                f_combobox = self.combobox_far.get()
                dphi = self.get_value(self.entry_df)
                dt = self.get_value(self.entry_dt)
                E = self.get_value(self.entry_E)
                if "Magnetic Flux (ΔΦ) & Time Interval (Δt)" in f_combobox:
                    result = -dphi / dt
                    self.entry_E.config(state='normal')
                    self.entry_E.delete(0, tk.END)
                    self.entry_E.insert(0, result)
                    self.entry_E.config(state='disabled')
                    
                elif "Electromotive Force EMK (E) & Time Interval (Δt)" in f_combobox:
                    result = -E * dt
                    self.entry_df.config(state='normal')
                    self.entry_df.delete(0, tk.END)
                    self.entry_df.insert(0, result)
                    self.entry_df.config(state='disabled')
                    
                elif "Electromotive Force EMK (E) & Magnetic Flux (ΔΦ)" in f_combobox:
                    result = -dphi / E
                    self.entry_dt.config(state='normal')
                    self.entry_dt.delete(0, tk.END)
                    self.entry_dt.insert(0, result)
                    self.entry_dt.config(state='disabled')
    
    def get_value(self, entry):
        try:
            return float(entry.get())
        except ValueError:
            return 0.0  # Handle invalid input    
if __name__ == "__main__":
    app = CalculatorApp()
    app.geometry("600x800")
    app.mainloop()
