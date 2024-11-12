# Clue_less

## Description:
JHU Foundations of Software Engineering Team Project

## Prequisites:
-[Anaconda]

## Setting Up the Environment
### Clone the Repository:
1. Clone the repository to your local machine using Git.

    eg. git clone <git@github.com>:jliburd2167/Clue_less.git

2. Navigate to the root of the directory

### Create and Activate a Conda Environment:

 Create a new conda environment using the clue_release_env.yml file.

    conda env create -f clue_release_env.yml -n clue_release

note: This step only needs to be done once.

    conda activate clue_release

### Leaving the Conda Environment
When you are done working, you can deactivate the Conda evironment.

	conda deactivate

## Databse Set up

### Migrate the Databse
Navigate to the root directory of rthe respository and type the following commands:

	python manage.py makemigrations
	python manage.py migrate

## Updating environment dependencies
If you make any changes to the dependencies, remember to update the clue_env_release.yml file using:

	conda env export > clue_env_release.yml

## Launching the Environment

Navigate to the root directory of the repository and type the following command from inside the clue_release environment to lauch the server application:

	daphne clue_less.asgi:application

In a new terminal, navigate to the Client directory and type the following command to launch the client Command Line Interface:

	python ClientCli.py


## Django Admin Interface

1. Create a Super user account

Navigate to the root of the project repository and type the following command

	python manage.py createsuperuser

2. Once you have created your super user account, launch the server app using the steps outlined above.

3. Open Your Web Browser: Navigate to <http://127.0.0.1:8000/admin/>.

## Run Test Cases

1. To run the Test Cases associated with the project navigate to the root project directory.
2. Enter the command:

### Django Test
```bash
python3 manage.py test <module>
```
### Pytest
```bash
python3 pytest
```

note: use the "-s" in pytest for debugging printouts

### References:
[Django Testing Overview](https://docs.djangoproject.com/en/5.1/topics/testing/overview/)
[Django Testing Examples](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
