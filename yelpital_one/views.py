from django.shortcuts import render
import json
import requests


YELP_API_KEY = "KfGcXeifbUMy0zHzGrXd-CI4ciniuZnV3myJsOmgu7zjGXRNBPwgDxF0r0IzZw86nteSPeNLQTKLwMW_oRFJ2iMOQaLhKNmK7cpy3DKBaX7ttsmj-1bOP-YhNltdXnYx"
YELP_SEARCH = "https://api.yelp.com/v3/businesses/search"


def yelp_query(name, location):
  headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
  params = {'name': name, 'location': location}
  query = requests.get(YELP_SEARCH, headers=headers, params=params)
  query_json = query.json()
  with open("yelpital_one/static/data/searchResult.json", "w") as outfile: 
    json.dump(query_json, outfile)
  return query_json


def search(request, *args, **kwargs):
    location = request.GET.get('location')
    name = request.GET.get('name')
    if not location and not name:
      return render(request, "yelpital_one/search.html", {})
    elif location and not name:
      items = yelp_query(name="restaurants", location=location)
    elif name and not location:
      items = yelp_query(name=name, location="united states")
    elif location and name:
      items = yelp_query(name=name, location=location)
    return render(request, "yelpital_one/search.html",{"results":items})
    

    