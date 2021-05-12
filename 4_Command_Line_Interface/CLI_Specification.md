## Instacart: CLI Specification
### Running the recommende from the Command Line:
In order to illustrate in an intuitive way the recommender system we have  developed, we created a lightweight CLI. Note that a user of course does not know, which user cluster they belong so, the usecase serves many illustrative purposes.

To run the recommender system using the CLI, please follow these steps in your terminal:  
1. ```cd instacart-product-recommender/4_Command_Line_Interface```  
2. `python recommend_me_something_py [product_count] [cluster_num] [basket_item1, basket_item2 ...]`

You can specify three arguments using the interface:  
1. `product_count`: This specifies how many products should be returned. Note that this is currently not perfectly accurate, as some products in the basket might not be in the cluster item dictionary.  
2. `cluster_num`: This is the number of the cluster the input user belongs too.  
3. `[basket]`: This is a list of basket items, specified as strings. The order does not matter, as the item embeddings are averaged to approximate the "true" basket embeddings.


