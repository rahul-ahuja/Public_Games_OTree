# Technical Assessment for BSCI SRSE Summer 2025
A technical assessment for SRSE candidates for the Behavioural Science group at WBS, focussing on fixing an oTree experiment.

Instructions to run the applications

pip install -r requirements.txt
docker build . -t otree_db
docker run --name otree-postgres -p 5432:5432 -d otree_db
export DATABASE_URL=postgresql://postgres:mypassword@localhost:5432/otree
otree resetdb

docker exec -it otree-postgres psql -U postgres -d otree
CREATE ROLE non_researcher NOINHERIT LOGIN PASSWORD 'non_researcher';
GRANT SELECT ON TABLE public.otree_participant TO non_researcher;


otree devserver 
127.0.0.1:8000


otree runprodserver
http://0.0.0.0:8000/