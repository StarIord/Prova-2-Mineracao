from os import rename
import pandas as pd
import matplotlib.pyplot as ptl

titanic=pd.read_csv('./titanic.csv')
#Questão a
print(titanic.head(10))#mostra as 10 primeiras entradas
#Questão b
titanic.sort_values(by=['Name'],ascending=True,inplace=True)#ordena em ordem alfabética
print(titanic.head(10))
#Questão c
titanic['Sobrevivente']=titanic['Survived'].map({1:'sim',0:'não'})# cria uma coluna com o nome sobrevivente com valores de sim e não.
print(titanic.head(10))
#Questão d
titanic=titanic.drop(columns=['SibSp'])#retira a coluna SibSp
titanic=titanic.drop(columns=['Parch'])#retira a coluna Parch
titanic=titanic.drop(columns=['Ticket'])#retira a coluna ticket
print(titanic.head(10))
#Questão e
titanic=titanic.rename({'PassengerId':'Id_do_Passageiro','Survived':'Sobreviveu','Pclass':'Classe_do_passageiro','Name':'Nome','Sex':'Sexo','Age':'Idade','Fare':'Tarifa','Cabin':'Cabine','Embarked':'Embarcou'},axis='columns') #renomeia as colunas
print(titanic.head(10))
#Questão f
titanic['Sexo']=titanic['Sexo'].replace(['male'],['masculino'])# troca a palavra male para masculino
titanic['Sexo']=titanic['Sexo'].replace(['female'],['FEMININO'])# troca a palavra female para FEMININO
print(titanic.head(10))
#Questão g
sobreviventes=titanic.groupby(['Classe_do_passageiro','Sobrevivente']).size()#apresenta o numero de sobreviventes por classe
print(sobreviventes.head())
#Questão h
mortos=titanic.groupby(['Sexo','Sobrevivente']).size()#apresenta o numero de mortos por sexo
print(mortos.head())
#Questão i
sobreviventes.plot(kind='bar')#monta um gráfico do tipo barra.
ptl.show()
#Quetão j
titanic.to_excel('titanic.xlsx', index = False,header=True)#exporta o arquivo para xlsx.
