<template>
    <b-modal
        v-if="item !== null"
        :id="modalId"
        :title="`Add how many ${item.name}`"
        header-bg-variant="primary"
        header-text-variant="light"
        @hide="onHide"
    >
        <b-row class="mb-2">
            <b-col>
                <b>Total Price: </b> ₱ {{ (item.price * quantity).toFixed(2) }}
            </b-col>
        </b-row>
        <b-row>
            <b-col>
                <b-input v-model="quantity" type="number" min="0" />
            </b-col>
        </b-row>
    </b-modal>
</template>

<script>
export default {
    props: {
        modalId: {
            type: String,
            default: "add-item-to-order-modal"
        },
        item: {
            type: Object,
            default: null
        }
    },
    data () {
        return {
            quantity: 0
        };
    },
    methods: {
        onHide (bvEvt) {
            if (bvEvt.trigger === "ok" && this.quantity > 0) {
                const itemToAdd = {
                    id: this.item.id,
                    name: this.item.name,
                    price: this.item.price,
                    quantity: parseInt(this.quantity)
                };
                this.$emit("add-item", itemToAdd);
            }
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
