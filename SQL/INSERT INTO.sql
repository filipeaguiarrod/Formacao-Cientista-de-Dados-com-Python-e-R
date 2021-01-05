use cadastro; # utilizar DB cadastro

INSERT INTO pessoas
(id,nome, nascimento, sexo, peso, altura, nacionalidade)

VALUES
(DEFAULT,'Creuza','1920-12-30','F','50.2','1.65',DEFAULT);

# Caso eu siga a sequencia eu posso simplesmente:

INSERT INTO pessoas VALUES
(DEFAULT,'Ana','1975-12-22','F','52.3','1.45','EUA'),
(DEFAULT,'Pedro','2000-07-15','M','52.3','1.45',default),
(DEFAULT,'Maria','1999-05-30','F','75.9','1.70','Portugal');



select * from pessoas