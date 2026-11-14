import json
import os
from datetime import datetime
import psutil


class CASystemCollector:
    def __init__(self, partition_path="/"):
        self.partition_path = partition_path
        self.last_snapshot = {}
        self.collector_name = "CASystemCollector"

    def get_platform_info(self):
        return {
            "os": os.name,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def get_cpu_usage(self):
        load_percentage = psutil.cpu_percent(interval=None)
        status_text = ca_evaluate_load_status(load_percentage)
        return {
            "percent": load_percentage,
            "status": status_text
        }

    def get_memory_usage(self):
        memory_info = psutil.virtual_memory()
        return {
            "total": memory_info.total,
            "used": memory_info.used,
            "free": memory_info.available,
            "percent": memory_info.percent,
            "formatted_total": ca_format_metrics(memory_info.total),
            "formatted_used": ca_format_metrics(memory_info.used),
            "formatted_free": ca_format_metrics(memory_info.available),
            "status": ca_evaluate_load_status(memory_info.percent)
        }

    def get_disk_usage(self):
        disk_info = psutil.disk_usage(self.partition_path)
        return {
            "path": self.partition_path,
            "total": disk_info.total,
            "used": disk_info.used,
            "free": disk_info.free,
            "percent": disk_info.percent,
            "formatted_total": ca_format_metrics(disk_info.total),
            "formatted_used": ca_format_metrics(disk_info.used),
            "formatted_free": ca_format_metrics(disk_info.free),
            "status": ca_evaluate_load_status(disk_info.percent)
        }

    def collect_all(self):
        self.last_snapshot = {
            "platform": self.get_platform_info(),
            "cpu": self.get_cpu_usage(),
            "memory": self.get_memory_usage(),
            "disk": self.get_disk_usage()
        }
        return self.last_snapshot

    def save_snapshot_to_file(self, target_filepath=None):
        if not self.last_snapshot:
            self.collect_all()
        if not target_filepath:
            target_filepath = "ca_system_metrics_snapshot.json"
        with open(target_filepath, "w", encoding="utf-8") as output_file:
            json.dump(self.last_snapshot, output_file, indent=4)
        return os.path.abspath(target_filepath)


def ca_format_metrics(raw_bytes, unit="GB", decimal_places=2):
    divisor_map = {
        "KB": 1024,
        "MB": 1024 ** 2,
        "GB": 1024 ** 3,
        "TB": 1024 ** 4
    }
    divisor = divisor_map.get(unit, 1024 ** 3)
    converted_value = raw_bytes / divisor
    return f"{converted_value:.{decimal_places}f} {unit}"


def ca_evaluate_load_status(percent_value):
    if percent_value >= 85.0:
        return "CRITICAL"
    if percent_value >= 70.0:
        return "WARNING"
    return "NORMAL"
