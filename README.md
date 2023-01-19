# API-based parser xe.com

This is one of my interview tasks.
[The task](https://github.com/Tsarikovich/api-converter-interview-task/blob/master/task.pdf) itself.

## Getting Started


### Prerequisites

- Python 3.11.0
- Locally installed MongoDB

### Installing

Install dependencies

    pip install -r requirements.txt

Then simply run

    python main.py


## How to use

### Add api-key
Firstly, you need to create a database in mongodb called **"api-converter"** and collection called **"api-keys"**. Then provide the collection with the document containing value of your api-key.
<br><br>
The structure of the collection should be like that:

    [{
      "value": "A1234568"
    }]

### Make a request

#### Convert request

    POST http://127.0.0.1:7777/convert?amount=60&from_currency=USD&to_currency=RUB

And remember to send the api-key you have created previously in header

    'Authorization': 'Bearer yourApiKey'

Result:

    {
      "converted_amount": 4134.51,
      "rate": 68.9085,
      "metadata": {
          "time_of_conversion": 1674051606.361781,
          "from_currency": "USD",
          "to_currency": "RUB"
      }
    }

#### Currencies request

    GET http://127.0.0.1:7777/currencies


#### History request

    GET http://127.0.0.1:7777/history
