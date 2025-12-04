import rclpy
from rclpy.node import Node
from person_msgs.srv import Query #変更

rclpy.init()
node = Node("talker")

 
def cb(request, responce):
    if request.name == "宮内瞭太"
        response.age = 20
    else:
        response.age = 76
    return response


def main():
    srv = node.create_service(Query, "query", cb) #サービスの作成
    rclpy.spin(node)
