"""

Creates:
 engine to interact with dockerised postgresql db
 ORM session
 base class for class definintions e.g. Movie, Actor etc.

 # create a PostgreSQL instance
docker run --name pdb-uniprot-db \
    -e POSTGRES_PASSWORD=PASSWORD \
    -e POSTGRES_USER=USERNAME \
    -e POSTGRES_DB=db \
    -p 5432:5432 \
    -d postgres

"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
import json

"""
# create a file called config.json with the following format:

{
"password": "x",
"user": "y"
}

where x and y are the password and username you picked when instantiating the docker instance.

"""
with open(os.path.join(os.getcwd(), "config.json"), "r") as confin:
	config = json.loads(confin.read())

USERNAME = config["user"]
PASSWORD = config["password"]

engine = create_engine('postgresql://'+USERNAME+':'+PASSWORD+'@localhost:5432/db',
		pool_pre_ping=True,
	    connect_args={
	        "keepalives": 1,
	        "keepalives_idle": 30,
	        "keepalives_interval": 10,
	        "keepalives_count": 5,       ### this stuff stops operational errors I was having
	    }
    )

Session = sessionmaker(bind=engine)

Base = declarative_base()

