import rclpy                         # ROS2のクライアントのためのライブラリ
from rclpy.node import Node          # ノードを実装するためのNodeクラス
from person_msgs.msg import Person       # 通信の型（16ビットの符号付き整数）


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg)


def main():
    pub = node.create_subscription(Person, "person", cb, 10)
    rclpy.spin(node)
