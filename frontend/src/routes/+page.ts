import type { PageLoad } from './$types';
import { redirect } from '@sveltejs/kit';

export const load: PageLoad = async ({ fetch, params }) => {
	const res = await fetch("http://127.0.0.1:8000/api/cats/", { options: { credentials: "include" }});
	console.log(res);
	if (res.status == 403) {
	   redirect(302, "http://127.0.0.1:8000/accounts/login?next=http://127.0.0.1:5173");
	}
	const item = await res.json();

	return { item };
};
