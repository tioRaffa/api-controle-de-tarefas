Com certeza\! Com base em toda a evolução do seu projeto, preparei um `README.md` detalhado e profissional. Ele foi pensado para impressionar: claro para recrutadores, completo para outros desenvolvedores e um ótimo resumo das suas habilidades.

Você pode copiar e colar o conteúdo abaixo diretamente em um arquivo chamado `README.md` na raiz do seu projeto no GitHub.

-----

# API de Gerenciamento de Projetos e Tarefas

## 📖 Sobre o Projeto

Este projeto é uma API RESTful completa e robusta para gerenciamento de projetos, tarefas (issues) e comentários. Desenvolvida com Django e Django REST Framework, a API foi projetada com foco em performance, segurança e boas práticas de desenvolvimento, servindo como uma base sólida para qualquer sistema de gerenciamento de trabalho (workflow management system).

O objetivo foi construir não apenas um CRUD funcional, but uma API inteligente, com funcionalidades avançadas que demonstram uma compreensão profunda dos padrões de desenvolvimento de APIs modernas.

## ✨ Funcionalidades Principais

Esta API vai além do básico, implementando uma série de funcionalidades avançadas:

  * **Autenticação e Gerenciamento de Usuários:** Sistema completo de autenticação via token, com endpoints para registro, login, logout e gerenciamento de perfil de usuário, utilizando a biblioteca Djoser.
  * **Sistema de Permissões Personalizado:** Implementação de permissões granulares (`IsOwnerOrReadOnly`) que garantem que um usuário só possa editar ou deletar os recursos que ele mesmo criou (Projetos, Issues, Comentários).
  * **Operações CRUD Completas:** Endpoints robustos para criar, ler, atualizar e deletar Projetos, Issues e Comentários.
  * **Filtragem Avançada de Dados:** Utilização da `django-filter` para permitir que os clientes da API filtrem resultados com base em múltiplos campos (ex: `?status=PENDENTE&project=3`).
  * **Busca Textual Abrangente:** Implementação de busca full-text com `SearchFilter`, permitindo pesquisas em campos como título e descrição (`?search=bug+pagamento`).
  * **Ordenação Dinâmica de Resultados:** Flexibilidade para o cliente ordenar os dados por diferentes campos e em ordem ascendente ou descendente (`?ordering=-created_at`).
  * **Otimização de Performance (N+1):** Uso estratégico de `select_related` e `prefetch_related` para otimizar as consultas ao banco de dados, prevenindo o clássico problema de "N+1 queries" e garantindo respostas rápidas.
  * **Endpoints Aninhados Personalizados:** Utilização do decorator `@action` para criar endpoints contextuais e intuitivos, como `/api/projects/{id}/issues/` e `/api/issues/{id}/comments/`, sem a necessidade de bibliotecas de roteamento extras.
  * **Endpoints Personalizados para o Usuário:** Criação de rotas especiais como `/api/comments/me/` para uma melhor experiência do usuário, permitindo que ele liste seus próprios recursos facilmente.

## 🛠️ Tecnologias Utilizadas

  * **Backend:** Python, Django
  * **API Framework:** Django REST Framework
  * **Autenticação:** Djoser
  * **Filtros:** Django Filter
  * **Banco de Dados:** PostgreSQL (Recomendado), SQLite3 (Desenvolvimento)
  * **Gerenciamento de Ambiente:** Venv (ou Poetry/Pipenv)

## 🚀 Instalação e Execução

Siga os passos abaixo para executar o projeto localmente.

**1. Pré-requisitos**

  * Python 3.10+
  * Git

**2. Clone o Repositório**

```bash
git clone https://github.com/tioRaffa/api-controle-de-tarefas.git
cd api-controle-de-tarefas
```

**3. Crie e Ative o Ambiente Virtual**

