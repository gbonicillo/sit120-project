<template>
    <general-contents-container>
        <b-row>
            <b-jumbotron
                class="w-100"
                header="Welcome to Check my Car!"
                lead="The site for checking reported issues and recalls for cars!"
                bg-variant="dark"
                text-variant="light"
            >
                <p>
                    Try searching report for your car by typing your car's make and/or model in the search bar
                </p>
            </b-jumbotron>
        </b-row>
    </general-contents-container>
</template>

<script>
export default {
    async asyncData ({ $axios, params }) {
        try {
            const result = await $axios.$get("/api/cars/");
            return {
                cars: result.results,
                contentCount: result.count,
                nextPage: result.next,
                prevPage: result.previous
            };
        } catch (err) {
            return { cars: [] };
        }
    },
    data () {
        return {
            cars: []
        };
    }
};
</script>
