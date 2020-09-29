<template>
    <div>
        Logging out please wait...
    </div>
</template>

<script>
export default {
    async created () {
        await this.$auth.logout();
    }
};
</script>
