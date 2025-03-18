import type { PageLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load: PageLoad = async ({ fetch, params, url }) => {
	const res = await fetch(import.meta.env.VITE_BACKEND_ENDPOINT + "/api/cats/", { options: { credentials: "include" }});

	if (res.status == 403) {
	   redirect(302, import.meta.env.VITE_BACKEND_ENDPOINT + "/accounts/login?next=" + url.href);
	}
	const item = await res.json();

	return { item };
};
