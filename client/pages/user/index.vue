<template>
    <general-contents-container>
        <user-profile
            :user="user"
        />
    </general-contents-container>
</template>

<script>

export default {
    middleware: "auth",
    async asyncData ({ $axios, paramas, store, error }) {
        try {
            const user = await $axios.$get(`/api/users/${store.$auth.user.id}`);
            return {
                user
            };
        } catch (err) {
            error({ statusCode: 500, message: "Something went wrong..." });
        }
    }
};
</script>

<style lang="scss" scoped>
.info-text {
    text-align: center;
}
</style>
