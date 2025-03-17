import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch, params }) => {
	const res = await fetch("http://127.0.0.1:8000/api/cats/", { options: { credentials: "include" }});
	const item = await res.json();
	console.log(item);

	return { item };
};
