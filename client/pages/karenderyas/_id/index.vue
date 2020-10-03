<template>
    <general-contents-container>
        <b-row class="d-flex justify-content-center mb-2">
            <karenderya-profile
                :karenderya="karenderya"
            />
        </b-row>
        <b-row
            class="d-flex justify-content-center mb-3"
        >
            <b-button
                block
                :to="`/karenderyas/${karenderya.id}/place-order`"
                variant="success"
            >
                Place an Order
            </b-button>
        </b-row>
        <b-row class="d-flex justify-content-center mb-2">
            <h1>Menu</h1>
        </b-row>
        <b-row
            class="justify-content-center"
        >
            <b-col
                v-for="item in menuItems"
                :key="item.id"
                class="lg-4 md-6 sm-12"
            >
                <menu-item-card
                    :menu-item="item"
                />
            </b-col>
        </b-row>
    </general-contents-container>
</template>

<script>
export default {
    middleware: ["auth"],
    async asyncData ({ $axios, params, store, error, redirect }) {
        try {
            const karenderya = await $axios.$get(`/api/shops/${params.id}`);
            const menuItemsResult = karenderya.menu_items;
            delete karenderya.menu_items;
            return {
                karenderya,
                menuItems: menuItemsResult
            };
        } catch (err) {
            error({ statusCode: 500, message: "Something went wrong..." });
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
