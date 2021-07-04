# Projeto Séries Temporais Covid-19

[<img src="https://img.shields.io/badge/author-Carolina%20Dias-FB3799?style=flat-square"/>](https://github.com/diascarolina) [<img src="https://img.shields.io/badge/carodias-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/carodias/) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/diascarolina/projeto-series-temporais-covid/blob/main/LICENSE)
 
![image](https://user-images.githubusercontent.com/33383955/124374332-d0a73900-dc70-11eb-913b-7aac931fc3e5.png)

# Sumário

1. [Introdução](#intro)
2. [Dados](#data)
3. [Análises](#analise)
4. [Conclusões](#conc)
5. [Propostas de Melhoria](#props)
6. [Ferramentas & Bibliotecas](#libs)
7. [Referências](#refs)
8. [Agradecimentos](#agra)
9. [Contatos](#contact)


<a name="intro"></a>
# 1 Introdução

No momento que atingimos a triste marca de meio milhão de mortos pela Covid-19 só no Brasil, cabe a nós uma reflexão sobre esse cenário que estamos vivenciando. Cabe a nós buscar alguma "luz no fim do túnel", luz essa em formato de vacina e também de impeachment.

Nesse contexto, busco trazer uma breve análise sobre as curvas de novos casos e novos óbitos por Covid-19 no Ceará. Além disso, são trazidas previsões que podem nos ajudar a entender para onde esses números estão tendendo. Números não, vidas!


**Ciência de Dados na Pandemia de Covid-19 no Ceará?!**

Em 2020 e em 2021 a [Secretaria de Saúde do Estado do Ceará](https://www.saude.ce.gov.br/) realizou diversas ações convidando a própria comunidade de ciência de dados a ajudar nos esforços contra a doença, fornecendo análises e previsões acerca dos dados abertos fornecidos pelo próprio SUS. Esse concurso é bem explicado no link a seguir. Vale a pena a leitura, pois também fornece um enorme contexto para o uso de ciência de dados na saúde.

- [Sesa busca propostas de ferramentas para prever curva da Covid-19](https://diariodonordeste.verdesmares.com.br/metro/sesa-busca-propostas-de-ferramentas-para-prever-curva-da-covid-19-1.3009707)

Com isso também foi lançado o [IntegraSUS Analytics](https://integrasusanalytics.saude.ce.gov.br/pt/home), plataforma do Governo do Ceará de Ciência de Dados relacionada à Covid-19.

- [Secretaria da Saúde do Ceará lança plataforma de dados IntegraSUS Analytics](http://www.issec.ce.gov.br/index.php/assessoria-de-comunicacao/listanoticias/932-secretaria-da-saude-do-ceara-lanca-plataforma-de-dados-integrasus-analytics)

<a name="data"></a>
# 2 Dados

Nesse projeto foram obtidos os dados de casos e óbitos por Covid-19 no Ceará no site do [Brasil.io](https://brasil.io/home/), um excelente repositório de dados públicos do nosso país.

Foi selecionado o dataset principal sobre a doença, disponível em: [Covid-19 - Brasil.io](https://brasil.io/dataset/covid19/caso_full/)

O próprio site nos diz que:

> Essa tabela possui os casos confirmados e óbitos obtidos dos boletins das Secretarias Estaduais de Saúde (SES). Os dados foram enriquecidos, de forma que a partir do momento em que um município confirma um caso, ele sempre aparecerá nessa tabela (mesmo que para uma determinada data a SES não tenha liberado o boletim - nesse caso é repetido o dado do dia anterior). Caso queira ver a tabela original (sem repetição e com datas faltantes), visite [caso](https://brasil.io/dataset/covid19/caso/).

O dataset utilizado nesse notebook possui sua última atualização no dia **29/06/2021** e uma cópia desse dataset encontra-se no [repositório do projeto](https://github.com/diascarolina/projeto-series-temporais-covid/blob/main/data/caso_full.csv.gz).

<div class="alert alert-success">
    <strong><a href='https://github.com/diascarolina/projeto-series-temporais-covid/blob/main/notebooks/limpeza-dados.ipynb'>Notebook de Limpeza dos Dados Sobre a Covid-19</a></strong>
</div>


Também foi feita uma breve análise sobre a vacinação contra a doença. Os dados foram extraídos de:

- [OpenDataSUS: Registros de Vacinação COVID-19](https://opendatasus.saude.gov.br/dataset/covid-19-vacinacao/resource/ef3bd0b8-b605-474b-9ae5-c97390c197a8)

Como os dados são sobre cada aplicação individual da vacina, os arquivos são muito grandes. Por isso, adaptei os datasets para termos os dados da contagem de quantas doses de vacina foram aplicadas por dia, obtendo assim um arquivo bem menor que pode ser encontrado [aqui](https://github.com/diascarolina/projeto-series-temporais-covid/blob/main/data/vacina_total_ce.csv). Última atualização desses dados: **29/06/2021**.

<a name="analise"></a>
# 3 Análises

O escopo desse projeto é limitado. Tratei apenas dos dados sobre a Covid no Estado do Ceará, sem entrar em nenhum município específico. Buscamos analisar como anda o crescimento da doença no Estado desde o primeiro caso registrado e tentar obter previsões para as séries temporais de casos e óbitos utilizando a Biblioteca Prophet.

Prophet é uma poderosa biblioteca de previsão de séries temporais criada pelo time de Ciência de Dados do Facebook. Presente em Python e em R, essa biblioteca trabalha muito bem (e rapidamente) com séries temporais com muita sazonalidade (como é o nosso caso). Além disso, existe a possibilidade de utilizá-lo para séries temporais multivariadas.

Ademais, fizemos uma breve análise sobre a aplicação de vacinas contra a Covid-19 no Estado do Ceará.

<a name="conc"></a>
# 4 Conclusões


