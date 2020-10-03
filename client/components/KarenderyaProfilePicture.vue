<!-- For customization later on -->

<template>
    <div>
        <b-avatar
            v-if="src.length === 0 || src === 'http://localhost:8000/api/media/defaults/user.png'"
            id="profile-picture"
            icon="shop"
            :size="size"
            :variant="variant"
        />
        <b-avatar
            v-else
            id="profile-picture"
            :src="src"
            :size="size"
            :variant="variant"
        />
    </div>
</template>

<script>
export default {
    props: {
        src: {
            type: String,
            default: ""
        },
        size: {
            type: String,
            default: "150"
        },
        variant: {
            type: String,
            default: "primary"
        }
    }
};
</script>

<style lang="scss" scoped>
#profile-picture {
    size: 6em;
}
</style>
