<template>
    <general-contents-container :page-title="`Order to ${karenderya.name}`">
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
                >
                    <b-button
                        v-b-modal="`add-item-modal-${item.id}`"
                        variant="success"
                        block
                    >
                        Add
                    </b-button>
                </menu-item-card>
                <add-item-to-order-modal
                    :modal-id="`add-item-modal-${item.id}`"
                    :item="item"
                    @add-item="addItem"
                />
            </b-col>
        </b-row>
        <order-summary
            :order-items="orderItems"
            :karenderya-id="karenderya.id"
        />
    </general-contents-container>
</template>

<script>
export default {
    middleware: "auth",
    async asyncData ({ $axios, params, error }) {
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
    },
    data () {
        return {
            modalVisible: false,
            orderItems: []
        };
    },
    methods: {
        addItem (item) {
            // If already in orderItems list, add quantity instead
            if (this.orderItems.filter(i => i.id === item.id).length > 0) {
                this.orderItems.filter(i => i.id === item.id)[0].quantity += item.quantity;
            } else {
                this.orderItems.push(item);
            }
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
