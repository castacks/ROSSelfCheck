
import rclpy
from rclpy.node import Node

class CounterPublisher(Node):
    def __init__(self):
        super().__init__('counter_publisher')

        self.declare_parameter('start_count', 0)

        start_count = self.get_parameter('start_count').get_parameter_value().integer_value

        # TODO: Need to import the Counter message type from msg_interfaces package.
        self.publisher_ = self.create_publisher(Counter, 'counter', 10)

        # TODO: Need to import the class definition of CounterMsgCreator from the py_pkg package.
        self.counter_msg_creator_ = \
            CounterMsgCreator('counter_publisher', start_count)

        self.timer_ = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = self.counter_msg_creator_.create(node=self)
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "{0}"'.format(msg))
