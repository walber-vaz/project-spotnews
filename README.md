# Projeto spotnews

## Descrição do projeto

O projeto spotnews é um projeto de um sistema de notícias, onde o usuário pode se cadastrar e logar no sistema, e assim, poderá criar, editar e excluir suas notícias. O usuário também poderá visualizar as notícias de outros usuários, e poderá comentar nas notícias de outros usuários. Usando Django, Django Rest Framework.

## Requisito do projeto

***1 - Crie a migrate e a model Categories***

Criar model de Categories com os seguintes campos:

- [x] Crie a classe Categories;
- [x] A classe Categories deve herdar os models do Django;
- [x] A classe Categories deve ter uma propriedade chamada name;
- [x] A propriedade name deve ser um campo de caracteres com um tamanho máximo de 200 caracteres;
- [x] A propriedade name não deve aceitar informações vazias ou maiores que 200 caracteres;
- [x] O método **str** da classe Categories deve retornar a propriedade name da categoria criada;

***2 - Crie a migrate e a model Users***

Criar model de Users com os seguintes campos:

- [x] Crie a classe Users;
- [x] A classe Users deve herdar os models do Django;
- [x] A classe Users deve ter as propriedades chamada name, email, password e role;
- [x] As propriedades name, password e role devem ser campos de caracteres com um tamanho máximo de 200 caracteres;
- [x] A propriedade email deve ser um campo do tipo email com um tamanho máximo de 200 caracteres;
- [x] As propriedades devem ser:
  - [x] name: Campo de caracteres, com tamanho máximo de 200 caracteres;
  - [x] email: Campo de email, , com tamanho máximo de 200 caracteres;
  - [x] password: Campo de caracteres, com tamanho máximo de 200 caracteres;
  - [x] role: Campo de caracteres, com tamanho máximo de 200 caracteres;
- [x] As propriedades name, email, password e role não devem aceitar informações vazias ou maiores que 200 caracteres;
- [x] O método **str** da classe Users deve retornar a propriedade name da pessoa usuária criada;

***3 - Crie a migrate e o model News***

Criar model de News com os seguintes campos:

- [x] Crie a classe News;
- [x] A classe News deve herdar os models do Django;
- [x] A classe News deve ter as propriedades chamada title, content, author, created_at, image e categories;
- [x] As propriedades devem ser:
  - [x] title: Campo de caracteres com tamanho máximo de 200 caracteres e com validação que não permita títulos com apenas uma palavra;
  - [x] content: Campo de texto, sem tamanho máximo de caracteres;
  - [x] author: Chave estrangeira da tabela ligada o model Users;
  - [x] created_at: Campo de data;
  - [x] image: Campo de imagem;
  - [x] categories: Chave estrangeira da tabela ligada o model Categories;
- [x] As propriedades title, content, created_at e categories não devem aceitar informações vazias;
- [x] A propriedade image pode aceitar informações vazias;
- [x] A propriedade title não deve aceitar informações maiores que 200 caracteres;
- [x] A propriedade created_at não deve aceita datas fora do padrão AAAA-MM-DD;
- [x] A propriedade img deve ter um campo upload_to que deve ser igual ao diretório 'img/';
- [x] A propriedade categories deve aceitar 1 ou mais categorias e deve se relacionar como muitos para muitos;
- [x] O método **str** da classe News deve retornar a propriedade title da notícia criada;

***4 - Crie a página Inicial***

Criar a página inicial com os seguintes requisitos:

