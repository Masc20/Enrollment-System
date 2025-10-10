from fastapi import APIRouter, Depends, status, Query

from app.db import get_db
from app.config import settings

# Schema/s
from app.schemas.enrollment_schema import *

# Services
from app.services.enrollment_service import *

router = APIRouter()

#TO DO:
#   create the secondary main end point of the API