from tortoise import models
from tortoise import fields


class Movie(models.Model):
    name = fields.CharField(max_length=50, null=False, description="电影名")
    year = fields.CharField(max_length=50, null=False, description="电影年份")
