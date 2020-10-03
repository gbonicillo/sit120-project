<template>
    <general-contents-container page-title="Karenderyas">
        <b-row class="mb-2">
            <b-col>
                <generic-search-bar
                    v-model="searchTerm"
                    placeholder="Search a karenderya here!"
                    @search="onSearch"
                />
            </b-col>
        </b-row>
        <b-row
            class="d-flex justify-content-center"
        >
            <b-col
                v-for="karenderya in karenderyas"
                :key="karenderya.id"
                lg="6"
                sm="12"
                class="mb-2"
            >
                <karenderya-card
                    :karenderya="karenderya"
                    style="cursor: pointer"
                    @click="onClickKarenderya(karenderya.id)"
                />
            </b-col>
        </b-row>
        <b-row>
            <b-col cols="6">
                <b-button
                    v-if="prevPage !== null"
                    variant="primary"
                    block
                    @click="fetchPage(prevPage)"
                >
                    <b-icon
                        icon="arrow-left-circle"
                    />
                </b-button>
            </b-col>
            <b-col cols="6">
                <b-button
                    v-if="nextPage !== null"
                    variant="primary"
                    block
                    @click="fetchPage(nextPage)"
                >
                    <b-icon
                        icon="arrow-right-circle"
                    />
                </b-button>
            </b-col>
        </b-row>
    </general-contents-container>
</template>

<script>
export default {
    middleware: "auth",
    async asyncData ({ $axios, params, error }) {
        try {
            const result = await $axios.$get("/api/shops");
            return {
                karenderyas: result.results,
                count: result.count,
                nextPage: result.next,
                prevPage: result.previous
            };
        } catch (err) {
            error({ statusCode: 500, message: "Something went wrong..." });
        }
    },
    data () {
        return {
            searchTerm: ""
        };
    },
    methods: {
        async fetchPage (pageUrl) {
            try {
                const url = pageUrl.replace(this.$axios.defaults.baseURL, "");
                const result = await this.$axios.$get(url);
                this.karenderyas = result.results;
                this.nextPage = result.next;
                this.prevPage = result.previous;
            } catch (err) {
                this.$toasted.global.defaultError();
            }
        },
        onClickKarenderya (id) {
            this.$router.push({
                path: `/karenderyas/${id}`
            });
        },
        onSearch () {
            // Remove " City" or " city" from search term
            const searchTerm = this.searchTerm.replace(/\s+[Cc]ity\s*/g, "");
            this.fetchPage(`/api/shops/?search=${searchTerm}`);
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
