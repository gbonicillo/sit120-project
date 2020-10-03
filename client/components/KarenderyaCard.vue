<template>
    <b-card class="karenderya-card">
        <b-card-text @click="$emit('click')">
            <karenderya-profile :karenderya="karenderya" avatar-size="75" />
        </b-card-text>
    </b-card>
</template>

<script>
export default {
    props: {
        karenderya: {
            type: Object,
            default () {
                return {
                    name: "",
                    profile_picture: "",
                    contact_number: "",
                    address: ""
                };
            }
        }
    }
};
</script>

<style lang="scss" scoped>
.karenderya-card{
    width:100%;
}
</style>
