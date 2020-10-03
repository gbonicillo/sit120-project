<template>
    <div class="card mb-3 menu-item-card">
        <img
            class="card-img-top menu-item-card-img"
            :src="menuItem.picture"
        >
        <div class="card-header">
            <h5 class="card-title text-center">
                {{ menuItem.name }}
            </h5>
        </div>
        <div class="card-body">
            <h5 class="card-title">
                ‎₱ {{ menuItem.price }}
            </h5>
            <p class="card-text">
                {{ menuItem.description }}
            </p>
        </div>
        <div
            v-if="!!this.$slots.default"
            class="card-footer text-center"
        >
            <slot />
        </div>
    </div>
</template>

<script>
export default {
    props: {
        menuItem: {
            type: Object,
            default () {
                return {
                    name: "",
                    price: "",
                    picture: "",
                    description: ""
                };
            }
        }
    }
};
</script>

<style lang="scss" scoped>
.menu-item-card{
    max-width: 300px;
}

.menu-item-card-img {
    max-width: 300px;
}

.card-header{
    background-color: var(--primary);
    color: var(--light);
}
</style>
