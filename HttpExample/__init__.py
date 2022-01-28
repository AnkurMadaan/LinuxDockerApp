import logging

import azure.functions as func

import numpy as np

import cx_Oracle

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    samplenumpy()
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    conn=startCon()
    resp=""

    if conn:
        resp="Connected to DB"
    else:
        resp="Unable to connect to DB"

    endCon(conn)

    if name:
        return func.HttpResponse(f"{resp} Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             f"{resp} This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    

def startCon():
    dsn=cx_Oracle.makedsn(
        '',
        '1521',
        sid=''
    )
    conn = cx_Oracle.connect(
        user='',
        password='',
        dsn=dsn
    )

    return conn

def endCon(conn):
    conn.close()

def samplenumpy():
    logging.info(f"loaded numpy")
    array = np.array([
    [3, 7, 1],
    [10, 3, 2],
    [5, 6, 7]
    ])
    logging.info(array)
    # Sort the whole array
    logging.info(np.sort(array, axis=None))

