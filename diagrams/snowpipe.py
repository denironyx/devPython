from diagrams import Cluster, Diagram
from diagrams.azure.integration import EventGridSubscriptions
from diagrams.saas.analytics import Snowflake
from diagrams.azure.database import BlobStorage
from diagrams.azure.storage import QueuesStorage
from diagrams.azure.iot import IotHub
from diagrams.generic.storage import Storage
from diagrams.programming.flowchart import Database

with Diagram("HoverTouch Process Flow", show=False):
    blobstorage = BlobStorage("blob storage")
    stage = Storage("external stage")
    snowflake = Snowflake("Snowflake Table")
    eventgrid = EventGridSubscriptions("Events  Notification")
    pipe = Database("COPY INTO as defined in Pipe")
    queues = QueuesStorage("Ingest Queue")

    with Cluster("Source of Data"):
        [IotHub("Touch Wall"),
        IotHub("Touch Car"),
        IotHub("Touch Glass")] >> blobstorage
        
    blobstorage >> stage >> eventgrid >> queues >> pipe >> snowflake