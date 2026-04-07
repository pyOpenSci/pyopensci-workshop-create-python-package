# <img src="https://www.pyopensci.org/images/logo.png" width=100 />  pyOpenSci: Create a Python Package Workshop Repository
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

This repository supports pyOpenSci workshops focused on Python packaging.

## Getting started
Before the workshop, be sure that you read the setup instructions that you received in an email.

You will need a GitHub and a testPyPI account to follow along.

## GitHub Codespaces

We have GitHub Codespaces configured for this workshop. To use this repository and the dev container associated with it in a workshop, instructor your learners to  create a new repository 
as a template using this repo. 

![use-template](https://github.com/user-attachments/assets/c4778b46-70dc-4d3e-86d5-b1bd50f8d183)

Open a codespace prior to attending
the workshop to ensure the environment loads properly. The initial codespace build can take up to 15 minutes.

The link above provides you with instructions 
on how to do this and how to setup the accounts you need for the workshop.

## Creating your package

To use the copier template, follow the [tutorial here](https://www.pyopensci.org/python-package-guide/tutorials/create-python-package.html) that walks you through the steps.
The command to run the copier template is:

`copier copy gh:pyopensci/pyos-package-template .`

## Cheat Sheet

Below is a command cheat sheet that will help you keep track of all of hte various commands used in our tutorials.

---

## Ship It: Command Cheat Sheet

### Codespace setup (one-time)

```console
# Shorten your terminal prompt
export PS1="$ "
```

```console
# Disable keyring. You need to do this in codesppaces only when publishing to PyPI using Hatch.
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring 
```

### Create your package

```bash
# Call the pyOpenSci package template
copier copy gh:pyOpenSci/pyos-package-template .
```

### uv commands

```bash
# Launch Python in your project environment
uv run python 
# Add package dependency 
uv add numpy 
# Remove package dependency
uv remove numpy    
# Add a development dependency
uv add --dev pytest 

```

### Hatch environments

```bash
# View all Hatch environments and scripts
hatch env show                       
# build your package; check your package distribution files using twine
hatch run build:check                
# Run test suite with coverage (across Python versions)
hatch run test:run                   
# Build sphinx documentation
hatch run docs:build 
# Serve sphinx docs locally with live reload            
hatch run docs:serve                 
# Check docstrings & code style
hatch run style:check
# Format code with ruff                
hatch run style:format               
# Check dependencies for vulnerabilities
hatch run audit:check                
```

### Build & publish

```bash
# build sdist + wheel into dist/ using native hatch in your current environment 
hatch build                          

# Publish with hatch to test pypi (r = repository)
hatch publish -r test
```

### Install a package

```bash
# Install from Test PyPI
uv pip install --index-url https://test.pypi.org/simple/ your-package-name
pip install -i https://test.pypi.org/simple/ your-package-name

# Install from GitHub
pip install git+https://github.com/username/repo-name
```

### Run tests directly with pytest (vs hatch)

```bash
 # Run all tests in your active Python envt with pytest
pytest                                   # Run tests using pytest with coverage     
pytest --cov=pyospackage --cov-report=term-missing  
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ncclementi"><img src="https://avatars.githubusercontent.com/u/7526622?v=4?s=100" width="100px;" alt="Naty Clementi"/><br /><sub><b>Naty Clementi</b></sub></a><br /><a href="https://github.com/pyOpenSci/pyopensci-workshop-create-python-package/commits?author=ncclementi" title="Code">💻</a> <a href="https://github.com/pyOpenSci/pyopensci-workshop-create-python-package/pulls?q=is%3Apr+reviewed-by%3Ancclementi" title="Reviewed Pull Requests">👀</a> <a href="https://github.com/pyOpenSci/pyopensci-workshop-create-python-package/issues?q=author%3Ancclementi" title="Bug reports">🐛</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
