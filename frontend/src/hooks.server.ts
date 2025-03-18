import type { HandleFetch } from '@sveltejs/kit';
export const handleFetch: HandleFetch = async ({ event, request, fetch }) => {
	if (request.url.startsWith(import.meta.env.VITE_BACKEND_ENDPOINT)) {
		request.headers.set('cookie', event.request.headers.get('cookie'));
	}

	return fetch(request);
};
