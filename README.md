# PostgreSQL/SQLAlchemy DB for Uniprot and PDB info

Barebones pattern used to set up a database for structural data of  proteins to save a huge amount of time with work projects and for MSc students I supervise who need to set up a DB/learn how to do it.

Easy to add more fields - modify the `Struc` or `Seq` classes and the `insert.py` functions to add or remove info you want in the database.

Set up for use in an interactive shell/notebook. Start with a Uniprot Acc no. (e.g. P99999) and use that to fetch sequence/structures/whatever using Uniprot REST API as a starting point.

I use Docker to set up the Postgresql DB - the following command is what I use to set it up and run the instance:
```
docker run --name pdb-uniprot-db \
    -e POSTGRES_PASSWORD=PASSWORD \
    -e POSTGRES_USER=USERNAME \
    -e POSTGRES_DB=db \
    -p 5432:5432 \
    -d postgres
```

set `USERNAME` and `PASSWORD` to whatever you want. As the data is not sensitive in any way I have not 