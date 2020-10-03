<template>
    <general-contents-container>
        <b-row class="d-flex justify-content-center mb-2">
            <karenderya-profile
                :karenderya="karenderya"
            />
        </b-row>
        <b-row class="d-flex justify-content-center mb-2">
            <b-button
                to="/my-karenderya/update"
                variant="primary"
            >
                Update Info
            </b-button>
        </b-row>
        <b-row class="d-flex justify-content-center mb-2">
            <h1>Menu</h1>
        </b-row>
        <b-row
            class="d-flex justify-content-center mb-3"
        >
            <b-button
                to="/my-karenderya/add-menu-item"
                variant="primary"
            >
                Add Menu Item
            </b-button>
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
                >
                    <b-row>
                        <b-col>
                            <b-button
                                variant="danger"
                                block
                            >
                                Delete
                            </b-button>
                        </b-col>
                        <b-col>
                            <b-button
                                variant="primary"
                                block
                                :to="`/my-karenderya/update-menu-item/${item.id}`"
                            >
                                Update
                            </b-button>
                        </b-col>
                    </b-row>
                </menu-item-card>
            </b-col>
        </b-row>
    </general-contents-container>
</template>

<script>
export default {
    middleware: ["auth", "is-owner"],
    async asyncData ({ $axios, params, store, error, redirect }) {
        try {
            const result = await $axios.$get(`/api/user/my-shop`)
                .catch((err) => {
                    if (err.response.status === 404) {
                        redirect(`/my-karenderya/create`);
                    }
                });
            const karenderya = await $axios.$get(`/api/shops/${result.id}`);
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
