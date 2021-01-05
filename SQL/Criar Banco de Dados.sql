create database cadastro 
default character set utf8 # caracteres acentuados no padrao PT-BR
default collate utf8_general_ci;

create database meubank;
drop database meubank;

use cadastro;

CREATE TABLE PESSOAS(
id int NOT NULL auto_increment, # Campo nao pode ser vazio e vai incrementar 
NOME varchar(30) NOT NULL,# obriga que nao seja branco para criar registro
NASCIMENTO date, # cadastrar dia de nascimento pois idade muda
SEXO enum('M','F'), # coleção que só permite usar ou M ou F
PESO decimal(5,2), # Cinco casas com 2 números depois da vírgula
ALTURA decimal(3,2),
NACIONALIDADE varchar(20) DEFAULT 'Brasil', # se ninguém digitar nada ele preenche com brasil
primary key (id) # usa id como chave primária
)default charset utf8; #defini o tipo de caractere 