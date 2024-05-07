
create table cliente
(
id int auto_increment primary key,
nome varchar(80) not null,
email varchar(80) not null,
data_cad timestamp default current_timestamp
)Engine = innoDB;

create table noticias_email
(
id_noticias INT not null auto_increment,
email Varchar(80) not null,
primary key (id_noticias))
Engine = InnoDB

DELIMITER $$
CREATE TRIGGER after_insert_cliente
AFTER INSERT ON cliente
FOR EACH ROW
BEGIN
    INSERT INTO noticias_email (email)
    VALUES (NEW.email);
END$$
DELIMITER ;

INSERT INTO cliente (nome, email) VALUES
('Cliente 1', 'cliente1@example.com'),
('Cliente 2', 'cliente2@example.com'),
('Cliente 3', 'cliente3@example.com'),
('Cliente 4', 'cliente4@example.com'),
('Cliente 5', 'cliente5@example.com'),
('Cliente 6', 'cliente6@example.com'),
('Cliente 7', 'cliente7@example.com'),
('Cliente 8', 'cliente8@example.com'),
('Cliente 9', 'cliente9@example.com');

select * from noticias_email;

Drop table cliente