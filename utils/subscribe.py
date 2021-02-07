# Author Cuber
# coding=utf-8
# @Time    : 2021/2/2 17:19
# @Site    : 
# @File    : subscribe.py
# @Software: PyCharm
import time
import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("连接成功")
        print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    # 获取来自主题的消息
    # print(msg.topic + " " + str(msg.payload))
    # print(msg.topic)#输出主题
    data = msg.payload.decode()
    # print(type(data))
    print(data)


if __name__ == '__main__':
    client = mqtt.Client("client", protocol=3)
    client.username_pw_set("admin", "password")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host="127.0.0.1", port=1883, keepalive=60)  # 订阅频道
    time.sleep(1)
    # qos为服务质量
    # 如何高效并发订阅主题以及接受消息
    client.subscribe("test", 2)
    client.loop_forever()
