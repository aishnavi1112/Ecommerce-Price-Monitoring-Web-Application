

SERP_API_KEY="c4621bc8d333fa3bd1257042a84f645e21c76aa9dd4c33e16261c92121454431"

import json
from serpapi import GoogleSearch


def search_product(search_query):
  params = {
    "engine": "google_shopping",
    "q": search_query,
    "api_key": SERP_API_KEY,
    "gl": 'in'
  }
  search = GoogleSearch(params)
  results = search.get_dict()

  with open("result.json", "w+") as file:
    file.write(json.dumps(results))
  shopping_results = results["shopping_results"]

  return shopping_results


def get_seller_price(product_id, source):

  params = {
    "engine": "google_product",
    "product_id": product_id,
    "offers": "1",
    "gl": "in",
    "api_key": SERP_API_KEY
  }


  search = GoogleSearch(params)
  results = search.get_dict()
  sellers_results = results["sellers_results"]["online_sellers"]

  seller = list(filter(
    lambda seller: seller if source.lower() in seller['name'].lower() else None, sellers_results
  ))[0]

  if seller:
    price = seller['base_price'].replace(",", "")[1:]
  return price
