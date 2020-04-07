# _*_ coding: utf-8 _*_
__auther__ = 'guozheng'
__date__ = '2020-4-7 21:23'
from rest_framework import serializers
from ranking.models import RankModel

class RankSerializers(serializers.ModelSerializer):
    class Meta:
        model = RankModel
        fields = ['rank','account','score']