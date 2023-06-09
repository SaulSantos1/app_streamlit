# importando bibliotecas

import streamlit as st
import pandas as pd
import numpy as np
# importando arquivos

titanic = pd.read_csv('tested.csv')

# Colocando uma palavra para meu título 
st.sidebar.title('Menu')

# Abrindo uma caixa de seleções para identificar o item que desejo 
opcoes = st.sidebar.selectbox(
    'Selecione a opção',[
        'Sexo', 'Menores de 18 anos', 'Adultos','Não informaram idade' ,'Sobreviventes'])
# Especificando a opção que desejo por meio dos 'ifs'
if opcoes == 'Sexo':
    st.title('Titanic : Sexo dos passageiros e tripulantes')
    opcaoSex = st.selectbox('Escolha o sexo:',['','Masculino','Feminino'])
    if opcaoSex == 'Masculino':
        homem = titanic[titanic['Sex'] == 'male' ]
        homem[['Name','Age','Sex']]
        st.write('Total = ',len(homem))
    elif opcaoSex == 'Feminino': 
        mulher = titanic[titanic['Sex'] == 'female']
        mulher[['Name','Age','Sex']]
        st.write('Total = ',len(mulher))
if opcoes == 'Menores de 18 anos':
    st.title('Titanic : Menores de 18 anos')
    opcaoMenor = st.selectbox('Escolha a idade:',['','Entre 0 a 10 anos', 'Entre 11 a 17 anos'])
    if opcaoMenor == 'Entre 0 a 10 anos':
        crianca=titanic[titanic['Age'] <= 10]
        crianca[['Name','Age','Sex']]
        st.write('Total = ',len(crianca))
    elif opcaoMenor == 'Entre 11 a 17 anos': 
        adolescente = titanic[(titanic['Age'] >= 11) & (titanic['Age'] <= 17)]
        adolescente[['Name','Age','Sex']]
        st.write('Total = ',len(adolescente))
        
if opcoes == 'Adultos':
    st.title('Titanic : Adultos')
    idadeAdulto = st.selectbox('Escolha a idade:',['','Entre 18 a 35 anos','Mais de 35 anos'])
    if idadeAdulto == 'Entre 18 a 35 anos' :
        adulto = titanic[(titanic['Age'] >= 18) & (titanic['Age'] <= 35)]
        adulto[['Name','Age','Sex']]
        st.write('Total = ', len(adulto))
    elif idadeAdulto == 'Mais de 35 anos':
        adultoVelho = titanic[titanic['Age'] > 35]
        adultoVelho[['Name','Age','Sex']]
        st.write('Total = ', len(adultoVelho))
if opcoes == 'Não informaram idade':
    st.title('Titanic: Sem a informação da idade')
    semIdade = st.button('Pessoas sem informação da idade')
    if semIdade:
        sIdade = titanic.replace(np.nan,'') 
        sIdade = sIdade[sIdade['Age'] == '']
        sIdade[['Name','Age','Sex']]
        st.write('Total = ', len(sIdade))
if opcoes == 'Sobreviventes': 
    st.title('Titanic: Sobreviventes e Falecidos')
    opcaoSobrevivente = st.selectbox('Escolha uma opção:',['','Sobreviventes', 'Mortos'])
    if opcaoSobrevivente == 'Sobreviventes':
        sobreviventes = titanic[titanic['Survived'] == 1]
        sobreviventes[['Name','Age','Sex']]
        st.write('Total = ', len(sobreviventes))
    elif opcaoSobrevivente == 'Mortos':
        mortos = titanic[titanic['Survived'] == 0]
        mortos[['Name','Age','Sex']]
        st.write('Total = ', len(mortos))

#st.dataframe(dataframe[dataframe['Sex'] == sex])

