create database Venta;
Use Venta;

create table cliente (
idCliente INT(11) NOT NULL,
Documento VARCHAR(45) NULL DEFAULT NULL,
Nombre VARCHAR(45) NULL DEFAULT NULL,
PRIMARY KEY (idCliente));

CREATE TABLE vendedores(
idVendedores INT(11) NOT NULL,
Documento VARCHAR(45) NULL DEFAULT NULL,
nombre VARCHAR(45) NULL DEFAULT NULL,
PRIMARY KEY (idVendedores));

CREATE TABLE factura(
idFactura INT(11) NOT NULL,
fecha DATE NULL DEFAULT NULL,
cliente_idCliente INT(11) NOT NULL,
vendedores_idVendedores INT(11) NOT NULL,
PRIMARY KEY (idfactura),
CONSTRAINT fk_factura_cliente1
foreign key (cliente_idCliente)
references venta.cliente (idCliente),
CONSTRAINT fk_factura_Vendedores1
foreign key (Vendedores_idVendedores)
references venta.vendedores (idVendedores));

create table ejemplos (id int primary key, nombres int);
alter table ejemplos rename Auditor;/*renombrar la tabla*/
alter table auditor add fecha date after nombres;/*agregar un campo*/
alter table auditor change nombres nombres varchar(30);/*cambiar el tipo de dato*/

select * from auditor;
select nombres,fecha from auditor;

insert into auditor values (1, 'Goku yandel lopez','2026-03-09');
insert into auditor (id,nombres,fecha) values (2,'Vegeta Wisin Diaz','2026-03-09');
insert into auditor(id,nombres,fecha) values (3,'Naruto Anuel Vega','2026-03-09');
insert into auditor(id,nombres,fecha) values (4,'Diomedez kakashi','2026-03-09'),(5,'Crillin Villazon','2026-01-20');

select * from idatos;



update auditor set nombres='Silvestre saitama' where id=5;
update auditor set nombres='Westcol Yancha', fecha='2023-01-25' where id=3;

delete from auditor where id=1;

create table idatos (numero int, deci float, fecha date, fechahora datetime,
lista enum('Masculino','Femenino','bajo en sal','sin sal'));

insert into idatos values (3,1.3,now(),now(),'Masculino');