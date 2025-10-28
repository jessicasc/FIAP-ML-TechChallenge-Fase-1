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

Os detalhes de cada endpoint podem ser acessados na documentação feita com Swagger e disponível no link: https://jessicasc-tc1-fiap-7e560f0b9791.herokuapp.com/apidocs/

## Aplicabilidade da API





