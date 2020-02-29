
from graphene import ObjectType, String, Schema


class Query(ObjectType):
    # this defines a field `hello` in our Schema with a single Argument `name`
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # Our resolver methods takes the graphql context (root, info) as well as
    # Argument (name) and returns data for query response
    def resolve_hello(root, info, name):
        # f-strings a new and improved way to fofrmat strings it evaluates at
        # runtime thus can can call functions and resolve expressions... enjoy
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya'


# for each field in our schema we write a resolver to fetch data requested by a
# client's Query using the context and Args
schema = Schema(query=Query)

qurry = schema.execute('{goodbye}')
print(qurry.data)


# In Graphql Schema Defination Language SDL, we can describe the fields
# defined by class Query above as

# type Query {
#   hello(name: String="stranger"): String
#   goodbye: String
# }

# write meduim article
# to test schema from django ORM 
# open django ORM 'python manage.py shell' import schema
#from console import schema.schema.execute()
#pass your query '{hello(name: "Richard Okonicha")}'
#https://docs.graphene-python.org/en/latest/quickstart/#requirements
# query = schema.schema.execute('{hello}')  
# query_with_argument = '{ hello(name: "GraphQL") }'
# print(result.data['hello'])                                              
