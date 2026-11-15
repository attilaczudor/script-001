import os
import unittest
from ca_system_service import (
    CASystemCollector,
    ca_format_metrics,
    ca_evaluate_load_status
)


class CATestSystemCollector(unittest.TestCase):
    def setUp(self):
        self.collector = CASystemCollector()

    def test_ca_format_metrics_gigabytes(self):
        raw_bytes = 1024 ** 3 * 2
        formatted = ca_format_metrics(raw_bytes, "GB")
        self.assertEqual(formatted, "2.00 GB")

    def test_ca_format_metrics_megabytes(self):
        raw_bytes = 1024 ** 2 * 500
        formatted = ca_format_metrics(raw_bytes, "MB")
        self.assertEqual(formatted, "500.00 MB")

    def test_ca_evaluate_load_status_normal(self):
        status = ca_evaluate_load_status(45.0)
        self.assertEqual(status, "NORMAL")

    def test_ca_evaluate_load_status_warning(self):
        status = ca_evaluate_load_status(75.0)
        self.assertEqual(status, "WARNING")

    def test_ca_evaluate_load_status_critical(self):
        status = ca_evaluate_load_status(92.0)
        self.assertEqual(status, "CRITICAL")

    def test_collector_cpu_metrics(self):
        cpu_data = self.collector.get_cpu_usage()
        self.assertIn("percent", cpu_data)
        self.assertIn("status", cpu_data)
        self.assertGreaterEqual(cpu_data["percent"], 0.0)

    def test_collector_memory_metrics(self):
        memory_data = self.collector.get_memory_usage()
        self.assertIn("total", memory_data)
        self.assertIn("used", memory_data)
        self.assertIn("percent", memory_data)
        self.assertIn("formatted_total", memory_data)

    def test_collector_disk_metrics(self):
        disk_data = self.collector.get_disk_usage()
        self.assertIn("path", disk_data)
        self.assertIn("total", disk_data)
        self.assertIn("used", disk_data)
        self.assertIn("percent", disk_data)

    def test_collector_snapshot_save(self):
        temp_target = "test_ca_snapshot.json"
        result_path = self.collector.save_snapshot_to_file(temp_target)
        self.assertTrue(os.path.exists(temp_target))
        if os.path.exists(temp_target):
            os.remove(temp_target)


if __name__ == "__main__":
    unittest.main()
