import os
import json
from pymongo import MongoClient


class DataBaseHandler:
    def __init__(self):
        port = int(os.environ['DB_PORT'])
        db_name = os.environ['DB_NAME']

        client = MongoClient('database', port)
        self.db = client[db_name]
        # We use the same name for the collection as we do for the database, since we only have a single collection.
        self.collection = self.db[db_name]

    def get_all_atm(self):
        """

        :return:
        """
        all_atms = list(self.collection.find())
        return all_atms

    def get_atm_by_canton(self, canton_name: str):
        """

        :param canton_name:
        :return:
        """
        return list(self.collection.find({
            "canton": canton_name
        }))

    def get_atm_on_operator_name(self, operator_name):
        """

        :param operator_name:
        :return: list of ATMs
        """
        atms = list(self.collection.find({'operator': operator_name}))
        return atms

    def get_atm_by_canton_and_operator_name(self, operator_name, canton):
        """

        :param operator_name:
        :param canton:
        :return: list of ATMs
        """
        return list(
            self.collection.find({
                "operator": operator_name,
                "canton": canton,
            })
        )

    def populate_database(self):
        """
        Drops the database, if it exists and re-creates it from the data/clean_data.json file.

        :return:
        """
        self.collection.drop()

        with open('data/clean_data.json') as file:
            file_data = json.load(file)

        if isinstance(file_data, list):
            self.collection.insert_many(file_data)
        else:
            self.collection.insert_one(file_data)

        return self


if __name__ == '__main__':
    db = DataBaseHandler()
    print(db.get_all_atm())
    print(db.get_atm_on_operator_name('UBS'))
