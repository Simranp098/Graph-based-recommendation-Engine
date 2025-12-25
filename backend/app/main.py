from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # 1. IMPORT THIS
from .routes import recommendations

app = FastAPI()

# 2. DEFINE THE ALLOWED ORIGINS ( REACT APP)
origins = [
    "http://localhost:3000",
]

# 3. ADD THE MIDDLEWARE TO YOUR APP
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)

app.include_router(recommendations.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Graph Recommendation Engine API"}