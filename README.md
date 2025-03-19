# README

> [!IMPORTANT]
> The READMEs in the `backend` and `frontend` directories come from the Django and Svelte templates.
> For this exercise, look *ONLY* at this README.

## Requirements

* [uv](https://docs.astral.sh/uv/#installation)
* NPM
  * On a Debian 12 system, `sudo apt install npm` is fine
  * On Ubuntu 22.04, [install nvm](https://github.com/nvm-sh/nvm?tab=readme-ov-file#install--update-script).

## Using nvm

> [!IMPORTANT]
> If you install nvm, then the nvm installer prints some instructions.
> You must read the instructions before npm is operative.

You must run `nvm install 22` once to install Node.js 22.

In every terminal session where you need to run `npm`, execute `nvm use 22` to configure the right version of Node.js.

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

* Visit `http://127.0.0.1:5173`.
* Because you are not logged in, the application redirects you to http://127.0.0.1:8000/accounts/login/ for logging in.
* Log in as `staff`/`staff`.
* You are redirected to `http://127.0.0.1:5173/`.
* Because you are now logged in, you can view the cats.
* If you use the admin at `http://127.0.0.1:8000/admin/`, and add cats as the `staff` user, when refreshing `http://127.0.0.1:5173/` updates are visible.

## Adjusting the base URLs

This application is composed of a backend and a frontend.
Each component needs to locate the other.

The backend uses the `FRONTEND_URL` variable in the `backend/backend/dj/settings.py` file as the address of the frontend.

The frontend uses the `VITE_BACKEND_ENDPOINT` variable in the `frontend/.env.development` file as the address of the backend.

In the computer that this example was developed on, things worked with `http://127.0.0.1:8000` as the backend address and `http://127.0.0.1:5173` as the frontend address.
Note that those are the URLs in the instructions above.

In more complex environments, such as when running this example inside WSL in a Windows machine, those URLs might not work properly.
(For example, when accessing the websites using a browser in Windows outside WSL.)
In these cases, redefining the URLs to use `localhost` or the actual IP address of the device (the WSL Linux VM IP address, for instance) might be needed for things to work properly.
When redefining these URLs, adjust the URLs used in the instructions accordingly.

> [!IMPORTANT]
> Review the URL displayed in the browser URL bar constantly to make sure it matches your expectations.
