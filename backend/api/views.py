import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.forms.models import model_to_dict
from products.models import Products

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductsSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):  

    print(request.data)
    serializer = ProductsSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return JsonResponse({"invalid" : "change the data input"})

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

    # model_data = Products.objects.all().order_by("?").first()
    # instance = Products.objects.all().order_by("?").first()
    # data = {}
    # data = request.POST
    # data = {}

        # instance = serializer.save()
        # print(instance)
        # print(serializer.data)
        # instance = serializer.save()
        # print(instance)
        # print(serializer.data)
        # data = instance
    # serializer = ProductsSerializer(data.request.data)

        # return Response(serializer.data)

    # if instance:
    #     # data['id'] = model_data.id
    #     # data['title'] = model_data.title
    #     # data['content'] = model_data.content
    #     # data['price'] = model_data.price
    #     # data = model_to_dict(model_data)
    #     # data = model_to_dict(model_data, fields=['id', 'title', 'content', 'price', 'sale_price'])
    #     data = ProductsSerializer(instance).data
    #     # json_data_string = json.dumps(data)

        # return Response(serializer)
    # return HttpResponse(json_data_string)