import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class SquareMover(Node):
    def __init__(self):
        super().__init__('square_mover')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self._tick)  # run every 0.1s
        self.stage = 0
        self.t0 = time.time()
        # tweak these if needed
        self.forward_speed = 0.20
        self.turn_speed_deg = 45.0
        self.forward_time = 2.0
        self.turn_time = 2.0

    def _tick(self):
        msg = Twist()
        now = time.time()

        if self.stage % 2 == 0:
            # move forward
            msg.linear.x = self.forward_speed
            if now - self.t0 > self.forward_time:
                self.stage += 1
                self.t0 = now
        else:
            # rotate ~90°
            msg.angular.z = math.radians(self.turn_speed_deg)
            if now - self.t0 > self.turn_time:
                self.stage += 1
                self.t0 = now

        if self.stage >= 8:
            self.pub.publish(Twist())  # stop
            self.get_logger().info('Square complete!')
            rclpy.shutdown()
            return

        self.pub.publish(msg)

def main():
    rclpy.init()
    node = SquareMover()
    rclpy.spin(node)

if __name__ == '__main__':
    main()
