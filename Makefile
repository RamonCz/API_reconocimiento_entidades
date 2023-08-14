# set the name of the conda environment
CONDA_ENV_NAME=myenv

# set the name of the virtual environment
VENV_NAME=myenv

# set the path to the requirements.txt file
REQUIREMENTS=requirements.txt

# set the path to the main.py script
MAIN_SCRIPT=app/main.py

# set the path to the test_model.py script
TEST_SCRIPT=test/test_model.py

# create the conda environment
create-conda-env:
	conda create --name $(CONDA_ENV_NAME) --file $(REQUIREMENTS)

# activate the conda environment
activate-conda-env:
	conda activate $(CONDA_ENV_NAME)

# create the virtual environment with venv
create-venv:
	python3 -m venv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && pip install -r $(REQUIREMENTS)

# activate the virtual environment with venv
activate-venv:
	. $(VENV_NAME)/bin/activate

# run the main.py script with Flask
run-main:
	FLASK_APP=$(MAIN_SCRIPT) flask run

# run tests in test_model.py with pytest
test-model:
	pytest $(TEST_SCRIPT)


install_conda:
	create-conda-env activate-conda-env

install_env:
	create-venv activate-venv:
