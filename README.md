# Modified Public Game in OTree

# Overview

This is an extension of the public goods game in OTree https://otree.readthedocs.io/en/latest/tutorial/part2.html
In this modified public goods game, there can be any multiple number of players.


# Instructions to setup the application and PostgreSQL database from Docker. Below are commands to be executed in the terminal

```
pip install -r requirements.txt

docker build . -t otree_db
docker run --name otree-postgres -p 5432:5432 -d otree_db
export DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/otree
otree resetdb
```

# Instructions to run the application

```
otree devserver 
127.0.0.1:8000

otree runprodserver # to run in the production environment 
http://0.0.0.0:8000/
```