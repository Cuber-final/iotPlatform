# Author Cuber
# coding=utf-8
# @Time    : 2021/2/2 17:18
# @Site    : 
# @File    : client.py
# @Software: PyCharm
import json
import threading

from paho.mqtt import client as mqtt
# 当连接上服务器后回调此函数
import time

HOST = "127.0.0.1"
PORT = 1883


class MqttClient:
    client = mqtt.Client('tester')

    def __init__(self, host, port):
        self._on_message = None
        self._host = host
        self._port = port

        self.client.on_connect = self._on_connect  # 设置连接上服务器回调函数
        self.client.on_message = self._on_message  # 设置接收到服务器消息回调函数

    def connect(self, username='admin', password='public'):
        self.client.username_pw_set(username, password)
        self.client.connect(self._host, self._port, 60)  # 连接服务器,端口为1883,维持心跳为60秒

    def publish(self, topic, data):
        self.client.publish(topic, data)

    def loop(self, timeout=None):
        thread = threading.Thread(target=self._loop, args=(timeout,))
        # thread.setDaemon(True)
        thread.start()

    def _loop(self, timeout=None):
        if not timeout:
            self.client.loop_forever()
        else:
            self.client.loop(timeout)

    def _on_connect(self, client, userdata, flags, rc):
        print("\nConnected with result code " + str(rc))
        client.subscribe("test")

    def _is_json(self, data):
        try:
            json.loads(data)
        except ValueError:
            return False
        return True

    def publish_loop(self):
        pass


# 问题：如何确认是否发出，即需要接收方提供确认消息
if __name__ == '__main__':
    client = MqttClient(HOST, PORT)
    client.connect('tester', 'tester')
    data = '{"msg":"hello world","tel":"187232"}'
    # client.publish('test', '123456')
    client.publish('test', data)
    client.loop()
