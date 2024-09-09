# Super portifolio python 

## Contexto do Projeto

O foco principal deste projeto, com base nos ensinamentos da **Trybe**, é praticar e consolidar os conhecimentos em **Django** e **Django Rest Framework (DRF)**, desenvolvendo uma API robusta para gerenciamento de perfis e projetos em um super portfólio. A aplicação contará com autenticação via **JWT** e permitirá a criação, leitura, atualização e remoção (CRUD) de perfis, projetos, certificados e instituições certificadoras.

<details>
  <summary>O que é a Trybe?🤔</summary>
  A Trybe é uma escola de desenvolvimento web genuinamente comprometida com o sucesso profissional de seus estudantes. Com o Modelo de Sucesso Compartilhado (MSC) oferecido pela Trybe Fintech, uma instituição financeira autorizada pelo Banco Central do Brasil, os alunos têm a opção de pagar apenas quando estiverem trabalhando.
</details>


Neste projeto, a API permite que usuários cadastrem seus perfis e projetos, além de armazenar suas certificações e as instituições certificadoras. Com a implementação da arquitetura **CRUD** e a utilização de **ViewSets** e **Serializers**, será possível criar rotas e endpoints RESTful eficientes, com suporte a entidades aninhadas, ou seja, será possível gerenciar certificados e instituições certificadoras de forma integrada.

### Funcionalidades Principais:

1. **Autenticação JWT**:
   - O projeto implementa autenticação utilizando o **Simple JWT**, garantindo que apenas usuários autenticados possam acessar rotas sensíveis.
   - A autenticação é exigida para criar, atualizar ou deletar perfis e projetos, enquanto a leitura é acessível publicamente.

2. **CRUD de Perfis e Projetos**:
   - Os usuários poderão criar e gerenciar seus perfis e projetos. Cada perfil poderá ser associado a múltiplos projetos, permitindo a construção de um portfólio completo.
   - O CRUD de perfis permite listar, criar, editar e excluir perfis e projetos por meio de endpoints RESTful.

3. **Perfis Customizados**:
   - A visualização dos perfis será renderizada diretamente em templates HTML para permitir uma navegação amigável e informativa.
   - O método `GET` para exibir perfis é aberto ao público, sem necessidade de autenticação, enquanto as demais operações (POST, PATCH, DELETE) requerem login.

4. **CRUD Inline de Certificados e Instituições**:
   - É possível criar e gerenciar certificados e suas respectivas instituições certificadoras em uma única requisição, tornando a interface mais eficiente e intuitiva.
   - Através de serializers aninhados, será possível exibir todas as certificações e suas instituições de forma estruturada.

5. **Exibição de Perfil Completo**:
   - A página de perfil exibe todos os detalhes de um usuário, incluindo certificados, instituições certificadoras e projetos associados, permitindo uma visão completa do portfólio do usuário.

### Habilidades Desenvolvidas:

- Utilização do **Django REST Framework (DRF)** para criar uma API com entidades aninhadas.
- Implementação de autenticação baseada em **JWT** com o pacote **Simple JWT**.
- Criação de **ViewSets** customizados para fornecer permissões diferenciadas para métodos HTTP específicos.
- Desenvolvimento de **CRUD** inline, permitindo a manipulação de múltiplas entidades relacionadas em uma única requisição.
- Renderização de templates HTML diretamente do backend para exibição de perfis e projetos de forma amigável ao usuário.

---

## Tecnologias Usadas

- [Python](https://www.python.org/) - Linguagem de programação utilizada para desenvolver o backend da aplicação.
- [Django](https://www.djangoproject.com/) - Framework web utilizado para estruturar a aplicação server-side.
- [Django Rest Framework (DRF)](https://www.django-rest-framework.org/) - Extensão do Django utilizada para criar APIs RESTful.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - Biblioteca para autenticação baseada em tokens JWT no Django Rest Framework.
- [MySQL](https://www.mysql.com/) -  Banco de dados relacional utilizado para armazenar as informações de perfis, projetos, certificados e instituições.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Linguagem de marcação utilizada para a construção das páginas web.
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) - Utilizado para estilização das páginas HTML e garantir uma interface visual atraente.
- [Docker](https://www.docker.com/) - Utilizado para containerização da aplicação, facilitando o gerenciamento de ambientes de desenvolvimento e produção.



## Entre em contato:
<a href="mailto:zazac3179@gmail.com" target="_blank">
  <img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" height="40" width="auto" />
</a>
<a href="https://www.linkedin.com/in/isaque-s-oliveira/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="isaque oliveira" height="30" width="40" /></a>
<a href="https://wa.me/5574981510614" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" /></a>
