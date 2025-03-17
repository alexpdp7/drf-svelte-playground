# backend

## Requirements

[Install uv](https://docs.astral.sh/uv/getting-started/installation/).

## Running the project

```
uv run devserver.py
```

## Creating a new application

Choose an application name.
A Django application is a Python package, and should follow [Python package and module](https://peps.python.org/pep-0008/#package-and-module-names) name conventions.
Prefer short, all-lowercase names.
(If needed, separate words with underscores.)

Replace `$APP` in the following command with the Django application name.

```
uvx copier copy gh:alexpdp7/django-tws -r app-template backend/dj/$APP
```

Add `backend.dj.$APP` to `backend/dj/settings.py`, `INSTALLED_APPS`.

Edit:

* `backend/dj/$APP/models.py` to add new models
* `backend/dj/$APP/devserver_data.py` to add new initial data
* `backend/dj/$APP/admin.py` to add models to the admin

`devserver.py` recreates the database each time it runs, and loads the data in `devserver_data.py`.
`devserver_data.py` contains some commented-out code to create users.
Use this code in your first app to always have at least a valid user for development testing.

## Running `manage.py`

```
uv run python -m backend.dj.manage ...
```

Do not use `manage.py startapp` to create applications, use the `copier` command above instead.

## Handling model changes

If you are experimenting with models, then every time you run `devserver.py`, `devserver.py` deploys the latest changes to your models without having to create a migration.
If you make changes to models, then run `devserver.py` to apply them immediately.
(You can also make changes to the admin to be able to validate that your model changes look good.)

Once you are satisfied with your model changes, run `uv run python -m backend.dj.manage makemigrations` to create a migration and "solidify" the changes.

## Pushing your code to a new Git repository

* Run `git init` from the project root to initialize the project directory as an empty Git repository.
* Run `git add .` to add the current contents of the project to the first commit.
* Run `git status` to review the files that the commit will contain.
* Run `git commit` to commit the changes.

Once you have a local Git repository with an initial version of your code, you can push it to a Git forge such as GitHub.
Review the Git forge instructions to learn how to do this.

### Pushing to GitHub

* Click the plus (+) sign in the top right corner of every GitHub page, then click "New repository".
* In the form, leave the "Add a README file" checkbox unchecked, and the "Add .gitignore" and "Choose a license" dropdowns as "None".
* Fill the rest of the form, then click "Create repository".
* Follow the steps under "...or push an existing repository from the command line" to push the initial version of your code to GitHub.

## Handling Django version updates and other dependencies

The `pyproject.toml` file contains the following line:

```
    "django~=5.1.6",
```

This means that the project will start with any 5.1.x version of Django, starting from 5.1.6.

Django training wheels targets Django 5.1.x, but later versions of Django might require updates to the generated code.
Django training wheels helps you kickstart Django projects, but does not tackle the problem of keeping a project updated with more recent Django versions.

You should update your project to be on supported versions of Django, especially if you expose your project to the Internet.
Review ["managing dependencies" in the uv documentation](https://docs.astral.sh/uv/guides/projects/#managing-dependencies) to learn how to update dependencies.

Automated dependency update tools exist, such as [Dependabot](https://docs.github.com/en/code-security/dependabot) or [Mend Renovate](https://www.mend.io/renovate/).
