
import rclpy

def main(args=None):
    rclpy.init(args=args)

    # Need the CounterPublisher class definition of the current ROS package.
    counter_publisher = CounterPublisher()

    rclpy.spin(counter_publisher)

    counter_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    