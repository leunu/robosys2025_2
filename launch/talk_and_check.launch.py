# SPDX-FileCopyrightText: 2025 Raito Kaneko
# SPDX-License-Identifier: BSD-3-Clause
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='mypkg', executable='text_source'),
        Node(package='mypkg', executable='style_checker'),
    ])
