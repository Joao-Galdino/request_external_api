from cerberus import Validator

def get_pagination_validator(request: any):
    """ Pagination validator """
    query_param_validator = Validator({
        'page': {'type': 'string', 'allowed':['1', '2', '3', '4'],'required': True}
    })
    

    response = query_param_validator.validate(request.query_param)
     
    if response is False:
        raise Exception(query_param_validator.errors)


    print(query_param_validator.errors)
    print(response)