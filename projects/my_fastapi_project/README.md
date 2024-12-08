# Example usage

## Build the project
Navigate to this folder (where the `pyproject.toml` file is)

1. Export the dependencies (when using uv workspaces and having no project-specific lock-file):
``` shell
uv export --no-emit-project --output-file requirements.txt
```

2. Build a wheel:
``` shell
uv build --out-dir ./dist
```

## Build a docker image

``` shell
docker build -t myimage .
```

## Run the image

``` shell
docker run -d --name mycontainer -p 8000:8000 myimage
```

The OpenAPI specification of this FastAPI app can now be accessed at http://localhost:8000/docs#
