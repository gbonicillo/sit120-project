<template>
    <h1 class="display-4 page-title text-center" style="width:100%">
        {{ pageTitle }}
    </h1>
</template>

<script>
export default {
    props: {
        pageTitle: {
            type: String,
            default: "Page Title"
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
