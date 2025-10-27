# Python Polylith Example

This is a repository with an example `Python` setup of the Polylith Architecture using `uv`.
Here you will find examples of code being shared between different kind of projects, and the developer tooling setup.


## Using uv workspaces
Polylith works really well with `uv workspaces`. In this repo, you'll find an example setup.

The recommended setup for Polylith is to treat the _projects_ as workspaces,
instead of having a full-blown `pyproject.toml` in each component.
With this setup, there is no need for any package boilerplate or configuration.

The _projects_ define how the thing should be built, packaged and deployed.

The _bricks_ (components and bases) are the shared code in your Monorepo.

### Setup
Define the _projects_ as workspace members in your root `pyproject.toml`:

``` toml
[tool.uv.workspace]
members = ["projects/*"]
```

The _project-specific_ `pyproject.toml` files defines the needed third-party dependencies.
In those, you can specify the dependencies without version if you like. The fixed versions are in they
`uv.lock` file at the repo root.

That's all you need! :tada:

## Deploying a project
There's several ways to deploy an individual project. In this repo, you will find a setup that should work
well for most cases.

Have a look at [the "My FastAPI project" README](./projects/my_fastapi_project/README.md) for details.

The main idea is:
- generate a project-specific lock file (i.e. a _requirements.txt_)
- build a wheel for the project, that will contain the needed Polylith __bricks__ only.
- install the wheel and the dependencies (in the example, Docker is used)


## Developer experience

### Mypy
Have a look at the `mypy.ini` configuration file, to make `Mypy` work really well with this type of architecture.

``` ini
[mypy]
mypy_path = components, bases
namespace_packages = True
explicit_package_bases = True
```

Have a look at this repository for more information and documentation:
[Python tools for the Polylith Architecture](https://github.com/DavidVujic/python-polylith)
