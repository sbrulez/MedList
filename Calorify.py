import tkinter as tk
from tkinter import messagebox
from datetime import timedelta

class CalorifyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calorify")
        self.geometry("400x350")

        self.current_weight = tk.StringVar()
        self.target_weight = tk.StringVar()
        self.selected_period = tk.StringVar(value="Weekly")

        self.create_widgets()
        self.show_main_page()

    def create_widgets(self):
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(self.main_frame, text="Welcome to Calorify", font=("Helvetica", 18))
        label.pack(pady=20)

        start_button = tk.Button(self.main_frame, text="Get Started", command=self.show_calculate_page)
        start_button.pack()

        self.calculate_frame = tk.Frame(self)
        label1 = tk.Label(self.calculate_frame, text="Enter your current weight in pounds:")
        label1.pack()

        current_weight_entry = tk.Entry(self.calculate_frame, textvariable=self.current_weight)
        current_weight_entry.pack()

        label2 = tk.Label(self.calculate_frame, text="Enter your target weight in pounds:")
        label2.pack()

        target_weight_entry = tk.Entry(self.calculate_frame, textvariable=self.target_weight)
        target_weight_entry.pack()

        period_label = tk.Label(self.calculate_frame, text="Select time period:")
        period_label.pack()

        period_options = ["Weekly", "Monthly", "Quarterly"]
        period_menu = tk.OptionMenu(self.calculate_frame, self.selected_period, *period_options)
        period_menu.pack()

        calculate_button = tk.Button(self.calculate_frame, text="Calculate", command=self.calculate)
        calculate_button.pack()

        back_button = tk.Button(self.calculate_frame, text="Back", command=self.show_main_page)
        back_button.pack()

        self.result_frame = tk.Frame(self)
        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack(pady=50)

    def show_main_page(self):
        self.result_frame.pack_forget()
        self.calculate_frame.pack_forget()
        self.main_frame.pack()

    def show_calculate_page(self):
        self.main_frame.pack_forget()
        self.calculate_frame.pack()

    def show_result_page(self, result):
        self.result_label.config(text=result)
        self.calculate_frame.pack_forget()
        self.result_frame.pack()

    def calculate(self):
        try:
            current_weight = float(self.current_weight.get())
            target_weight = float(self.target_weight.get())

            if target_weight > current_weight:
                days_needed = self.weight_training_calculator(current_weight, target_weight)
                result = f"To reach your target weight, focus on weight training for approximately {days_needed} days."
                self.show_result_page(result)
            elif target_weight < current_weight:
                calories_needed = self.calories_to_burn(current_weight, target_weight)
                period_days = self.get_period_days(self.selected_period.get())
                calories_per_period = calories_needed / period_days
                result = f"To reach your target weight in {self.selected_period.get().lower()}, burn approximately {calories_per_period:.2f} calories per day."
                self.show_result_page(result)
            else:
                messagebox.showinfo("Info", "Your current weight is the same as your target weight. No action needed!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid weight values.")

    def weight_training_calculator(self, current_weight, target_weight):
        pounds_to_gain = target_weight - current_weight
        calories_burned_per_lb_muscle = 50
        days_needed = pounds_to_gain * calories_burned_per_lb_muscle
        return days_needed

    def calories_to_burn(self, current_weight, target_weight):
        pounds_to_lose = current_weight - target_weight
        calories_to_burn = pounds_to_lose * 3500
        return calories_to_burn

    def get_period_days(self, period):
        if period == "Weekly":
            return 7
        elif period == "Monthly":
            return 30  
        elif period == "Quarterly":
            return 90 

if __name__ == "__main__":
    app = CalorifyApp()
    app.mainloop()

