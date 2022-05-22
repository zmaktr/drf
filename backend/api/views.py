import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from products.models import Products
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["POST"])
def api_home(request, *args, **kwargs):  

    # print(dir(request))
    # print(request)

    # body = request.body
    # print(body)

    # data = {}
    # try:
    #     data = json.loads(body) # takes in JSON data --> returns python dictionary
    # except:
    #     pass
    # print(data)

    # print(request.headers) # request.headers in python dictionary
    # print(json.dumps(dict(request.headers))) # request.headers in json format
    # print(request.content_type)

    # data['prams']           = dict(request.GET)
    # data['headers']         = dict(request.headers)
    # data['content_type']    = request.content_type

    model_data = Products.objects.all().order_by("?").first()
    
    data = {}

    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price'])
        # json_data_string = json.dumps(data)

    return Response(data)
    return HttpResponse(json_data_string)