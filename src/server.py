import json

from flask import Flask, render_template, Response
from database_handler import DataBaseHandler

app = Flask(__name__)
db = DataBaseHandler()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/canton")
def cantons():
    """
    Displays a bar chart of all ATMs that can be filtered by canton.

    :return:
    """
    return render_template("canton.html")


@app.route("/map/<operator_name>")
@app.route("/map/<operator_name>/<canton>")
def show_map(operator_name: str, canton="null"):
    """
    Uses the bank_markers and logos of the banks.

    :return: the map with logos of the banks
    """
    return render_template('map.html', operator_name=operator_name, canton=canton)


@app.route("/api/atm")
def get_atm():
    """
    Uses the MongoDB Connector class and returns all ATMs.

    :return:
    """
    data = db.get_all_atm()

    response = Response(json.dumps(data, default=str))

    # Set the Content-Type to JSON so that the response is displayed nicely in the browser.
    response.headers.add('Content-Type', 'application/json')
    # Allow access through the IP. Without this header we'd encounter a CORS error.
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/api/atm/<operator_name>")
@app.route("/api/atm/<operator_name>/<canton>")
def get_atm_by_operator(operator_name: str, canton=None):
    """
    Uses the MongoDB Connector class and returns all ATMs filtered by the operator bank.

    :param operator_name: operator (name of the bank)
    :param canton:
    :return:
    """
    response = Response()

    if canton is None:
        data = db.get_atm_on_operator_name(operator_name)
    else:
        data = db.get_atm_by_canton_and_operator_name(operator_name, canton)
        print(data)

    if len(data) == 0:
        response.status = 404

    response.data = json.dumps(data, default=str)

    # Set the Content-Type to JSON so that the response is displayed nicely in the browser.
    response.headers.add('Content-Type', 'application/json')
    # Allow access through the IP. Without this header we'd encounter a CORS error.
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route("/api/atm/canton/<canton_name>")
def get_atm_by_canton(canton_name: str):
    """

    :param canton_name: The name of the canton entered.
    :return:
    """
    response = Response()

    data = db.get_atm_by_canton(canton_name)

    response.data = json.dumps(data, default=str)

    # Set the Content-Type to JSON so that the response is displayed nicely in the browser.
    response.headers.add('Content-Type', 'application/json')
    # Allow access through the IP. Without this header we'd encounter a CORS error.
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    db.populate_database()
    app.run(host='0.0.0.0', port=14032)
