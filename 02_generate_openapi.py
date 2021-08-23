########## READ CONFIG ##########
import glob
import json

files = glob.glob("schema/*.json")

tags = []
paths = {}
schemas = {}

for schema in files:
    with open(schema, "r") as f:
        data = json.loads(f.read())

        tags.append(data["tag"])
        paths = {**paths, **data["path"]}
        schemas = {**schemas, **data["schemas"]}

########## CONFIG ##########
TITLE = "Swagger example"

########## OPENAPI SCHEMA TEMPLATE ##########
openapi = {
    "openapi": "3.0.2",
    "info": {"title": TITLE, "version": "0.1.0"},
    # "host": HOST,
    # "basePath": BASEPATH,
    "schemes": ["https", "http"],
    "tags": tags,
    "paths": paths,
    "components": {"schemas": schemas},
}

########## WRITE TO FILE ##########
with open("swagger/swagger.json", "w") as f:
    json_string = json.dumps(openapi, indent=4)
    json_string = json_string.replace("#/definitions/", "#/components/schemas/")

    f.write(json_string)

print("successfully generated OpenAPI schema.")
