from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def get_index(index_name='cfe_Products'):
    client = get_client()
    index = client.init_index(index_name)
    return index

def perform_search(query, *args, **kwargs):
    index = get_index()
    params = {}
    tags = ""

    # add tags to params
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilters'] = tags
    
    # add facetFilters to search --> filter search by "user"   
    index_filter= [f"{k}:{v}" for k, v in kwargs.items() if v]
    if len(index_filter) != 0:
        params['facetFilters'] = index_filter

    results = index.search(query, params)
    return results