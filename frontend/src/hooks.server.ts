import type { HandleFetch } from '@sveltejs/kit';
export const handleFetch: HandleFetch = async ({ event, request, fetch }) => {
	if (request.url.startsWith('https://127.0.0.1:8000/')) {
		request.headers.set('cookie', event.request.headers.get('cookie'));
	}

	return fetch(request);
};
