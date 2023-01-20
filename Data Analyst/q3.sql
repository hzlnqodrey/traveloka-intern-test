
given table:
1. people table
2. companies table
3. location table

people table
field -> [id, name, company_id]
insert ->
1, Chris, 3
2, James, 1
3, Carla, 2
4, Sherlock, 1

companies table
field -> [id, name, location_id]
insert ->
1, Aberton Inc, 1,
2, Belfast Food, 2,
3, London Law Firm, 1,

locations table
field -> [id, name]
insert ->
1, London
2, Belfast
3, Edenburgh

OUTPUT: GET  PLACE AND PEOPLE GROUP BY the most top LOCATION_ID 
-> PEOPLE.NAME, COMPANIES.NAME
