from fastapi import APIRouter, Request as RequestFastApi
from src.validator.get_starships_in_pagination_validator import get_pagination_validator
starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
def get_starships_in_pagination(request: RequestFastApi):
    """get_starships_in_pagination"""
    get_pagination_validator(request)

    return "Olá mundo from FastApi"



# Bom dia!
# Segue informativo de atualização dos Dashboards do BI:

# °Direcional - 04:09
# °Plimor - 03:02
# °Plimor - 03:02

# *Atualizados - Leve

# Controle Operacional - 09:12
# Devolução - 09:02
# Scan Rate - 10:03
# Volumetria - 07:13
# SLA - 09:58
# SFx - 10:01
# Pedidos em Aberto - 09:28
# Transferência - 06:01