from fastapi import APIRouter, Request as RequestFastApi
from src.main.adapters import request_adapter
from src.validator.get_starships_in_pagination_validator import get_pagination_validator
from src.main.adapters.request_adapter import request_adapter

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: RequestFastApi):
    """get_starships_in_pagination"""
    get_pagination_validator(request)
    await request_adapter(request, print)

    return "Olá mundo from FastApi"
