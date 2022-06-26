# index.py

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Products

@register(Products)
class ProductsIndex(AlgoliaIndex):
    
    # to filter all public products (public = True)
    # should_index = 'is_public'
    
    # fields to show in result
    fields = ('title', 'content', 'price', 'user', 'public')

    # alogolia tags 
    tags = 'get_tags'

    # geo_field = 'location'
    # settings = {'searchableAttributes': ['name']}
    # index_name = 'my_index'

    settings = {
        # attributes related to the product used for further filtering search 
        'attributesForFaceting' : [ 'user', 'public' ],
        # drive search results based on these attributes
        'searchableAttributes' : [ 'title', 'content']
    }