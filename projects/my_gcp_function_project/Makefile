.PHONY: add-gcp-entrypoint export-deps build-gcp-project gcp-package

PROJECT_NAME = my_gcp_function_project-0.1.0

add-gcp-entrypoint:
	cp ../../bases/example/greet_gcp_function/__init__.py ./main.py

export-deps:
	@(echo "functions-framework==3.5.x" > requirements.txt)
	@echo "I haven't found a way to export deps from Hatch, as done in Poetry. Using hardcoded requirements.txt in this folder."

build-gcp-project: export-deps add-gcp-entrypoint
	uv build --out-dir ./dist

gcp-package: build-gcp-project
	mv dist/$(PROJECT_NAME)-py3-none-any.whl dist/function.zip
