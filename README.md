# README

> [!IMPORTANT]
> The READMEs in the `backend` and `frontend` directories come from the Django and Svelte templates.
> For this exercise, look *ONLY* at this README.

## Requirements

* [uv](https://docs.astral.sh/uv/#installation)
* NPM. (On a Debian system, `sudo apt install npm` is fine.)

## Running

In one terminal:

```
cd backend
uv run devserver.py
```

On a different terminal:

```
cd frontend
npm install  # only needed once (or when the dependencies on package.json change)
npm run dev -- --host
```

In a browser:

* Visit `http://127.0.0.1:8000/api-auth/login/`.
* Log in as `staff`/`staff`.
* You are redirected to an error page, this is normal.
* Visit `http://127.0.0.1:5173/`.
