from ariadne import QueryType, MutationType, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
import uuid
from uvicorn import run

type_defs = load_schema_from_path("schema.graphql")

query = QueryType()
mutation = MutationType()


users = {}

@query.field("getUser")
def resolve_get_user(_, info, id):
    return users.get(id, None)

@query.field("getAllUsers")
def resolve_get_all_users(_, info):
    return list(users.values()) 

@mutation.field("createUser")
def resolve_create_user(_, info, name, age):
    user_id = str(uuid.uuid4())
    users[user_id] = {"id": user_id, "name": name, "age": age}
    return users[user_id]

@mutation.field("updateUser")
def resolve_update_user(_, info, id, name=None, age=None):
    if id in users:
        if name:
            users[id]["name"] = name
        if age:
            users[id]["age"] = age
        return users[id]
    return None

schema = make_executable_schema(type_defs, query, mutation)

app = GraphQL(schema, debug=True)

if __name__ == "__main__":
    run(app, host="127.0.0.1", port=8000)
