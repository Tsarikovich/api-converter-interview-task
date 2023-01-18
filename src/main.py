import uvicorn
from database import Database
from fastapi import Depends
from fastapi_config import api_key_auth, app
from xeparser import XEParser


@app.post('/convert', dependencies=[Depends(api_key_auth)])
async def convert(amount: int, from_currency: str, to_currency: str):
    value = await XEParser.convert(amount, from_currency, to_currency)

    result = Database.save_transaction(
        amount, from_currency, to_currency, value
    )

    return result


@app.get('/currencies', dependencies=[Depends(api_key_auth)])
async def get_currencies():
    return await XEParser.get_currencies()


@app.get('/history', dependencies=[Depends(api_key_auth)])
async def history():
    return Database.show_history()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=7777)
