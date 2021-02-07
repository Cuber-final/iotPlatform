from django.db import models


# 思考，数据由mqtt消息中间件转发得到的数据时string类型，
# we need jsonStr to be parsed into json


class Data(models.Model):
    data = models.CharField(max_length=64, null=True, blank=True)  # 限制在两位小数
    date = models.DateTimeField(auto_now_add=True)  # 上传时间,自动保存时间

    class Meta:
        db_table = 'DataList'


class DataStream(models.Model):
    stream_name = models.CharField(max_length=20, null=False)  # 数据流名称如'温度'，'湿度'
    stream_para = models.IntegerField(null=True, default=0)  # 数据类型,以属性代码表示0-4分别表示温度、湿度、甲烷浓度等数据流属性
    limit = models.FloatField(null=True, default=0, blank=True)  # 阈值数值,此变量受神经网络算法部分影响,可修改
    qos = models.IntegerField(null=True, default=0)  # 服务质量,0-2
    unit = models.CharField(max_length=10, null=True, blank=True)  # 单位名称,如'米'
    unit_symbol = models.CharField(max_length=10, null=True, blank=True)  # 单位符号,如'm'
    data = models.ManyToManyField(Data, null=True, blank=True)

    class Meta:
        db_table = 'StreamList'
