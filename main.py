import tkinter as tk
from ca_system_service import CASystemCollector, ca_format_metrics


class CASystemApp:
    def __init__(self, master_window):
        self.master = master_window
        self.master.title("CA System Monitor - Dunaújvárosi Egyetem")
        self.master.geometry("520x460")
        self.master.minsize(480, 420)
        self.collector = CASystemCollector()


if __name__ == "__main__":
    root = tk.Tk()
    app = CASystemApp(root)
    root.mainloop()
