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

set `USERNAME` and `PASSWORD` to whatever you want. Then create a file called `config.json` in the same directory as `base.py` and add the password and username you chose using the following format:

```
{
"password": "PASSWORD",
"user": "USERNAME"
}
```

Some example queries are in `ref_queries.py`, to give a few examples of how to access data in the DB.

Its very barebones - I haven't added anything for deleting or updating entries, so its not quite CRUD... mainly cruddy. Since half the time at work I end up adding these functions, I'll update the repo to include these soon.