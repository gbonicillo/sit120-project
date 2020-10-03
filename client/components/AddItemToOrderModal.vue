<template>
    <b-modal
        v-if="item !== null"
        :id="modalId"
        :title="`Add how many ${item.name}`"
        header-bg-variant="primary"
        header-text-variant="light"
        @ok="onOk"
        @show="resetModal"
        @hidden="resetModal"
        @cancel="resetModal"
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
        onOk () {
            if (this.quantity > 0) {
                const itemToAdd = {
                    id: this.item.id,
                    name: this.item.name,
                    price: this.item.price,
                    quantity: parseInt(this.quantity)
                };
                this.$emit("add-item", itemToAdd);
            }
        },
        resetModal () {
            this.quantity = 0;
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
