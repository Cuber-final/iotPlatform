from django.db import models
from apps.website.models import DataStream


class Info(models.Model):
    # 在前端可通过点击数据浏览标签进入该设备的实时展 示
    device_id = models.IntegerField(primary_key=True, unique=True, null=False)  # 设备号为主键
    tag = models.CharField(max_length=32, null=True, blank=True)  # 设备标签-设备类型
    device_key = models.CharField(max_length=32, null=True, blank=True)  # 设备传输密钥
    device_name = models.CharField(max_length=32, null=True, blank=True)  # 设备名S
    dev_status = models.BooleanField(default=0, null=False)  # 在线状态,默认为 0 present offset and 1 present online
    creative_date = models.DateTimeField(auto_now_add=True)  # 创建时间
    protocol = models.CharField(max_length=10, null=True, default='mqtt')  # 传输协议,默认使用mqtt协议
    # 数据流为json序列，主要内容为所采集数据，这部分为每个设备的数据集的外键，多对多关系
    dev_stream = models.ManyToManyField(DataStream, blank=True, null=True)  # 传感器数据流

    class Meta:
        db_table = 'deviceInfo'
