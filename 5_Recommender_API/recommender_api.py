from flask import Flask, request, jsonify
from flask_cors import CORS
from engine.recommender_engine import recommend_product

app = Flask(__name__)
CORS(app) #Enable Cross-Origin Resource Sharing

app.config['JSON_SORT_KEY'] = False

# API Endpoint
@app.route('/api/', methods = ['GET'])
def retrieve_recommendations():
    
    # Parse inputs
    user_input = request.get_json()

    # Unpacking current_basket from JSON
    basket = user_input['current_basket'].values()

    recommendations = recommend_product(
        product_count=user_input['product_count'], 
        cluster_number=user_input['cluster_num'], 
        current_basket=basket
    )

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run()