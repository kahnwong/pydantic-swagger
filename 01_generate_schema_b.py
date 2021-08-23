from model.spam import Bar
from model.spam import Foo
from model.spam import Spam
from model.spam import SpamResponse

##################### CONFIG #####################
TAG_NAME = "Spam"
TAG_DESCRIPTION = ""

ENDPOINT_NAME = "detect-spam"
SUMMARY = "Detect spam"

REQUEST_SCHEMA = Spam.schema()
REQUEST_MODEL_NAME = REQUEST_SCHEMA["title"]

RESPONSE_SCHEMA = SpamResponse.schema()
RESPONSE_MODEL_NAME = RESPONSE_SCHEMA["title"]


##################### TAG ########################
tag = {
    "name": TAG_NAME,
    "description": TAG_DESCRIPTION,
    # "externalDocs": {
    #     "description": "Find out more",
    #     "url": "http://swagger.io",
    # },
}


##################### PATH #####################
path = {
    f"/{ENDPOINT_NAME}/": {
        "post": {
            "summary": SUMMARY,
            "tags": [TAG_NAME],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {"$ref": f"#/components/schemas/{REQUEST_MODEL_NAME}"}
                    }
                },
                "required": True,
            },
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": f"#/components/schemas/{RESPONSE_MODEL_NAME}"
                            }
                        }
                    },
                }
            },
        }
    },
}
##################### SCHEMA #####################
schemas = {REQUEST_MODEL_NAME: REQUEST_SCHEMA, RESPONSE_MODEL_NAME: RESPONSE_SCHEMA}

aux_models = [
    Foo,
    Bar,
]

for model in aux_models:
    model_schema = model.schema()
    model_name = model_schema["title"]

    schemas[model_name] = model_schema

##################### WRITE TO FILE #####################
import json
import os

os.makedirs("schema", exist_ok=True)

OUT_PATH = f"schema/{TAG_NAME.lower()}.json"
with open(OUT_PATH, "w") as f:
    json_data = {"tag": tag, "path": path, "schemas": schemas}

    f.write(json.dumps(json_data, indent=4))

print(f"Successfully generated raw schema for {TAG_NAME}")
