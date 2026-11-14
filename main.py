import tkinter as tk
from tkinter import ttk
from ca_system_service import CASystemCollector, ca_format_metrics


class CASystemApp:
    def __init__(self, master_window):
        self.master = master_window
        self.master.title("CA System Monitor - Dunaújvárosi Egyetem")
        self.master.geometry("540x480")
        self.master.minsize(500, 440)
        self.collector = CASystemCollector()

        self.main_container = tk.Frame(self.master, padx=16, pady=16)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.header_frame = tk.Frame(self.main_container, pady=8)
        self.header_frame.pack(fill=tk.X)

        self.title_label = tk.Label(
            self.header_frame,
            text="CA System Monitor",
            font=("Helvetica", 18, "bold")
        )
        self.title_label.pack(anchor="w")

        self.subtitle_label = tk.Label(
            self.header_frame,
            text="Czudor Attila (CA) - Szkript nyelvek Python",
            font=("Helvetica", 10),
            fg="dim gray"
        )
        self.subtitle_label.pack(anchor="w")

        self.separator = ttk.Separator(self.main_container, orient="horizontal")
        self.separator.pack(fill=tk.X, pady=10)

        self.cpu_card = tk.LabelFrame(
            self.main_container,
            text=" Processor (CPU) ",
            font=("Helvetica", 11, "bold"),
            padx=12,
            pady=10
        )
        self.cpu_card.pack(fill=tk.X, pady=6)

        self.cpu_percent_label = tk.Label(
            self.cpu_card,
            text="CPU Terheltség: 0.0%",
            font=("Helvetica", 12)
        )
        self.cpu_percent_label.pack(anchor="w")

        self.cpu_status_label = tk.Label(
            self.cpu_card,
            text="Állapot: NORMAL",
            font=("Helvetica", 10, "bold"),
            fg="forest green"
        )
        self.cpu_status_label.pack(anchor="w", pady=(4, 0))


if __name__ == "__main__":
    root = tk.Tk()
    app = CASystemApp(root)
    root.mainloop()
