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
        return 0.0

    def get_memory_usage(self):
        return {}

    def get_disk_usage(self):
        return {}

    def collect_all(self):
        self.last_snapshot = {
            "platform": self.get_platform_info(),
            "cpu": self.get_cpu_usage(),
            "memory": self.get_memory_usage(),
            "disk": self.get_disk_usage()
        }
        return self.last_snapshot


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
