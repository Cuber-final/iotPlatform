# Register your models here.
from django.contrib import admin
from .models import GUser

from django.contrib.auth.admin import UserAdmin

# 在原有基础上指明添加的字段
ADDITIONAL_FIELDS = ((None, {'fields': ('workerId', 'sex', 'tel', 'commute_start', 'commute_end', 'device', 'post')}),)


class GUserAdmin(UserAdmin):
    # 沿用默认设置，哈希加密数据
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS
    add_fieldsets = UserAdmin.fieldsets + ADDITIONAL_FIELDS


admin.site.register(GUser, GUserAdmin)
