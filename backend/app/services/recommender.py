from fastapi import Depends #Imports dependency support.
from .neo4j_connection import Neo4jConnection, get_neo4j_connection

class RecommenderService: #Creates a class that handles recommendation logic.
    def __init__(self, neo4j_conn: Neo4jConnection = Depends(get_neo4j_connection)): #Automatically receives a Neo4j connection when object is created.
        self.neo4j_conn = neo4j_conn
        #Automatically receives a Neo4j connection when object is created.

    def recommend_products_for_user(self, user_id: int): #Main function called by API to get recommendations.
        """
        Recommends products and also explains WHY, by showing the similar
        user and the shared product that led to the recommendation.
        """
        # This is a more advanced query that finds the reason for the recommendation
        query = """
        MATCH (targetUser:User {customerID: $user_id})-[:PURCHASED]->(sharedProduct:Product)
        //finds the target users purchased products,

        MATCH (similarUser:User)-[:PURCHASED]->(sharedProduct)
        WHERE targetUser <> similarUser
        //finds other users who purchased the same products (similar users)

        MATCH (similarUser)-[:PURCHASED]->(recommendedProduct:Product)
        WHERE NOT (targetUser)-[:PURCHASED]->(recommendedProduct)
        //Finds new products bought by similar users but not by target use

        WITH recommendedProduct, similarUser, sharedProduct, count(*) AS frequency
        ORDER BY frequency DESC
        //ranks recommended products based on frequency.
        // We use collect() to get a list of reasons and take the first one for simplicity

        
        WITH recommendedProduct, 
             collect({
                 user: similarUser.name, 
                 product: sharedProduct.name
             })[0] AS reason
        RETURN recommendedProduct.id AS product_id,
               recommendedProduct.name AS name,
               recommendedProduct.category AS category,
               reason.user AS similar_user_name,
               reason.product AS shared_product_name
        LIMIT 12
        """
        try:
            results = self.neo4j_conn.query(query, parameters={'user_id': user_id}) 
            #Main function called by API to get recommendations.
            products = [dict(record) for record in results]
            #Converts Neo4j result rows into Python dictionaries.
            return products
        except Exception as e:
            print(f"An error occurred while running the query: {e}")
            return [] #Handles error safely.