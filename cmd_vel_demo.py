import rclpy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node


class CmdVelDemo(Node):
    def __init__(self):
        super().__init__('cmd_vel_demo')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Odometry,
            '/model/vehicle_blue/odometry',
            self.on_odometry,
            10,
        )
        self.timer = self.create_timer(0.5, self.publish_cmd_vel)
        self.step = 0

    def on_odometry(self, msg: Odometry):
        position = msg.pose.pose.position
        self.get_logger().info(
            f'Odometria: x={position.x:.2f}, y={position.y:.2f}, z={position.z:.2f}'
        )

    def publish_cmd_vel(self):
        msg = Twist()
        if self.step < 10:
            msg.linear.x = 0.5
            msg.angular.z = 0.0
            self.get_logger().info('Andando para frente')
        elif self.step < 15:
            msg.linear.x = 0.0
            msg.angular.z = 0.8
            self.get_logger().info('Girando')
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Parando')

        self.publisher.publish(msg)
        self.step += 1

        if self.step > 20:
            self.get_logger().info('Encerrando demonstracao')
            rclpy.shutdown()


def main():
    rclpy.init()
    node = CmdVelDemo()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
