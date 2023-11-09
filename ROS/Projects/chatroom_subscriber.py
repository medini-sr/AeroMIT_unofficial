#!/usr/bin/env python3



import rospy
from std_msgs.msg import String

def chatroom_listener(data):
    rospy.loginfo(data.data)

def chatroom_subscriber():
    rospy.init_node('chatroom_subscriber')
    rospy.Subscriber('chatroom_topic', String, chatroom_listener)
    rospy.spin()
def chatroom server():
    rospy.init_node('chatroom_server')
    pub = rospy.Publisher('chatroom_topic', String, queue_size=10)
    
while not rospy.is_shutdown():
    username = input("Enter your username: ")
    message = input("Enter a message: ")

        # Get the current timestamp
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Format the message with username and timestamp
    formatted_message = f"[{timestamp}] {username}: {message}"

    pub.publish(formatted_message)

if __name__ == '__main__':
    chatroom_subscriber()
