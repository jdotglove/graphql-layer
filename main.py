# Module used as main code executor
from fastapi import Security, Depends, FastAPI, HTTPException, Response
from fastapi.security.api_key import APIKeyQuery, APIKeyCookie, APIKeyHeader, APIKey
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, JSONResponse
from strawberry.fastapi import GraphQLRouter

from src import config
from src.graphql.schema import schema

api_key_header = APIKeyHeader(name=config.API_KEY_NAME, auto_error=False)

graphql_app = GraphQLRouter(schema)
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.include_router(graphql_app, prefix="/graphql")

async def get_api_key(
    api_key_header: str = Security(api_key_header),
):
    if api_key_header == config.API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )

# Order matters for route declaration

# @app.put("/secure_endpoint/update", response_model=str, tags=["test"])
# async def get_secure_endpoint(updateMessage: MessageRequest, api_key: APIKey = Depends(get_api_key)):
#     responseMessage = updateMessage.body[::-1]
#     return responseMessage

# @app.get("/secure_endpoint", response_model=str, tags=["test"])
# async def get_secure_endpoint(response: Response, api_key: APIKey = Depends(get_api_key)):
#     message = "How cool is this?" 
#     return message