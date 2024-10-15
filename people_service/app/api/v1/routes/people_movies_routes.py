from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


@router.get("/persons/{person_id}/movies")
def get_person_movies(person_id: int):
    return {"endpoint": "get_person_movies"}


@router.post("/persons/{person_id}/movies")
def add_movie_to_person(person_id: int):
    return {"endpoint": "add_movie_to_person"}


@router.delete("/persons/{person_id}/movies")
def remove_movie_from_person(person_id: int):
    return {"endpoint": "remove_movie_from_person"}
