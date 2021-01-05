describe pessoas; # ver a tabela 

alter table pessoas # quero alterar tabela pessoas 
add column profissao varchar(10); #adicionada em um último campo

alter table pessoas
drop column profissao; # excluir profissão


alter table pessoas # quero alterar tabela pessoas 
add column profissao varchar(10) AFTER nome; 

alter table pessoas # quero alterar tabela pessoas 
add codigo int first;

#Mudando estrutura;

alter table pessoas
modify column profissao varchar(20);

#Renomear coluna CHANGE

alter table pessoas

change column profissao prof varchar(20);

#Renomear tabela inteira

alter table pessoas
rename to gafanhotos;



select * from pessoas