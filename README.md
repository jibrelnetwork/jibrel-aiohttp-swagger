# Jibrel aiohttp swagger plugin

Minimal aiohttp swagger UI plugin.

Features:

* render swagger UI
* add spec endpoint and serve provided yaml for UI
* serve swagger UI static
* optional spec version substitution from file content

## Install

Last published release:

`pip install jibrel-aiohttp-swagger`

Dev version from git:

`pip install git+https://github.com/jibrelnetwork/jibrel-aiohttp-swagger#egg=jibrel_aiohttp_swagger`

## Usage

```python
from jibrel_aiohttp_swagger import setup_swagger
setup_swagger(app,
              spec_path='v1.swagger.yml',
              version_file_path='version.txt')
```
