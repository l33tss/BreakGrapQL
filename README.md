# GraphQL API IDOR Vulnerability PoC

This repository contains a Proof of Concept (PoC) for demonstrating an Insecure Direct Object Reference (IDOR) vulnerability within a GraphQL API. The provided scripts simulate a scenario where unauthorized access to user data is possible due to improper access controls.

## What is IDOR?

Insecure Direct Object References (IDOR) occur when an application provides direct access to objects based on user-supplied input. As a result of this vulnerability, attackers can bypass authorization and access data and functionality that ought to be restricted.

## Introspection in GraphQL

GraphQL APIs offer an introspection system that allows clients to query the schema for information about the types and operations available. While powerful for development purposes, excessive exposure through introspection queries can lead to security vulnerabilities if not properly managed.

### Introspection Query

The provided PoC script includes an introspection query that enumerates available queries, mutations, their parameters, and return types. This feature is instrumental in understanding the API's structure and planning further actions, including exploiting vulnerabilities.

## How the IDOR Happens

The lab setup includes a simple GraphQL API managing user data, with operations to create users, update user information, and fetch all users. Due to a lack of proper authorization checks, the API is vulnerable to IDOR, allowing unauthorized access to modify any user data.

### Steps Demonstrating IDOR

1. **User Creation**: The PoC script creates two mock users, "Alice" and "Bob," without any authentication or authorization.
2. **User Enumeration**: By fetching all users, the script demonstrates how an attacker can enumerate user IDs and other data.
3. **Unauthorized Update**: The script then updates Bob's name to "HACKED" using his user ID, simulating an IDOR attack where an unauthorized actor modifies user data.

## PoC Step-by-Step Guide

This guide details the steps involved in the Proof of Concept (PoC) to demonstrate the IDOR vulnerability. It includes an explanation of GraphQL queries and mutations, and how they are used within this PoC.

### Understanding GraphQL Queries

In GraphQL, a query is used to read or fetch values. It is the equivalent of a GET request in REST. A query must specify what fields are needed on the object being queried. For example, when fetching users, you can specify that you only need their `id`, `name`, and `age`.

### Query Structure

A typical GraphQL query to fetch all users might look like this:

```graphql
{
  getAllUsers {
    id
    name
    age
  }
}
```
This query fetches the id, name, and age of all users by invoking the getAllUsers field on the root query type.

### Understanding GraphQL Mutations

While queries are for fetching data, mutations change data. They are the equivalent of POST, PUT, PATCH, or DELETE in REST. A mutation must specify the operation name and the input parameters, as well as the fields that should be returned on the object that was affected by the mutation.

### Mutation Structure
For example, creating a new user with a mutation might look like this:

```graphql
mutation CreateUser($name: String!, $age: Int!) {
  createUser(name: $name, age: $age) {
    id
    name
    age
  }
}
```
This mutation creates a new user and requests the id, name, and age of the newly created user in the response.


### Protecting Against IDOR

To protect against IDOR vulnerabilities, developers should:

- Implement strict authentication and authorization checks before accessing or modifying data.
- Avoid exposing sensitive information, like user IDs, directly in APIs.
- Consider using indirect references or UUIDs that are not easily guessable.

## Conclusion

The provided PoC and lab setup illustrate the importance of proper security measures in GraphQL APIs to prevent IDOR vulnerabilities. It highlights the need for robust access controls to protect user data and ensure that only authorized actions are performed.

