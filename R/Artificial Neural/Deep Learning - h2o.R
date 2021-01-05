library(h2o)

h2o.init()

#importaremos arquivo para treino e de teste

treino = h2o.importFile(file.choose())
teste = h2o.importFile(file.choose())

head(treino)

# Transformar a classe em um tipo fator - classe coluna 785

treino[,785] = as.factor(treino[,785]) #todas linhas e coluna 785 p/ fator
teste[,785] = as.factor(teste[,785])

# Trabalhando efetivamente com deep_learning
# Epochs = Qtde de processos completos de treinamento (Ajuste peso e viés (bias)
#Criando modelo 

modelo = h2o.deeplearning(x = colnames(treino[,1:784]),y="C785",training_frame = treino, validation_frame = teste,distribution="AUTO",activation = "RectifierWithDropout",hidden=c(64,64,64),sparse = TRUE, epochs = 40)

plot(modelo)

#como selecionar o número de epochs ?????? menos melhor ?

h2o.performance(modelo)

# Erro observado = 0.0346 - > 3,46%

# Observando o teste:

treino[20,785]

pred=h2o.predict(modelo,newdata=treino[20,1:784])

pred$predict



