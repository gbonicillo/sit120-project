<template>
    <b-card
        v-if="order !== null"
        style="width:100%"
        :header-class="cardHeaderClass"
    >
        <template
            v-slot:header
        >
            {{ cardHeaderText }}
        </template>
        <b-card-text
            style="cursor:pointer;"
            @click="toggleRemarks(order.id)"
        >
            <b-row>
                <b-col
                    lg="2"
                    sm="12"
                >
                    <b-row
                        class="d-flex justify-content-center mb-2"
                    >
                        <user-profile-picture
                            :src="order.user.profile_picture"
                            size="100"
                        />
                    </b-row>
                    <b-row
                        class="d-flex justify-content-center"
                    >
                        <p class="text-center">
                            {{ order.user.name }}
                        </p>
                        <p class="text-center">
                            {{ order.user.address }}
                        </p>
                        <p class="text-center">
                            <b>Order Date</b> <br>
                            {{ order.created_at }}
                        </p>
                    </b-row>
                </b-col>
                <b-col
                    lg="10"
                    sm="12"
                    style="width:100%"
                >
                    <b-row class="d-flex justify-content-center">
                        <h4>
                            Orders
                        </h4>
                    </b-row>
                    <b-row class="mb-2">
                        <b-list-group style="width:100%">
                            <b-list-group-item
                                v-for="item in order.menu_items"
                                :key="item.name"
                            >
                                <b-row>
                                    <b-col cols="6">
                                        {{ item.name }} x{{ item.quantity }}
                                    </b-col>
                                    <b-col
                                        cols="6"
                                        class="d-flex justify-content-end"
                                    >
                                        ₱ {{ (item.price * item.quantity).toFixed(2) }}
                                    </b-col>
                                </b-row>
                            </b-list-group-item>
                        </b-list-group>
                    </b-row>
                    <b-row
                        class="d-flex justify-content-end"
                    >
                        <h5 class="mr-2">
                            <b>Total:</b> ₱ {{ getTotalPrice(order.menu_items).toFixed(2) }}
                        </h5>
                    </b-row>
                    <b-row
                        :id="`remarks-${order.id}`"
                        style="display:none"
                    >
                        <b-col>
                            <h5>Remarks</h5>
                            {{ order.remark }}
                        </b-col>
                    </b-row>
                </b-col>
            </b-row>
        </b-card-text>
        <b-card-footer
            v-if="order.status === 'PD'"
            style="padding:0px;"
        >
            <b-row>
                <b-col cols="6">
                    <b-button
                        variant="danger"
                        style="height:100%"
                        block
                        @click="updateStatus('RJ', order.id)"
                    >
                        Reject
                    </b-button>
                </b-col>
                <b-col cols="6">
                    <b-button
                        variant="success"
                        style="height:100%"
                        block
                        @click="updateStatus('AC', order.id)"
                    >
                        Accept
                    </b-button>
                </b-col>
            </b-row>
        </b-card-footer>
    </b-card>
</template>

<script>
export default {
    props: {
        order: {
            type: Object,
            default: null
        }
    },
    computed: {
        cardHeaderClass () {
            let headerClass = "card-header-pending";

            switch (this.order.status) {
            case "PD":
                headerClass = "card-header-pending";
                break;
            case "AC":
                headerClass = "card-header-accepted";
                break;
            case "RJ":
                headerClass = "card-header-canceled";
                break;
            case "CN":
                headerClass = "card-header-canceled";
                break;
            }

            return headerClass;
        },
        cardHeaderText () {
            let headerText = "PENDING";

            switch (this.order.status) {
            case "PD":
                headerText = "PENDING";
                break;
            case "AC":
                headerText = "ACCEPTED";
                break;
            case "RJ":
                headerText = "REJECTED";
                break;
            case "CN":
                headerText = "CANCELLED";
                break;
            }

            return headerText;
        }
    },
    methods: {
        getTotalPrice (items) {
            let total = 0;
            items.forEach((item) => {
                total += item.price * item.quantity;
            });

            return total;
        },
        toggleRemarks (id) {
            $(`#remarks-${id}`).slideToggle("fast");
        },
        updateStatus (status, id) {
            this.$axios.put(`/api/orders/${id}/update-status`, {
                status
            }).then((response) => {
                let msg = "";
                switch (status) {
                case "AC":
                    msg = "Accepted order!";
                    break;
                case "RJ":
                    msg = "Rejected order!";
                    break;
                }
                if (response.data.id) {
                    this.$emit("status-changed");
                    this.$toast.global.defaultSuccess({
                        msg
                    });
                }
            }).catch((err) => {
                if (err.response.data.status) {
                    this.$toast.global.error({
                        msg: err.response.data.status
                    });
                }
            });
        }
    }
};
</script>

<style lang="scss" scoped>
.card-header-pending{
    background-color: var(--warning);
    color: var(--light);
}
.card-header-accepted{
    background-color: var(--success);
    color: var(--light);
}
.card-header-canceled{
    background-color: var(--danger);
    color: var(--light);
}

</style>
