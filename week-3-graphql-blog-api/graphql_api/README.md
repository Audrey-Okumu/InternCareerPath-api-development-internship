# Week 3 – GraphQL Blog API

## 📘 Project Overview
This project is a **GraphQL Blog API**.  
The main goal is was to understand and implement **GraphQL APIs**, focusing on schema definition, resolvers, queries, and mutations while avoiding common REST API problems such as **over-fetching and under-fetching of data**.

The API enables clients to manage blog **authors** and **posts** using a single GraphQL endpoint.

---

## 🧰 Technology Stack
- **Python 3**
- **Django**
- **Graphene-Django**
- **SQLite** (development database)
- **GraphQL Playground (GraphiQL)**

---

## Data Models

### Author
| Field | Type |
|------|------|
| id | Integer |
| name | String |

### Post
| Field | Type |
|------|------|
| id | Integer |
| title | String |
| content | Text |
| author | Foreign Key → Author |

---

## 🔌 API Endpoints
| URL | Description |
|----|------------|
| `/` | Simple homepage |
| `/graphql/` | GraphQL Playground |
| `/admin/` | Django Admin interface |

---

## 🔍 GraphQL Queries

### Fetch all authors
```graphql
query {
  allAuthors {
    id
    name
  }
}
```
### Fetch all posts with author info 
```
query {
  allPosts {
    id
    title
    author {
      name
    }
  }
}
```
### Fetch a single post by ID
```
query {
  postById(id: 1) {
    title
    content
    author {
      name
    }
  }
}
```
## GraphQL Mutations
### Create an author
```
mutation {
  createAuthor(name: "Audrey Akello") {
    author {
      id
      name
    }
  }
}
```

### Create a blog post
```
mutation {
  createPost(
    title: "Introduction to GraphQL"
    content: "GraphQL allows clients to request exactly the data they need."
    authorId: 1
  ) {
    post {
      id
      title
      author {
        name
      }
    }
  }
}
```
---

## Running the Project Locally
### Step 1: Clone the repository
```
git clone <repository-url>
```
### Step 2: Navigate to the Week 3 directory
```
cd week-3-graphql-blog-api
```
### Step 3: Activate virtual environment
```
env\Scripts\activate
```
### Step 4: Install dependencies
```
pip install django graphene-django
```

### Step 5: Apply database migrations
```
python manage.py migrate
```

### Step 6: Start the development server
```
python manage.py runserver
```

## Key GraphQL Concepts Demonstrated

Schema Definition – Defining types and relationships

Resolvers – Handling how data is fetched

Queries vs Mutations – Read and write operations

Avoiding Over-Fetching – Clients request only required fields

Single Endpoint Design – All operations through /graphql/
