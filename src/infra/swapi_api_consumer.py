from typing import Type
from collections import namedtuple
import requests
from requests import Request


class SwapiApiConsumer:
    def __init__(self) -> None:
        self.get_starships_response = namedtuple(
            "GET_Starships", "status_code request response"
        )

    def get_starships(self, page: int) -> any:

        req = requests.Request(
            method="get", url="https://swapi.dev/api/starships/", params={"page": page}
        )
        req_prepared = req.prepare()

        response = self.__send_http_request(req_prepared)

        return self.get_starships_response(
            status_code=response.status_code, request=req, response=response.json()
        )

    @classmethod
    def __send_http_request(cls, req_prepared: Type[Request]) -> any:
        """
        Prepare a sessin and send http request
        :param - req_prepared: Request Objct with all params
        :response - Http response raw
        """

        http_session = requests.Session()
        reponse = http_session.send(req_prepared)
        return reponse
