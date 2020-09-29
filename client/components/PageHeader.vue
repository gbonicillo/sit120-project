<template>
    <h1 class="display-4">
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
