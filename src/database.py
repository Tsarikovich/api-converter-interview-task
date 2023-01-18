import datetime

from pymongo import MongoClient


class Database:
    client = MongoClient()

    transaction = client['api-converter']['transactions']
    users_api_keys_collection = client['api-converter']['api-keys']

    @staticmethod
    def save_transaction(
        amount: int, from_currency: str, to_currency: str, result: float
    ):
        document = {
            'converted_amount': result,
            'rate': result / amount,
            'metadata': {
                'time_of_conversion': datetime.datetime.now().timestamp(),
                'from_currency': from_currency,
                'to_currency': to_currency,
            },
        }

        Database.transaction.insert_one(document)
        document.pop('_id')
        return document

    @staticmethod
    def show_history():
        docs = []
        for doc in Database.transaction.find({}):
            doc.pop('_id')
            docs.append(doc)

        print(docs)
        return docs
