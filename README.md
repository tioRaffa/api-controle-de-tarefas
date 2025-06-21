# API de Gerenciamento de Projetos e Tarefas

## 📖 Sobre o Projeto

Este projeto é uma API RESTful completa e robusta para gerenciamento de projetos, tarefas (issues) e comentários. Desenvolvida com Django e Django REST Framework, a API foi projetada com foco em performance, segurança e boas práticas de desenvolvimento, servindo como uma base sólida para qualquer sistema de gerenciamento de trabalho (workflow management system).

O objetivo foi construir não apenas um CRUD funcional, mas uma API inteligente, com funcionalidades avançadas que demonstram uma compreensão profunda dos padrões de desenvolvimento de APIs modernas.

## ✨ Funcionalidades Principais

Esta API vai além do básico, implementando uma série de funcionalidades avançadas:

  * **Autenticação JWT e Gerenciamento de Usuários:** Sistema completo de autenticação via JSON Web Token (JWT), com endpoints para registro, login (`access`/`refresh` tokens), verificação e renovação de tokens, utilizando a biblioteca Djoser.
  * **Sistema de Permissões Personalizado:** Implementação de permissões granulares (`IsOwnerOrReadOnly`) que garantem que um usuário só possa editar ou deletar os recursos que ele mesmo criou (Projetos, Issues, Comentários).
  * **Operações CRUD Completas:** Endpoints robustos para criar, ler, atualizar e deletar Projetos, Issues e Comentários.
  * **Filtragem Avançada de Dados:** Utilização da `django-filter` para permitir que os clientes da API filtrem resultados com base em múltiplos campos (ex: `?status=PENDENTE&project=3`).
  * **Busca Textual Abrangente:** Implementação de busca full-text com `SearchFilter`, permitindo pesquisas em campos como título e descrição (`?search=bug+pagamento`).
  * **Ordenação Dinâmica de Resultados:** Flexibilidade para o cliente ordenar os dados por diferentes campos e em ordem ascendente ou descendente (`?ordering=-created_at`).
  * **Otimização de Performance (N+1):** Uso estratégico de `select_related` e `prefetch_related` para otimizar as consultas ao banco de dados, prevenindo o clássico problema de "N+1 queries" e garantindo respostas rápidas.
  * **Endpoints Aninhados Personalizados:** Utilização do decorator `@action` para criar endpoints contextuais e intuitivos, como `/api/v1/projects/{id}/issues/` e `/api/v1/issues/{id}/comments/`.
  * **Endpoints Personalizados para o Usuário:** Criação de rotas especiais como `/api/v1/comments/me/` para uma melhor experiência do usuário.

## 🛠️ Tecnologias Utilizadas

  * **Backend:** Python, Django
  * **API Framework:** Django REST Framework
  * **Autenticação:** Djoser, DRF Simple JWT
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

```
# requirements.txt
Django
djangorestframework
django-filter
djoser
djangorestframework-simplejwt 
psycopg2-binary # Se usar PostgreSQL
```

```bash
pip install -r requirements.txt
```

## 📫 Configuração de Email para Desenvolvimento (Mailtrap)

