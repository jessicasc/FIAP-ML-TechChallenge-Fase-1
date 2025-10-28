# API de Livros - FIAP ML Tech Challenge 1

O objetivo desse projeto foi desenvolver uma RESTFul API com endpoints que forneçam informações sobre dados de livros obtidos por meio de web scrapping no site https://books.toscrape.com.

## Endpoints
### Books
**/api/v1/books** - Listar todos os livros.  
**/api/v1/books/{id}** - Buscar livro por ID.  
**/api/v1/books/search** - Buscar livros por título e/ou categoria.  
**/api/v1/books/top-rated** - Buscar os livros mais bem avaliados.  
**/api/v1/books/price-range** - Buscar livros dentro de uma faixa de preço.  
### Categories
**/api/v1/categories** - Listar todas as categorias.  
### Health
**/api/v1/health** - Avalia a saúde da API.  
### Stats
**/api/v1/stats/overview** - Retorna estatísticas gerais dos livros, como quantidade total de livros, preço médio e distribuição por rating.   
**/api/v1/stats/categories**- Retorna estatísticas gerais por categoria, como quantidade total de livros e preço médio por categoria.  
  
Os detalhes de cada endpoint podem ser acessados na documentação feita com Swagger e disponível no link:  
https://jessicasc-tc1-fiap-7e560f0b9791.herokuapp.com/apidocs/

## Aplicabilidade da API
**Recomendações**  
  - recomendar livros com título, categorias e preços semelhantes ao histórico de compra de um usuário;   
  - recomendar livros mais bem avaliados.
       
**Monitoramento**  
  - acompanhar preço médio por categoria, o que ajudaria a ter uma base para precificação de lançamentos;  
  - acompanhar estoque, o que permitiria identificar tendências nas vendas.

**Predições**  
  - prever preços utilizando um modelo de regressão baseado nas características do livro;    
  - prever o sucesso de um livro utilizando um modelo de classificação baseado nas características do livro.  

### Plano de integração com modelos de Machine Learning  
1. Coletar os dados via endpoints da API;  
2. Limpeza e pré-processamentos dos dados;   
3. Treinamento do modelo;  
4. Avaliação de desempenho;  
5. A partir desse ponto é possível integrar o modelo à API, realizar novos treinamentos, vincular os resultados à dashboards e etc.









