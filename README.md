# example-pydantic-swagger

Convert pydantic definition to swagger docs

## Usage
```bash
# get schema from projectA
$ pipenv run python 01_generate_schema_a.py

# get schema from projectB
$ pipenv run python 01_generate_schema_b.py

# generate OpenAPI JSON
$ pipenv run python 02_generate_openapi.py

# spin up swagger ui
$ docker-compose up
```

Access via http://localhost:8080

## Screenshots
![picture 1](images/a75223fd6bd411514a558e0db808d3336658d88eb9578ce9d4540a84528932df.png)
![picture 2](images/2226ae3242c60596b0883ac6525c106c582678e64f108b80c236588df870d428.png)
![picture 3](images/70e29168ef4790bdabfd4c85e0914f738e7920741d67f00e61be5785e51284b7.png)


## References
- https://github.com/swagger-api/swagger-ui/blob/master/docs/usage/installation.md
