CREATE TABLE IF NOT EXISTS users (
    id_user SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passw VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO users (username, passw, nombre) 
VALUES ('admin', 'admin!123', 'Super admin');

