"""User App API Routes"""

from typing import List
from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.orm import Session

from core import database

from app.point import schemas
from app.point.api.v1 import service


router = APIRouter(prefix="/api/v1/point", tags=["point"])

@router.get('/')
def hello():
    return "point"