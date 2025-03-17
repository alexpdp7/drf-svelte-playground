# README

In one terminal:

```
cd backend
uv run devserver.py
```

On a different terminal:

```
cd frontend
npm run dev -- --host
```

In a browser:

* Visit `http://127.0.0.1:8000/api-auth/login/`.
* Log in as `staff`/`staff`.
* You are redirected to an error page, this is normal.
* Visit `http://127.0.0.1:5173/`.
