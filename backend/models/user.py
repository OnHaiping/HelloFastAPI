from tortoise import models
from tortoise import fields


class User(models.Model):
    username = fields.CharField(max_length=20, null=False, description="账号")
    password = fields.CharField(max_length=100, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=True, description="昵称", default="你好")