Para evitar o envio de e-mails reais durante o desenvolvimento e teste, este projeto é configurado para usar o [Mailtrap.io](https://mailtrap.io) como um servidor SMTP falso. O Mailtrap captura todos os e-mails enviados pela aplicação (como os de reset de senha) e os exibe em uma caixa de entrada virtual segura, permitindo que você visualize e depure o conteúdo do e-mail sem spammar usuários reais.

### Como Configurar o Mailtrap

1.  **Crie uma Conta Gratuita:** Vá até [mailtrap.io](https://mailtrap.io) e crie uma conta.
2.  **Encontre suas Credenciais:** No seu painel do Mailtrap, navegue até a sua "Inbox" e encontre a seção "SMTP Settings" ou "Integrations". Selecione "Django" na lista para ver as credenciais já formatadas.
3.  **Adicione as Credenciais ao seu arquivo `.env`:** Copie os valores fornecidos pelo Mailtrap e adicione-os ao seu arquivo `.env` local. As variáveis necessárias estão listadas na seção de instalação abaixo.

Com isso, qualquer funcionalidade que dispare um e-mail (como o reset de senha do Djoser) terá seu e-mail capturado na sua caixa de entrada do Mailtrap.


**5. Configure as Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto, baseado no exemplo `.env.example`.

```
# .env.example
SECRET_KEY='sua-chave-secreta-super-dificil-de-adivinhar'
DEBUG=True
DATABASE_URL='sqlite:///db.sqlite3'
# Exemplo para PostgreSQL:
# DATABASE_URL='postgres://user:password@host:port/dbname'

Configuração de Email com Mailtrap para Desenvolvimento
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.mailtrap.io
EMAIL_PORT=2525
EMAIL_HOST_USER=your_mailtrap_user_here
EMAIL_HOST_PASSWORD=your_mailtrap_password_here
EMAIL_USE_TLS=True
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

A API estará disponível em `http://127.0.0.1:8000/api/v1/`.

-----

## 📋 Documentação da API

Todos os endpoints requerem autenticação via Token JWT. O token de acesso deve ser enviado no cabeçalho `Authorization`.
`Authorization: JWT <seu_token_de_acesso>`


### Autenticação (Djoser com JWT)

| Método | URL | Descrição |
| :--- | :--- | :--- |
| `POST` | `/api/v1/auth/users/` | Registra um novo usuário. |
| `POST` | `/api/v1/auth/jwt/create/` | Realiza o login. Retorna um `access` e `refresh` token. |
| `POST` | `/api/v1/auth/jwt/refresh/` | Gera um novo `access` token usando um `refresh` token válido. |
| `POST` | `/api/v1/auth/jwt/verify/` | Verifica se um `access` token ainda é válido. |
| `GET` | `/api/v1/auth/users/me/` | Retorna os dados do usuário logado. |
| `POST` | `/api/v1/auth/users/reset_password/` | **(Novo)** Inicia o fluxo de reset de senha. Envia um e-mail para o usuário. |
| `POST` | `/api/v1/auth/users/reset_password_confirm/` | **(Novo)** Finaliza o fluxo de reset de senha com os dados do e-mail. |

### Projetos (`/api/v1/projects/`)

| Método | URL | Descrição | Permissão |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/projects/` | Lista todos os projetos. | Autenticado |
| `POST` | `/api/v1/projects/` | Cria um novo projeto. O `owner` é definido automaticamente. | Autenticado |
| `GET` | `/api/v1/projects/{id}/` | Retorna os detalhes de um projeto. | Autenticado |
| `PATCH/PUT` | `/api/v1/projects/{id}/` | Atualiza um projeto. | Dono do Projeto |
| `DELETE` | `/api/v1/projects/{id}/` | Deleta um projeto. | Dono do Projeto |
| `GET` | `/api/v1/projects/{id}/issues/` | **(Action)** Lista todas as `issues` de um projeto específico. | Autenticado |

### Issues (`/api/v1/issues/`)

| Método | URL | Descrição | Permissão |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/issues/` | Lista todas as `issues`. Suporta **filtros**, **busca** e **ordenação**. | Autenticado |
| `POST` | `/api/v1/issues/` | Cria uma nova `issue`. O `reporter` é definido automaticamente. | Autenticado |
| `GET` | `/api/v1/issues/{id}/` | Retorna os detalhes de uma `issue`. | Autenticado |
| `PATCH/PUT`| `/api/v1/issues/{id}/` | Atualiza uma `issue`. | Criador da Issue |
| `DELETE` | `/api/v1/issues/{id}/` | Deleta uma `issue`. | Criador da Issue |
| `GET` | `/api/v1/issues/{id}/comments/` | **(Action)** Lista todos os comentários de uma `issue`. | Autenticado |
| `POST` | `/api/v1/issues/{id}/comments/` | **(Action)** Cria um novo comentário para uma `issue`. | Autenticado |

**Exemplos de Query Params para `GET /api/v1/issues/`:**

  * **Filtrar:** `?status=PENDENTE&project=1`
  * **Buscar:** `?search=corrigir+login`
  * **Ordenar:** `?ordering=-priority`

### Comentários (`/api/v1/comments/`)

| Método | URL | Descrição | Permissão |
| :--- | :--- | :--- | :--- |
| `GET` | `/api/v1/comments/` | Lista todos os comentários. Suporta filtro por `issue`. | Autenticado |
| `GET` | `/api/v1/comments/?issue=5` | Exemplo de filtro: lista comentários apenas da `Issue` de ID 5. | Autenticado |
| `GET` | `/api/v1/comments/me/` | **(Action)** Lista apenas os comentários do usuário logado. | Autenticado |
| `POST` | `/api/v1/comments/` | Cria um novo comentário. Requer `body` e `issue_id` no corpo. | Autenticado |
| `GET` | `/api/v1/comments/{id}/` | Retorna o detalhe de um comentário. | Autenticado |
| `PATCH/PUT`| `/api/v1/comments/{id}/` | Atualiza um comentário. | Dono do Comentário |
| `DELETE` | `/api/v1/comments/{id}/` | Deleta um comentário. | Dono do Comentário |
