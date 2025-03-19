from datetime import timedelta
from contextlib import nullcontext as does_not_raise

import pytest

from src.auth.token import create_token, decode_token
from src.auth.exception import InvalidTokenError, ExpiredTokenError


@pytest.mark.parametrize(
    "minute, expectation",
    [
        (0, pytest.raises(ExpiredTokenError)),
        (1, does_not_raise()),
    ]
)
@pytest.mark.asyncio
async def test_decode_access_token(minute, expectation):
    data = {"email": "test_email"}
    
    token = create_token(data, timedelta(minutes=minute))
    
    with expectation:
        payload = decode_token(token)

