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

## Adjusting the base URLs

This application is composed of a backend and a frontend.
Each component needs to locate the other.

The backend uses the `FRONTEND_URL` variable in the `backend/backend/dj/settings.py` file as the address of the frontend.

The frontend uses the `VITE_BACKEND_ENDPOINT` variable in the `frontend/.env.development` file as the address of the backend.

In the computer that this example was developed on, things worked with `http://127.0.0.1:8000` as the backend address and `http://127.0.0.1:5173` as the frontend address.
Note that those are the URLs in the instructions above.

In more complex environemnts, such as when running this example inside WSL in a Windows machine, those URLs might not work properly.
(For example, when accessing the websites using a browser in Windows outside WSL.)
In these cases, redefining the URLs to use `localhost` or the actual IP address of the device (the WSL Linux VM IP address, for instance) might be needed for things to work properly.
When redefining these URLs, adjust the URLs used in the instructions accordingly.

> [!IMPORTANT]
> Review the URL displayed in the browser URL bar constantly to make sure it matches your expectations.
