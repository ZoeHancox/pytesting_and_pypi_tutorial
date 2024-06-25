# Tutorial for Pytesting and PyPI

Basic tutorial for testing and packaging Python code. Read below on how to work with this repository.

![Tests](https://github.com/ZoeHancox/pytesting_and_pypi_tutorial/actions/workflows/tests.yml/badge.svg)

## Getting Started

To clone this repository:

- Open Git Bash, your Command Prompt or Powershell
- Navigate to the directory where you want to clone this repository: cd/path/to/directory
- Run git clone command: `git clone https://github.com/ZoeHancox/pytesting_and_pypi_tutorial.git`

---

To create a suitable environment we suggest using Anaconda:

- Build conda environment: conda create --name tut_env python=3.8
- Activate environment: conda activate tut_env
- Change to your current working directory: cd path\to\pytesting_and_pypi_tutorial
- Install requirements: pip install -r ./requirements.txt


## Pytest Practice

Once you've cloned the repository and set up your IDE as desired, head to `pytest_tutorial/pytesting.ipynb` and work through this notebook.

## TestPyPI Practice

Once you've completed the `pytesting.ipynb` notebook work through the steps below to complete your very own `passgen` TestPyPI package.

- [ ] Create a TestPyPI account [here](https://test.pypi.org/account/register/).

- [ ] Rename the `passgen` folder to `passgen_yourname`.

- [ ] Rename the `name="passgen",` in `setup.py` to `name="passgen_yourname"`.