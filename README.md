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

### Protecting Against IDOR

To protect against IDOR vulnerabilities, developers should:

- Implement strict authentication and authorization checks before accessing or modifying data.
- Avoid exposing sensitive information, like user IDs, directly in APIs.
- Consider using indirect references or UUIDs that are not easily guessable.

## Conclusion

The provided PoC and lab setup illustrate the importance of proper security measures in GraphQL APIs to prevent IDOR vulnerabilities. It highlights the need for robust access controls to protect user data and ensure that only authorized actions are performed.

