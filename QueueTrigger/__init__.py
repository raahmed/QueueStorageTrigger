import logging
import azure.functions as func
import azure.cosmos.cosmos_client as cosmos_client

def main(msg: func.QueueMessage) -> None:
    body = msg.get_json()
    date = body['date']
    year, month, _ = date.split("T")[0].split("-")
    city = body['city']
    country = body['country']
    temperature = body['temperature']
    # Obtain HOST and MASTER_KEY from: https://portal.azure.com/#@[user_email]/resource/subscriptions/[subscription_id]/resourceGroups/[resource_group_name]/providers/Microsoft.DocumentDb/databaseAccounts/[db_account_name]/keys
    HOST = "//TODO"
    MASTER_KEY = "//TODO"
    # construct your own doc_link and document as needed. This is a sample.
    # Please see the readme for details regarding the code below.
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})
    database_link = 'dbs/' + 'weather-data'
    collection_link = database_link + '/colls/' + 'weather-data'
    doc_id = year + "-" + month + "___" + city + "-" + country
    doc_link = collection_link + '/docs/' + doc_id
    try:
        document = {'id' : doc_id,
            'city' : city,
            'country' : country,
            'Temperature_List' : [str(temperature)],
            'Month' : month,
            'Year' : year
            }
        client.CreateItem(collection_link, document)
    except:
        response = client.ReadItem(doc_link)
        response["Temperature_List"].append(str(temperature))
        client.UpsertItem(collection_link, response)
    logging.info('Python queue trigger function processed a queue item:')