```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

**4. Instale as Dependências**
Crie um arquivo `requirements.txt` com o conteúdo abaixo e execute o `pip install`.

```
# requirements.txt
Django
djangorestframework
django-filter
djoser
psycopg2-binary # Se usar PostgreSQL
```

```bash
pip install -r requirements.txt
```

**5. Configure as Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto, baseado no exemplo `.env.example`.

```
# .env.example
SECRET_KEY='sua-chave-secreta-super-dificil-de-adivinhar'
DEBUG=True
DATABASE_URL='sqlite:///db.sqlite3'
# Exemplo para PostgreSQL:
# DATABASE_URL='postgres://user:password@host:port/dbname'
```

**6. Aplique as Migrações do Banco de Dados**

```bash
python manage.py migrate
```

**7. Crie um Superusuário**

```bash
python manage.py createsuperuser
```

**8. Execute o Servidor de Desenvolvimento**

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/`.

-----

## 📋 Documentação da API

Todos os endpoints requerem autenticação (Token JWT). O token deve ser enviado no cabeçalho `Authorization`.
`Authorization: JWT seu_token_de_acesso`

### Autenticação (Djoser)

| Método | URL | Descrição |
| :--- | :--- | :--- |
| `POST` | `/auth/users/` | Registra um novo usuário. |
| `POST` | `/auth/token/login/` | Realiza o login e retorna um token de acesso. |
| `POST` | `/auth/token/logout/` | Realiza o logout, invalidando o token. |
| `GET` | `/auth/users/me/` | Retorna os dados do usuário logado. |

### Projetos (`/api/projects/`)

| Método | URL | Descrição | Permissão |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/projects/` | Lista todos os projetos. | Autenticado |
| `POST` | `/api/projects/` | Cria um novo projeto. O `owner` é definido automaticamente. | Autenticado |
| `GET` | `/api/projects/{id}/` | Retorna os detalhes de um projeto. | Autenticado |
| `PATCH/PUT` | `/api/projects/{id}/` | Atualiza um projeto. | Dono do Projeto |
| `DELETE` | `/api/projects/{id}/` | Deleta um projeto. | Dono do Projeto |
| `GET` | `/api/projects/{id}/issues/` | **(Action)** Lista todas as `issues` de um projeto específico. | Autenticado |

### Issues (`/api/issues/`)

| Método | URL | Descrição | Permissão |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/issues/` | Lista todas as `issues`. Suporta **filtros**, **busca** e **ordenação**. | Autenticado |
| `POST` | `/api/issues/` | Cria uma nova `issue`. O `reporter` é definido automaticamente. | Autenticado |
| `GET` | `/api/issues/{id}/` | Retorna os detalhes de uma `issue`. | Autenticado |
| `PATCH/PUT` | `/api/issues/{id}/` | Atualiza uma `issue`. | Criador da Issue |
| `DELETE` | `/api/issues/{id}/` | Deleta uma `issue`. | Criador da Issue |
| `GET` | `/api/issues/{id}/comments/` | **(Action)** Lista todos os comentários de uma `issue`. | Autenticado |
| `POST` | `/api/issues/{id}/comments/` | **(Action)** Cria um novo comentário para uma `issue`. | Autenticado |

**Exemplos de Query Params para `GET /api/issues/`:**

  * **Filtrar:** `?status=PENDENTE&project=1`
  * **Buscar:** `?search=corrigir+login`
  * **Ordenar:** `?ordering=-priority`

### Comentários (`/api/comments/`)

| Método | URL | Descrição | Permissão |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/comments/` | Lista todos os comentários. Suporta filtro por `issue`. | Autenticado |
| `GET` | `/api/comments/?issue=5` | Exemplo de filtro: lista comentários apenas da `Issue` de ID 5. | Autenticado |
| `GET` | `/api/comments/me/` | **(Action)** Lista apenas os comentários do usuário logado. | Autenticado |
| `POST` | `/api/comments/` | Cria um novo comentário. Requer `body` e `issue_id` no corpo. | Autenticado |
| `GET` | `/api/comments/{id}/` | Retorna o detalhe de um comentário. | Autenticado |
| `PATCH/PUT` | `/api/comments/{id}/` | Atualiza um comentário. | Dono do Comentário |
| `DELETE` | `/api/comments/{id}/` | Deleta um comentário. | Dono do Comentário |
