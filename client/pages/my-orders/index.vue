<template>
    <general-contents-container page-title="Orders">
        <h2 class="text-muted">
            <em>Tap on order to show remarks</em>
        </h2>
        <b-row
            v-for="order in orders"
            :key="order.id"
            class="mb-2"
        >
            <user-order-card
                :order="order"
                @status-changed="updatePage"
            />
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
        <h2
            v-if="count===0"
            class="text-muted"
        >
            <em>No orders</em>
        </h2>
    </general-contents-container>
</template>

<script>
export default {
    middleware: ["auth"],
    async asyncData ({ $axios, params, redirect, error, store }) {
        try {
            const ordersResult = await $axios.$get(`/api/users/${store.$auth.user.id}/orders`);
            return {
                count: ordersResult.count,
                orders: ordersResult.results,
                nextPage: ordersResult.next,
                prevPage: ordersResult.previous
            };
        } catch (err) {
            error({ statusCode: 500, message: "Something went wrong..." });
        }
    },
    methods: {
        async fetchPage (pageUrl) {
            try {
                const url = pageUrl.replace(this.$axios.defaults.baseURL, "");
                const ordersResult = await this.$axios.$get(url);
                this.orders = ordersResult.results;
                this.nextPage = ordersResult.next;
                this.prevPage = ordersResult.previous;
            } catch (err) {
                this.$toasted.global.defaultError();
            }
        },
        updatePage () {
            this.fetchPage(`/api/shops/${this.karenderyaId}/orders`);
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
