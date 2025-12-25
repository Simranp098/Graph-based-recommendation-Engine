# Inside backend/app/routes/recommendations.py
from fastapi import APIRouter, Depends
from ..services.recommender import RecommenderService # 1. Import your service

router = APIRouter()

@router.get("/recommendations/user/{user_id}")
def get_user_recommendations(user_id: int, recommender: RecommenderService = Depends()): # 2. Inject the service
    # 3. Call the actual recommendation function and return the results
    recommendations = recommender.recommend_products_for_user(user_id) #call the funtion perform all neo4j logic
    return recommendations