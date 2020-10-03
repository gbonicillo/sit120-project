<template>
    <div
        id="order-summary"
        class="fixed-bottom d-flex justify-content-center text-center "
        @click="onClick"
    >
        <h5 id="summary-text">
            <b>Total Price</b> ₱ {{ totalPrice }} <br>
            <em>(Click to see full summary)</em>
        </h5>
        <b-modal
            id="order-summary-modal"
            title="Order Summary"
            header-bg-variant="primary"
            header-text-variant="light"
            @hide="onHide"
        >
            <b-table-simple
                hover
                small
                responsive
            >
                <b-thead head-variant="dark">
                    <b-tr>
                        <b-th class="text-center">
                            Item
                        </b-th>
                        <b-th class="text-center">
                            Quantity
                        </b-th>
                        <b-th class="text-center">
                            Price
                        </b-th>
                    </b-tr>
                </b-thead>
                <b-tbody>
                    <b-tr
                        v-for="item in orderItems"
                        :key="item.id"
                        @click="onClickRow(item)"
                    >
                        <b-td>
                            {{ item.name }}
                        </b-td>
                        <b-td class="text-center">
                            {{ item.quantity }}
                        </b-td>
                        <b-td class="text-center">
                            ₱ {{ item.price }}
                        </b-td>
                    </b-tr>
                    <b-tr>
                        <b-td>
                            <b>Total:</b>
                        </b-td>
                        <b-td class="text-center">
                            {{ totalQuantity }}
                        </b-td>
                        <b-td class="text-center">
                            ₱{{ totalPrice.toFixed(2) }}
                        </b-td>
                    </b-tr>
                </b-tbody>
            </b-table-simple>
        </b-modal>
        <b-modal
            id="order-remark-modal"
            title="Remark"
            header-bg-variant="primary"
            header-text-variant="light"
            @hide="onHideRemark"
        >
            <form-group
                id="remark"
                v-model="remark"
                label=""
                form-type="textarea"
                placeholder="Enter remark (optional)"
            />
        </b-modal>
    </div>
</template>

<script>
export default {
    props: {
        orderItems: {
            type: Array,
            default () {
                return [];
            }
        },
        karenderyaId: {
            type: Number,
            default: -1
        }
    },
    data () {
        return {
            remark: ""
        };
    },
    computed: {
        totalPrice () {
            let total = 0;
            this.orderItems.forEach((item) => {
                total += item.price * item.quantity;
            });
            return total;
        },
        totalQuantity () {
            let total = 0;
            this.orderItems.forEach((item) => {
                total += item.quantity;
            });
            return total;
        }
    },
    methods: {
        onClick () {
            this.$bvModal.show("order-summary-modal");
        },
        onClickRow (item) {
            const confirmation = confirm(`Are you sure you want to remove ${item.name}?`);
            if (confirmation) {
                const index = this.orderItems.indexOf(item);
                if (index > -1) {
                    this.orderItems.splice(index, 1);
                }
            }
        },
        onHide (bvEvt) {
            if (bvEvt.trigger === "ok") {
                if (this.orderItems.length > 0) {
                    const confirmation = confirm(`Place order?`);
                    if (confirmation) {
                        this.$bvModal.show("order-remark-modal");
                    }
                } else {
                    this.$toasted.global.defaultError({
                        msg: "Your order is empty"
                    });
                }
            }
        },
        onHideRemark (bvEvt) {
            if (bvEvt.trigger === "ok") {
                if (this.orderItems.length > 0) {
                    this.createOrder();
                } else {
                    this.$toasted.global.defaultError({
                        msg: "Your order is empty"
                    });
                }
            }
        },
        async createOrder () {
            const menuItems = [];
            this.orderItems.forEach((item) => {
                menuItems.push({
                    menu_item: item.id,
                    quantity: item.quantity
                });
            });
            await this.$axios.post(`/api/orders/create`, {
                user: this.$auth.user.id,
                shop: this.karenderyaId,
                remark: this.remark,
                items: menuItems
            })
                .then((response) => {
                    if (response.data.id) {
                        this.$router.push({
                            path: "/my-orders"
                        });
                    }
                })
                .catch((err) => {
                    this.$toasted.global.defaultError({
                        msg: err.response.data
                    });
                });
        }
    }
};
</script>

<style lang="scss" scoped>
@import '@/assets/theme-colors.scss';

#order-summary{
    background-color: var(--primary);
    color: var(--white);
    cursor: pointer;
    min-height: 50px;
}

#summary-text{
    margin: auto;
    min-height: 100%;
}
</style>
