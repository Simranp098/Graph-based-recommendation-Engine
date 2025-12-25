# Graph-based-recommendation-Engine
Built a graph-based recommendation system where users and items are modeled as nodes connected by interactions. Applied graph traversal and scoring techniques to analyze relationships and generate personalized recommendations, demonstrating practical use of graph algorithms, data structures, and Python.


## 📖 Project Overview

This project is a full-stack E-Commerce Recommendation System designed to solve the "Black Box" problem of traditional algorithms. Unlike standard SQL-based systems, this engine utilizes a Graph Database (Neo4j) to model complex relationships between Users, Products, and Transactions.

The core innovation is Explainable AI (XAI). The system provides transparency by generating natural language explanations for every recommendation (e.g.,"Recommended because you and Robert Gonzales both bought Mobile"), helping build user trust and engagement.


## ✨ Key Features

High-Performance Graph Traversal: Utilizes Neo4j's index-free adjacency to perform real-time Collaborative Filtering queries in milliseconds.
Explainable Recommendations: Extracts specific graph paths to explain *why* a product was suggested (Target User → Shared Item → Neighbor → Recommended Item).
Dynamic User Dashboard: A responsive React.js frontend that allows switching between user profiles to see personalized results instantly.
🛠️ Scalable Architecture: Decoupled architecture using FastAPI (Backend) and React (Frontend) ensures scalability and maintainability.

---

## 🏗️ Tech Stack

| Component       | Technology      | Description 
| :---            | :---            |  :--- 
| Frontend        | React.js        | Single Page Application (SPA) for the user interface. 
| Backend         | Python (FastAPI)| High-performance API handling business logic. 
| Database        | Neo4j           | Graph database storing Users (:User) and Products (:Product). 
| Query Lang      | Cypher          | Used for efficient graph pattern matching. 
| Data Processing | Pandas          | Used for preprocessing CSV datasets before loading. 

---

## 📂 Project Structure

```bash
Graph-Recommendation-Engine/
├── backend/
│   ├── app/
│   │   ├── models/         # Pydantic schemas (Data Validation)
│   │   ├── routes/         # API endpoints (GET /recommendations)
│   │   ├── services/       # Business logic (Recommender Algorithm)
│   │   └── main.py         # Entry point & CORS setup
│   ├── Dataset/            # CSV files (users.csv, products.csv, purchased.csv)
│   ├── load_data.py        # ETL Script to populate Neo4j
│   └── neo4j_connection.py # Database driver management
├── frontend/
│   ├── src/
│   │   ├── components/     # Reusable UI cards
│   │   ├── App.js          # Main frontend logic
│   │   └── api.js          # Axios calls to Backend
│   └── package.json
└── README.md
