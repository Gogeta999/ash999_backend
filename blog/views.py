from django.http import HttpResponse
from graphene.types.scalars import String
import requests
from requests.api import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
import config

def index(request):
    return HttpResponse('Hello Fucking World!!!')


@api_view(['POST'])
def search(request):
    inputData = request.data
    notionHeaders = {
     "Authorization": "Bearer " + config.NOTION_TOKEN,
     "Content-Type": "application/json",
     "NOTION-Version": "2021-08-16"
    }

    result = requests.post(config.NOTION_SEARCH_URL, json={
    "query": inputData,
    "sort":{
      "direction":"ascending",
      "timestamp":"last_edited_time"
    }  
    } ,headers=notionHeaders)
    data = result.json()
    print('Status------------->' + str(result.status_code))
    print('-------------Data-------------')
    print(data)
    print('::---------------------------------------::')

    return Response(data)
    