import json
import os
from datetime import datetime
import psutil


class CASystemCollector:
    def __init__(self, partition_path="/"):
        self.partition_path = partition_path
        self.last_snapshot = {}

    def get_cpu_usage(self):
        return 0.0

    def get_memory_usage(self):
        return {}

    def get_disk_usage(self):
        return {}


def ca_format_metrics(raw_bytes):
    gb_value = raw_bytes / (1024 ** 3)
    return f"{gb_value:.2f} GB"
