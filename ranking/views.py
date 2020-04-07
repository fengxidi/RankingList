import json

from rest_framework.views import APIView
from django.http import HttpResponse

from ranking.models import RankModel
from ranking.serializers import RankSerializers

class RankView(APIView):

    def get(self,request,*args,**kwargs):
        account = kwargs.get('account')
        #获取全部数据
        userinfo_ranks = RankModel.objects.all().order_by('rank')
        rets = RankSerializers(instance=userinfo_ranks,many=True)
        res = json.dumps(rets.data,ensure_ascii=False)
        datas = json.loads(res)

        #获取当前用户数据
        userinfo = RankModel.objects.filter(account=account).first()
        ret = RankSerializers(instance=userinfo)
        data = json.loads(json.dumps(ret.data,ensure_ascii=False))
        datas.append(data)

        return  HttpResponse(json.dumps(datas,ensure_ascii=False))

    def post(self,request,*args,**kwargs):

        account = request._request.POST.get('account')
        score = int(request._request.POST.get('score','0'))
        RankModel.objects.update_or_create(account=account,defaults={'score':score,'rank':0})

        userinfo_rank = RankModel.objects.all().order_by('-score')
        for i,user in enumerate(userinfo_rank):
            user.rank = i+1
            user.save()

        return HttpResponse('提交数据')





