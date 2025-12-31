# SPDX-FileCopyrightText: 2025 Raito Kaneko
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TextSource(Node):
    def __init__(self):
        super().__init__('text_source')
        self.pub = self.create_publisher(String, 'raw_text', 10)
        self.timer = self.create_timer(3.0, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "今日は良い日だと思いました。明日も晴れると考えました。"
        self.pub.publish(msg)
        self.get_logger().info('Sent: ' + msg.data)

def main():
    rclpy.init()
    node = TextSource()
    rclpy.spin(node)
