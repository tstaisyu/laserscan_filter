import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from laser_filters.laser_scan_filters import LaserScanAngleBoundsFilter

class LaserFilterNode(Node):
    def __init__(self):
        super().__init__('laser_filter_node')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            10)
        self.publisher = self.create_publisher(LaserScan, '/scan_filtered', 10)
        self.filter = LaserScanAngleBoundsFilter()

        # Load parameters
        self.declare_parameters(namespace='', parameters=[
            {'lower_angle': 0.0, 'upper_angle': 0.0, 'invert': False}
        ])
        self.filter.configure(self.get_parameters_by_prefix('filter'))

    def laser_callback(self, msg):
        filtered_scan = self.filter.update(msg)
        self.publisher.publish(filtered_scan)

def main(args=None):
    rclpy.init(args=args)
    laser_filter_node = LaserFilterNode()
    rclpy.spin(laser_filter_node)
    laser_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

