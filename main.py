# Module used as main code executor
from fastapi import Security, Depends, FastAPI, HTTPException, Response
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
# from fastapi.openapi.docs import get_swagger_ui_html
# from fastapi.openapi.utils import get_openapi
from starlette.status import HTTP_403_FORBIDDEN
# from starlette.responses import RedirectResponse, JSONResponse
from strawberry.fastapi import GraphQLRouter

from src import config
from src.dependencies import get_api_key
from src.graphql.schema import schema

graphql_app = GraphQLRouter(schema=schema, graphiql=True)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")



# Order matters for route declaration

# @app.put("/secure_endpoint/update", response_model=str, tags=["test"])
# async def get_secure_endpoint(updateMessage: MessageRequest, api_key: APIKey = Depends(get_api_key)):
#     responseMessage = updateMessage.body[::-1]
#     return responseMessage

# @app.get("/secure_endpoint", response_model=str, tags=["test"])
# async def get_secure_endpoint(response: Response, api_key: APIKey = Depends(get_api_key)):
#     message = "How cool is this?" 
#     return message