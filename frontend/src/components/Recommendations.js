import React, { useState, useEffect } from 'react';

function Recommendations({ userId }) {
    const [recommendations, setRecommendations] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        if (!userId) {
            setRecommendations([]);
            return;
        }

        const fetchRecommendations = async () => {
            setIsLoading(true);
            setError(null);
            try {
                const response = await fetch(`http://127.0.0.1:8000/recommendations/user/${userId}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setRecommendations(data);
            } catch (err) {
                setError('Failed to fetch recommendations. Is the backend server running?');
            }
            setIsLoading(false);
        };

        fetchRecommendations();
    }, [userId]);
    
    if (isLoading) {
        return <div className="loading-spinner"></div>;
    }

    if (error) {
        return <p className="error-text">{error}</p>;
    }

    if (!userId) {
        return <p className="placeholder-text">Please select a user to see their personalised recommendations.</p>;
    }
    
    return (
        <div className="recommendations-container">
            <h3>✨ Here Are Your Personalised Recommendations</h3>
            {recommendations.length > 0 ? (
                <div className="recommendations-list">
                    {recommendations.map((item, index) => (
                        <div key={`${item.product_id}-${index}`} className="recommendation-card">
                            <div>
                                <span className="category">{item.category}</span>
                                <h4>{item.name}</h4>
                            </div>
                            <div className="reason">
                                Because you and {item.similar_user_name} both purchased {item.shared_product_name}.
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <p>No new recommendations found for this user based on their purchase history.</p>
            )}
        </div>
    );
}

export default Recommendations;