<!--
Crie um template para a página inicial do projeto;
Crie a view e a url necessárias para renderizar o template home.html;
Inclua as urls de news nas urls do projeto;
O template da página inicial deve ser renderizado na rota http://127.0.0.1:8000/;
O template deve ter uma tag link importando o arquivo css css/style.css que está na página de estáticos;
A importação de arquivos estáticos deve ser feita através do template tag static;
O caminho para a página inicial deve ter o nome de home-page;
O template da página inicial deve ter como título Página Inicial;
O template da página inicial deve ter um cabeçalho header com a classe header;
O template da página inicial deve ter uma lista não ordenada com a classe header-links dentro do cabeçalho;
O template da página inicial deve ter na lista não ordenada um link a com referência para a home-page e com o texto Home;
O template da página inicial deve ter cards das notícias cadastradas no banco;
O template da página inicial deve ter títulos h2 com a classe news-title e os títulos das notícias como valores;
O template da página inicial deve ter tags span com a classe news-date e a datas de criação das notícias como valores;
O template deve exibir as datas no formato DD/MM/AAAA;
O template da página inicial deve exibir as imagens das notícias;
-->
- [x] Crie um template para a página inicial do projeto;
- [x] Crie a view e a url necessárias para renderizar o template home.html;
- [x] Inclua as urls de news nas urls do projeto;
- [x] O template da página inicial deve ser renderizado na rota http://
- [x] O template deve ter uma tag link importando o arquivo css css/style.css que está na página de estáticos;
- [x] A importação de arquivos estáticos deve ser feita através do template tag static;
- [x] O caminho para a página inicial deve ter o nome de home-page;
- [x] O template da página inicial deve ter como título Página Inicial;
- [x] O template da página inicial deve ter um cabeçalho header com a classe header;
- [x] O template da página inicial deve ter uma lista não ordenada com a classe header-links dentro do cabeçalho;
- [x] O template da página inicial deve ter na lista não ordenada um link a com referência para a home-page e com o texto Home;
- [x] O template da página inicial deve ter cards das notícias cadastradas no banco;
- [x] O template da página inicial deve ter títulos h2 com a classe news-title e os títulos das notícias como valores;
- [x] O template da página inicial deve ter tags span com a classe news-date e a datas de criação das notícias como valores;
- [x] O template deve exibir as datas no formato DD/MM/AAAA;
- [x] O template da página inicial deve exibir as imagens das notícias;

***5 - Crie a página de Detalhes de uma Notícia***

Criar a página de detalhes de uma notícia com os seguintes requisitos:

- [x] Crie um template para a página detalhes da notícia;
- [x] Crie a view e a url necessárias para renderizar o template news_details.html;
- [x] O template da página detalhes da notícia deve ser renderizado na rota <http://127.0.0.1:8000/news/><int:id>
- [x] O caminho para a página detalhes da notícia deve ter o nome de news-details-page;
- [x] O template da página detalhes da notícia deve ter como título Página de Detalhes da Notícia;
- [x] O template da página detalhes da notícia deve ter um cabeçalho header com a classe header;
- [x] O template da página detalhes da notícia deve ter uma lista não ordenada com a classe header-links;
- [x] O template da página detalhes da notícia deve ter no cabeçalho um link a com referência para a home-page e com o texto Home;
- [x] O template da página detalhes da notícia deve exibir as seguintes informações:
- [x] O título da notícia em título h1;
- [x] O conteúdo da notícia em parágrafo p com classe news-content;
- [x] Cada categoria da notícia em uma tag span com classe news-categories;
- [x] A pessoa autora da notícia em uma tag span com classe news-author;;
- [x] A imagem da notícia;
- [x] A data de criação da notícia no formato DD/MM/AAAA;
- [x] Modifique as notícias no template home.html para que quando clicadas haja um redirecionamento para a página detalhes da notícia;

***6 - Crie a página de Formulário de uma Nova Categoria***

Criar a página de formulário de uma nova categoria com os seguintes requisitos:

- [x] Crie um template para o formulário de cadastro de uma categoria;
- [x] Crie a view e a url necessárias para renderizar o template categories_form.html;
- [x] O template do formulário de uma nova categoria deve ser renderizado na rota <http://127.0.0.1:8000/categories/>;
- [x] O caminho para o formulário de uma nova categoria deve ter o nome de categories-form;
- [x] O template do formulário de uma nova categoria deve ter como título Formulário para Nova Categoria;
- [x] O template do formulário de uma nova categoria deve ter um cabeçalho header com a classe header;
- [x] O template do formulário de uma nova categoria deve ter uma lista não ordenada com a classe header-links;
- [x] O template do formulário de uma nova categoria deve ter no cabeçalho um primeiro link a com referência para a home-page e com o texto Home;
- [x] O template do formulário de uma nova categoria deve ter no cabeçalho um outro link a com referência para a categories-form e com o texto Cadastrar Categorias;
- [x] O template do formulário de uma nova categoria deve ter uma tag de formulário com a propriedade method do tipo post e a propriedade action com a url para /categories;
- [x] O template do formulário de uma nova categoria deve carregar o token de segurança CSRF em seu interior usando a tag de template adequada;
- [x] O template do formulário de uma nova categoria deve ter uma label que como o valor Nome;
- [x] O template do formulário de uma nova categoria deve ter um input com as algumas especificações:
  - [x] A propriedade type do tipo text;
  - [x] A propriedade name com o valor name;
  - [x] A propriedade maxlength com o valor 200;
  - [x] Precisa ser um campo obrigatório;
