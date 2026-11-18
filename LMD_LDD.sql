
CREATE TABLE Palmares (
    Annee      INT     NOT NULL,
    NOC        CHAR(3) NOT NULL,
    Rang       INT,
    Nb_Or      INT DEFAULT 0,
    Nb_Argent  INT DEFAULT 0,
    Nb_Bronze  INT DEFAULT 0,
    Total      INT ,
    PRIMARY KEY (Annee, NOC)
);

LOAD DATA INFILE 'Olympics (1896-2024).csv' INTO TABLE Palmares
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Annee, NOC, Rang, Nb_Or, Nb_Argent, Nb_Bronze);


SELECT *
FROM Palmares
WHERE Nb_Or > 30;

SELECT * 
FROM Palmares
WHERE NOC LIKE 'F%';

SELECT * 
FROM Palmares
WHERE Nb_Or > 20
AND Nb_Argent > 20;

SELECT * 
FROM Palmares
WHERE NOC IN ('USA', 'FRA', 'CHN');

SELECT P1.Annee, P1.NOC, P1.Rang 
FROM Palmares P1, Palmares P2
WHERE P1.NOC = P2.NOC
AND P1.Annee = P2.Annee;

SELECT P1.Annee, P1.NOC, P1.Rang 
FROM Palmares P1, Palmares P2
WHERE P1.Rang = P2.Rang;

SELECT P1.Annee, P1.NOC, P1.Rang 
FROM Palmares P1, Palmares P2, Palmares P3
WHERE P1.NOC = P2.NOC
AND P2.Rang = P3.Rang;

SELECT P1.Annee, P1.NOC, P1.Rang 
FROM Palmares P1, Palmares P2, Palmares P3, Palmares P4
WHERE P1.NOC = P2.NOC
AND P2.Rang = P3.Rang
AND P3.Annee = P4.Annee;

SELECT NOC, SUM(Nb_Or) AS total_or 
FROM Palmares
GROUP BY NOC
HAVING SUM(Nb_Or) > 50;

SELECT Annee, COUNT(DISTINCT NOC) AS nb_pays
FROM Palmares
GROUP BY Annee
HAVING COUNT(DISTINCT NOC) > 10;

SELECT DISTINCT P1.NOC
FROM Palmares P1
WHERE EXISTS (
    SELECT 1
    FROM Palmares P2
    WHERE P2.NOC = P1.NOC
    AND P2.Nb_Or > 0
);

SELECT DISTINCT P1.NOC
FROM Palmares P1
WHERE NOT EXISTS (
    SELECT 1
    FROM Palmares P2
    WHERE P2.NOC = P1.NOC
    AND P2.Nb_Or > 0
);

SELECT DISTINCT NOC   
FROM Palmares
WHERE Nb_Or > 0
AND NOC NOT IN (
    SELECT NOC
    FROM Palmares
    WHERE Nb_Argent > 0
);
