.PHONY: add-gcp-entrypoint export-deps build-gcp-project gcp-package

PROJECT_NAME = my_gcp_function_project-0.1.0

add-gcp-entrypoint:
	cp ../../bases/example/greet_gcp_function/__init__.py ./main.py

export-deps:
	@uv pip compile --extra-index-url https://pypi.org/simple pyproject.toml --output-file requirements.txt

build-gcp-project: export-deps add-gcp-entrypoint
	uv build --out-dir ./dist

gcp-package: build-gcp-project
	mv dist/$(PROJECT_NAME)-py3-none-any.whl dist/function.zip
