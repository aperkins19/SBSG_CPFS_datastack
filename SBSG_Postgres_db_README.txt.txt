
The database uses the postgres docker image:

It is IMPORTANT to understand that the data is stored in the container only unless it is mounted to a local directory.
If it is not then the database is deleted with the container.
In the longterm, we shall decide on a permanent home for the database.

a good overview
https://www.youtube.com/watch?v=G-5c25DYnfI

tempory home:
"C:\Users\Alex Perkins\OneDrive - University of Edinburgh\coding\data_analysis_dockers\CFPS datastack\metadata write gui\SBSG_Postgres_db"

placeholder password: cellfr34eva


first time setup:

docker run --name SBSG_Postgres_db_image -e POSTGRES_PASSWORD=cellfr34eva -p 5432:5432 -v "C:\Users\Alex Perkins\OneDrive - University of Edinburgh\coding\data_analysis_dockers\CFPS datastack\metadata write gui\SBSG_Postgres_db":/var/lib/postgresql/data -d postgres

walkthough of tags:

--name: name of container
-e: evironment variable that set the password for accessing the database on first time set up
-p: maps the ports from local:container
-v: mounts the container on to local directory
-d: runs in detached mode.