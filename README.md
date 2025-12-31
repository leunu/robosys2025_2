# mypkg - 文末表現解析パッケージ

[![test](https://github.com/leunu/robosys2025_2/actions/workflows/test.yml/badge.svg)](https://github.com/leunu/robosys2025_2/actions/workflows/test.yml)

このパッケージは、ROS 2を用いてテキスト内の文末表現（「と思いました。」等）をリアルタイムに解析するシステムです。

## ノードとトピックの説明
### 1. text_source ノード
- **役割**: 解析対象となる文章を一定周期で配信します。
- **配信トピック**: `/raw_text` [std_msgs/String]

### 2. style_checker ノード
- **役割**: 受信した文章の文末表現をカウントし、結果を配信します。
- **購読トピック**: `/raw_text` [std_msgs/String]
- **配信トピック**: `/check_result` [std_msgs/String]

## 実行方法
以下のローンチファイルを使用することで、両方のノードを同時に起動できます。

```bash
ros2 launch mypkg talk_and_check.launch.py
E0F
