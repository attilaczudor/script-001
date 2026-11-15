import tkinter as tk
from tkinter import ttk
from ca_system_service import CASystemCollector, ca_format_metrics


class CASystemApp:
    def __init__(self, master_window):
        self.master = master_window
        self.master.title("CA System Monitor - Dunaújvárosi Egyetem")
        self.master.geometry("560x580")
        self.master.minsize(520, 520)
        self.collector = CASystemCollector()

        self.main_container = tk.Frame(self.master, padx=16, pady=16)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.header_frame = tk.Frame(self.main_container, pady=6)
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
        self.separator.pack(fill=tk.X, pady=8)

        self.cpu_card = tk.LabelFrame(
            self.main_container,
            text=" Processor (CPU) ",
            font=("Helvetica", 11, "bold"),
            padx=12,
            pady=8
        )
        self.cpu_card.pack(fill=tk.X, pady=4)

        self.cpu_percent_label = tk.Label(
            self.cpu_card,
            text="CPU Terheltség: 0.0%",
            font=("Helvetica", 11)
        )
        self.cpu_percent_label.pack(anchor="w")

        self.cpu_status_label = tk.Label(
            self.cpu_card,
            text="Állapot: NORMAL",
            font=("Helvetica", 10, "bold"),
            fg="forest green"
        )
        self.cpu_status_label.pack(anchor="w", pady=(2, 0))

        self.memory_card = tk.LabelFrame(
            self.main_container,
            text=" Rendszermemória (RAM) ",
            font=("Helvetica", 11, "bold"),
            padx=12,
            pady=8
        )
        self.memory_card.pack(fill=tk.X, pady=4)

        self.memory_details_label = tk.Label(
            self.memory_card,
            text="Használat: 0.00 GB / 0.00 GB (0.0%)",
            font=("Helvetica", 11)
        )
        self.memory_details_label.pack(anchor="w")

        self.memory_status_label = tk.Label(
            self.memory_card,
            text="Állapot: NORMAL",
            font=("Helvetica", 10, "bold"),
            fg="forest green"
        )
        self.memory_status_label.pack(anchor="w", pady=(2, 0))

        self.disk_card = tk.LabelFrame(
            self.main_container,
            text=" Háttértár (Partíció: /) ",
            font=("Helvetica", 11, "bold"),
            padx=12,
            pady=8
        )
        self.disk_card.pack(fill=tk.X, pady=4)

        self.disk_details_label = tk.Label(
            self.disk_card,
            text="Tárhely: 0.00 GB / 0.00 GB (0.0%)",
            font=("Helvetica", 11)
        )
        self.disk_details_label.pack(anchor="w")

        self.disk_status_label = tk.Label(
            self.disk_card,
            text="Állapot: NORMAL",
            font=("Helvetica", 10, "bold"),
            fg="forest green"
        )
        self.disk_status_label.pack(anchor="w", pady=(2, 0))

        self.control_frame = tk.Frame(self.main_container, pady=12)
        self.control_frame.pack(fill=tk.X)

        self.refresh_button = tk.Button(
            self.control_frame,
            text="Frissítés most",
            command=self.on_manual_refresh,
            font=("Helvetica", 10, "bold"),
            padx=10,
            pady=4
        )
        self.refresh_button.pack(side=tk.LEFT)

        self.last_update_label = tk.Label(
            self.control_frame,
            text="Utolsó frissítés: -",
            font=("Helvetica", 9),
            fg="dim gray"
        )
        self.last_update_label.pack(side=tk.RIGHT)

        self.on_manual_refresh()

    def get_status_color(self, status):
        if status == "CRITICAL":
            return "firebrick"
        if status == "WARNING":
            return "dark orange"
        return "forest green"

    def on_manual_refresh(self):
        data = self.collector.collect_all()

        self.cpu_percent_label.config(
            text=f"CPU Terheltség: {data['cpu']['percent']:.1f}%"
        )
        self.cpu_status_label.config(
            text=f"Állapot: {data['cpu']['status']}",
            fg=self.get_status_color(data['cpu']['status'])
        )

        self.memory_details_label.config(
            text=f"Használat: {data['memory']['formatted_used']} / {data['memory']['formatted_total']} ({data['memory']['percent']:.1f}%)"
        )
        self.memory_status_label.config(
            text=f"Állapot: {data['memory']['status']}",
            fg=self.get_status_color(data['memory']['status'])
        )

        self.disk_details_label.config(
            text=f"Tárhely: {data['disk']['formatted_used']} / {data['disk']['formatted_total']} ({data['disk']['percent']:.1f}%)"
        )
        self.disk_status_label.config(
            text=f"Állapot: {data['disk']['status']}",
            fg=self.get_status_color(data['disk']['status'])
        )

        self.last_update_label.config(
            text=f"Utolsó frissítés: {data['platform']['timestamp']}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = CASystemApp(root)
    root.mainloop()
