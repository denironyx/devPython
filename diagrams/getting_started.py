# diagram.py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.saas.analytics import Snowflake
from diagrams.azure.database import BlobStorage
from diagrams.azure.integration import EventGridSubscriptions
from diagrams.azure.storage import QueuesStorage

from diagrams import Cluster
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache
from diagrams.aws.network import Route53

with Diagram("Web Service", show = False):
    ELB("lb") >> EC2("web") >> RDS("userdb")

with Diagram("Grouped Workers", show=False, direction="TB"):
    ELB("lb") >> [EC2("Worker1"),
                  EC2("Worker2"),
                  EC2("Worker3"),
                  EC2("Worker4"),
                  EC2("Worker5")] >> RDS("events")

# Clustered Web Servicess
with Diagram("Clusered Web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]
    
    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached >> Snowflake("snowflake")

# Snowflake snowpipe functions
with Diagram("Snowpipe Pipeline", show=False):
    dns = Route