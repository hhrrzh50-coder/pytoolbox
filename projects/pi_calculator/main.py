"""Simple desktop interface for calculating pi."""
import threading
import tkinter as tk
from tkinter import messagebox, ttk

from pytoolbox.pi import calculate_pi


class PiCalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Pi Calculator")
        root.geometry("620x440")
        root.minsize(480, 340)

        frame = ttk.Frame(root, padding=18)
        frame.pack(fill="both", expand=True)
        ttk.Label(frame, text="π Pi Calculator", font=("Segoe UI", 20, "bold")).pack(anchor="w")
        ttk.Label(frame, text="Choose how many digits after the decimal point to calculate.").pack(anchor="w", pady=(4, 14))

        controls = ttk.Frame(frame)
        controls.pack(fill="x")
        ttk.Label(controls, text="Decimal places:").pack(side="left")
        self.digits = tk.StringVar(value="100")
        ttk.Entry(controls, textvariable=self.digits, width=12).pack(side="left", padx=8)
        self.button = ttk.Button(controls, text="Calculate π", command=self.start_calculation)
        self.button.pack(side="left")

        self.status = tk.StringVar(value="Ready")
        ttk.Label(frame, textvariable=self.status).pack(anchor="w", pady=(12, 6))
        self.output = tk.Text(frame, wrap="word", height=13, font=("Consolas", 10))
        self.output.pack(fill="both", expand=True)
        ttk.Button(frame, text="Copy result", command=self.copy_result).pack(anchor="e", pady=(8, 0))

    def start_calculation(self):
        try:
            digits = int(self.digits.get())
            if not 0 <= digits <= 100000:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Enter a whole number from 0 to 100000.")
            return
        self.button.configure(state="disabled")
        self.status.set("Calculating…")
        self.output.delete("1.0", "end")
        threading.Thread(target=self.calculate, args=(digits,), daemon=True).start()

    def calculate(self, digits):
        try:
            result = calculate_pi(digits)
            self.root.after(0, self.show_result, result)
        except Exception as exc:
            self.root.after(0, self.show_error, str(exc))

    def show_result(self, result):
        self.output.insert("1.0", result)
        self.status.set(f"Done — {len(result) - 2 if '.' in result else 0} decimal places")
        self.button.configure(state="normal")

    def show_error(self, error):
        self.status.set("Calculation failed")
        self.button.configure(state="normal")
        messagebox.showerror("Calculation error", error)

    def copy_result(self):
        value = self.output.get("1.0", "end-1c")
        if value:
            self.root.clipboard_clear()
            self.root.clipboard_append(value)
            self.status.set("Result copied to clipboard")


if __name__ == "__main__":
    window = tk.Tk()
    PiCalculatorApp(window)
    window.mainloop()
