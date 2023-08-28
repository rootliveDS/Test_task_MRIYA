import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Received: %s", data.data)

def listener_node():
    rospy.init_node('listener_node', anonymous=True)
    rospy.Subscriber('log_topic', String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener_node()
