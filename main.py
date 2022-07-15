from typing import Union
from fastapi import FastAPI, Request
from typing import Optional
from fastapi import Header, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

@app.post('/')
async def read_root(request: Request):
    # import pdb; pdb.set_trace()
    return await request.json()


class PermissionRequest(BaseModel):  # pylint: disable=too-few-public-methods
    """
    PermissionRequest contains a single json object that can be hydrated into a
    cadmus PermissionRequest message.
    """
    checks: dict


@app.get('/permission-check')
async def permission_check(request: PermissionRequest, response: Response, authorization: Optional[str] = Header(None)) -> Response:
    if not authorization:
        raise HTTPException(detail='No authorization Header')
    
    _, access_token = authorization.split(" ")

    # import pdb; pdb.set_trace()

    data = {"checks": request.checks, "token": access_token}

    return data