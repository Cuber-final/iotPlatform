from django.utils import timezone

from apps.device.models import Info
from django.db import models
from django.contrib.auth.models import AbstractUser


class GUser(AbstractUser):
    # 对User模型的自定义以及拓展,定义一个工人模型即工人数据信息表
    # 工人基本信息，固定,与User模型对应并在此基础上拓展
    workerId = models.IntegerField(unique=True, db_index=True, blank=True, null=True)  # 工号由后端生成
    # 后续可修改的信息
    sex = models.BooleanField(null=True, default=0)  # 性别 0 represent male and 1 represent female
    tel = models.CharField(max_length=20, blank=True, null=True)  # 联系方式
    # 通勤时间，上下班打卡记录自动写入当前时间,时间的修改因受到员工签到事件的触发
    commute_start = models.DateTimeField(default=timezone.now, blank=True)
    commute_end = models.DateTimeField(default=timezone.now, blank=True)
    # 绑定设备,一对多关系，一个员工对应多个设备
    device = models.ForeignKey(Info, on_delete=models.CASCADE, blank=True, null=True)
    # 岗位类型，如矿井工人，地上检查员，基站管理员等，后续通过代码号进行分类
    post = models.IntegerField(blank=True, db_index=True, default=0)

    class Meta(AbstractUser.Meta):
        # 该U属性值定义模型对应的数据表名词
        db_table = 'userInfo'

    def __str__(self):
        return self.username
