CREATE database Käyttäjä
use Käyttäjä
CREATE TABLE Käyttäjä_tbl 
(
     Käyttäjä_id INTEGER PRIMARY KEY,
     Firstname VARCHAR(100),
     Lastname VARCHAR(100),
     Salary float,
     MobileNo varchar(15)
     start_date Date, 
     room_number INTEGER,
     FOREIGN_KEY 
     email varchar(50),
); 
insert into Käyttäjä_tbl values(5, 'Ville','Valtteri',50000,'0458520960')  
select * from Käyttäjä_tbl
update Käyttäjä_tbl set FirstName='Vaskerio' where Käyttäjä=3 

CREATE database Tehtävä
use Tehtävä
CREATE TABLE Tehtävä_tbl 
(
     Tehtävä_id INTEGER PRIMARY KEY,
     Firstname VARCHAR(100),
     Lastname VARCHAR(100),
     Salary float,
     MobileNo varchar(15)
     start_date Date, 
     room_number INTEGER, 
     FOREIGN_KEY 
     email varchar(50),
); 
insert into Tehtävä_tbl values(3, 'Veera','Valentiina',60000,'0458017611')  
select * from Tehtävä_tbl
update 

CREATE database Task
use Task
CREATE TABLE Task_tbl 
(
     Task_id INTEGER PRIMARY KEY, 
     Firstname VARCHAR(100),
     Lastname VARCHAR(100), 
     Salary float,
     MobileNo varchar(15) 
     start_date Date, 
     room_number INTEGER, 
     FOREIGN_KEY
     email varchar(50),
); 
insert into Task_tbl values(4, 'Markus','Oskari',70000,'0503529889') 
select * from Task_tbl 

Task_id INTEGER, 
Tehtävä_id INTEGER,
Käyttäjä_id INTEGER, 