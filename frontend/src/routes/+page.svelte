<script lang="ts">
	import type { PageProps } from './$types';

	let { data }: PageProps = $props();
</script>

<h1>Cats</h1>

<ul>
	{#each data.item as cat}
	       <li>{cat.name}</li>
	{/each}
</ul>
