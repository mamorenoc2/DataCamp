CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    salario REAL
);

INSERT INTO empleados (nombre, edad, salario)
VALUES 
('Ana', 25, 2000),
('Luis', 30, 3000);

SELECT * FROM empleados;