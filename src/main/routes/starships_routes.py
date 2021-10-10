from fastapi import APIRouter, Request as RequestFastApi

starships_routes = APIRouter()


@starships_routes.get("/api/starships/list")
def get_starships_in_pagination(request: RequestFastApi):
    """get_starships_in_pagination"""
    print(request.query_params)
    print(request.query_params["page"])

    return "Olá mundo from FastApi"
