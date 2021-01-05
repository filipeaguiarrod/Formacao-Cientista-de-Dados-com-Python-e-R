#install.packages('RPostgreSQL',dependencies=T)

library('RPostgreSQL')


#PostgreSQL, db = data base, host= minha máquina local, port=standard, user = std e password = eu criei
conexao = dbConnect("PostgreSQL",db="DS", host="localhost",port=5432,
                    user="postgres", password="sadafi")               

sql = "select quantidade, valortotal, produto, total from itensvenda iv
        inner join vendas v on (iv.idvenda=v.idvenda)
        inner join produtos p on (p.idproduto=iv.idproduto)"


# variável vira dataframe que posso executar tudo que eu quero 
vendas = dbGetQuery (conexao, sql)