- [x] O template do formulário de uma nova categoria deve ter um botão do tipo submit com texto Salvar;
- [x] Após o cadastro de uma categoria, a pessoa usuária deve ser redirecionada para a página principal;

***7 - Crie a página de Formulário de uma Nova Notícia***

Criar a página de formulário de uma nova notícia com os seguintes requisitos:

- [x] Crie um template para o formulário de cadastro de uma categoria;
- [x] Crie a view e a url necessárias para renderizar o template news_form.html;
- [x] O template do formulário de uma nova notícia deve ser renderizado na rota <http://127.0.0.1:8000/news/>;
- [x] O caminho para o formulário de uma nova notícia deve ter o nome de news-form;
- [x] O template do formulário de uma nova notícia deve ter como título Formulário para Nova Notícia;
- [x] O template do formulário de uma nova notícia deve ter um cabeçalho header com a classe header;
- [x] O template do formulário de uma nova notícia deve ter uma lista não ordenada com a classe header-links;
- [x] O template do formulário de uma nova notícia deve ter no cabeçalho um primeiro link a com referência para a home-page e com o texto Home;
- [x] O template do formulário de uma nova notícia deve ter no cabeçalho um segundo link a com referência para a categories-form e com o texto Cadastrar Categorias;
- [x] O template do formulário de uma nova notícia deve ter no cabeçalho um terceiro link a com referência para a news-form e com o texto Cadastrar Notícias;
- [x] O template do formulário de uma nova notícia deve ter uma tag de formulário com a propriedade method do tipo post, a propriedade action com a url para /news/ e a propriedade enctype com valor multipart/form-data;
- [x] O template do formulário de uma nova notícia deve carregar o token de segurança CSRF em seu interior usando a tag de template adequada;
- [x] O template do formulário de uma nova notícia deve ter as seguintes tag:
  - [x] Uma label como o valor Título;
  - [x] Um input do tipo text com o nome title;
  - [x] Uma label como o valor Conteúdo;
  - [x] Um textarea com o nome content;
  - [x] Uma label como o valor Autoria;
  - [x] Um select com o nome author;
  - [x] Múltiplos option sendo seus valores os nomes das pessoas usuárias cadastradas no banco;
  - [x] Uma label como o valor Criado em;
  - [x] Um input do tipo date com o nome created_at;
  - [x] Uma label como o valor URL da Imagem;
  - [x] Um input do tipo file com o nome image;
  - [x] Múltiplas label sendo seus valores os nomes das categorias cadastradas no banco;
  - [x] Múltiplos input do tipo checkbox com o nome categories, cada input ligado a uma label de categoria;
  - [x] Um botão do tipo submit com o valor Salvar;
- [x] Após o cadastro de uma notícia, a pessoa usuária deve ser redirecionada para a página principal;

***8 - Crie a rota api/categories com o DRF***

Criar a rota api/categories com os seguintes requisitos:

- [x] Adicione a rota api/ nas urls do projeto;
- [x] Vincule o router usado para construção da api com a rota api/do projeto;
- [x] Registre no router a rotas categories com o viewset de Categories;
- [x] Crie um serializer que receba a model Categories e tenha os campos id e name;
- [x] Crie uma view que receba todas as categorias cadastradas no banco de dados e o serializer criado anteriormente;
- [x] Crie uma rota para a view criada com o nome de categories;

***9 - Crie a rota api/users com o DRF***

Criar a rota api/users com os seguintes requisitos:

- [x] Adicione a rota api/ nas urls do projeto;
- [x] Vincule o router usado para construção da api com a rota api/do projeto;
- [x] Registre no router a rotas users com o viewset de Users;
- [x] Crie um serializer que receba a model Users e tenha os campos id, name, email e role;
- [x] Crie uma view que receba todas as pessoas usuárias cadastradas no banco de dados e o serializer criado anteriormente;
- [x] Crie uma rota para a view criada com o nome de users;

***10 - Crie a rota api/news com o DRF***

Criar a rota api/news com os seguintes requisitos:

- [x] Adicione a rota api/ nas urls do projeto;
- [x] Vincule o router usado para construção da api com a rota api/do projeto;
- [x] Registre no router a rotas news com o viewset de News;
- [x] Crie um serializer que receba a model News e tenha os campos id, title, content, author, created_at, image e categories;
- [x] Crie uma view que receba todas as notícias cadastradas no banco de dados e o serializer criado anteriormente;
- [x] Crie uma rota para a view criada com o nome de news;

## Autor

- [Walber Vaz](https://www.linkedin.com/in/walber-vaz/)
