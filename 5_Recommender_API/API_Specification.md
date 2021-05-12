## Instacart: API Specification
### 1. Installation:
To install and run the API, please follow these steps in your terminal:  
1. `cd instacart-product-recommender/5_Recommender_API`  
2. `python recommender_api.py`

This starts the *Flask* app in development mode. The API should be querying for requests under `http://127.0.0.1:5000/`.  

To retrieve results from the API, you can of course use *Postman* or *Insomnia* or similar API testing tools. Additionally, you can query for product recommendations using the `requests`library in Python. Note that the API does not have routes, but parameters need to be sent as JSON (or as dictionaries in Python). Note as well that — in order to facilitate the intuition behind the API — it does not accept the product IDs and instead takes product names, which are parsed internally using string matching. In a real-life setting, one would of course query the API using exact product specifications.  

### 2. Querying the API

This could be one possible schemas used for querying the API:

```json
{
	"product_count": 2,  
	"cluster_num": 3,  
	"current_basket":   {
		"product1": "Sushi",
		"product2": "Craft Beer",
		"product3": "Avocado",
		"product4": "Watermelon"
	}
}
```

The current basket takes annother dictionary of products. The possible length of `current_basket`is flexible and allows for a varied length of baskets. The four items chosen here serve illustrative purposes. 

