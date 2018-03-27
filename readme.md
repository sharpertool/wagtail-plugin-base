# Wagtail plugin base

A basic template for creating wagtail javascript plugins.

## Prerequisites

- [PyPi account](https://pypi.org/)
- [Python](https://www.python.org/)
- [Yarn](https://yarnpkg.com/en/) or [NPM](https://www.npmjs.com/)
- [Twine](https://pypi.python.org/pypi/twine)

## Getting started

- Fork the project
- `yarn install` or `npm install` to install webpack dependencies.
- Update setup.py with your own desired plugin information.
- Change other instances of 'plugin-base' to your own plugin name (incl. in webpack.config.js).

## Usage

- Write your plugin JavaScript in the src folder.
- `yarn run build` (or `npm run build`) will bundle the assets from the src directory into the [pluign-name]/static directory.
- `python setup.py sdist` will build your python package into a dist/ directory.
- `twine upload dist/*` will upload your built packages to PyPi.

## Resources

- You can find more information on getting your packages built and deployed at the following URL. 
https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi