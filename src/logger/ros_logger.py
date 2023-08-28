import rospy
from std_msgs.msg import String

def logger_node():
    rospy.init_node('logger_node', anonymous=True)
    log_pub = rospy.Publisher('log_topic', String, queue_size=10)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        log_data = "Logging some data..."
        log_pub.publish(log_data)
        rate.sleep()

if __name__ == '__main__':
    logger_node()