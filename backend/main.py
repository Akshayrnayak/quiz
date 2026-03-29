from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from quiz_data import get_categories, get_questions_by_category

app = FastAPI(title="W3Schools-like Quiz App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Category(BaseModel):
    id: str
    title: str
    description: str

class Question(BaseModel):
    id: int
    text: str
    options: List[str]
    correct_answer: int

class QuestionResponse(BaseModel):
    category: str
    questions: List[Question]

class LeaderboardEntry(BaseModel):
    username: str
    score: int
    total: int
    topic: str

# In-memory leaderboard database
leaderboard_db: List[LeaderboardEntry] = []

@app.get("/api/categories", response_model=List[Category])
def fetch_categories():
    categories = get_categories()
    if not categories:
        raise HTTPException(status_code=500, detail="Failed to load categories")
    return categories

@app.get("/api/questions/{category_id}", response_model=QuestionResponse)
def fetch_questions(category_id: str):
    questions = get_questions_by_category(category_id)
    if not questions:
        raise HTTPException(status_code=404, detail="Category not found or no questions available")
    return {"category": category_id, "questions": questions}

@app.get("/api/leaderboard", response_model=List[LeaderboardEntry])
def get_leaderboard():
    # Sort leaderboard by highest score, then by topic for simple sorting
    sorted_lb = sorted(leaderboard_db, key=lambda x: (x.score / x.total if x.total > 0 else 0), reverse=True)
    return sorted_lb

@app.post("/api/leaderboard", response_model=LeaderboardEntry)
def post_leaderboard(entry: LeaderboardEntry):
    leaderboard_db.append(entry)
    return entry
