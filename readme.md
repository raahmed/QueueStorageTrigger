# QueueTrigger - Python

The `QueueTrigger` makes it incredibly easy to react to new Queues inside of Azure Queue Storage. This sample demonstrates a simple use case of processing data from a given Queue.

## How it works

For a `QueueTrigger` to work, you provide a path which dictates where the queue messages are located inside your container.

## Learn more

Documentation:

To execute function properly, configure the keys in this folder:
1) HOST and MASTERKEY must be set in __init__.py for the CosmosDB used.
2) 'AzureWebJobsStorage' must have an accurate value in local.settings.json
3) The CosmosDB used must have a database called 'weather-data' and a collection within that, which is also called 'weather-data'.
4) The queue name must be 'weather-data', as that is the name set in function.json.

If you wish to change the DB/Collection/Queue names, you can free free to do so. Just remember to change them for the entire pipeline (both functions and the web component)
