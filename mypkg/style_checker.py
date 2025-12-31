# SPDX-FileCopyrightText: 2025 Raito Kaneko
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StyleChecker(Node):
    def __init__(self):
        super().__init__('style_checker')
        self.pub = self.create_publisher(String, 'check_result', 10)
        self.sub = self.create_subscription(String, 'raw_text', self.cb, 10)
        self.targets = ["と思いました。", "と考えました。", "と感じました。", "と受け止めました。"]

    def cb(self, msg):
        counts = {t: msg.data.count(t) for t in self.targets}
        res = String()
        res.data = str(counts)
        self.pub.publish(res)
        self.get_logger().info('Analyzed: ' + res.data)

def main():
    rclpy.init()
    node = StyleChecker()
    rclpy.spin(node)
