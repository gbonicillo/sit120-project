<template>
    <div>
        <b-row>
            <b-col class="d-flex justify-content-center mb-2">
                <karenderya-profile-picture
                    :src="karenderya.profile_picture"
                    :size="avatarSize"
                />
            </b-col>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <h1 class="text-center">
                {{ karenderya.name }}
            </h1>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <p class="info-text">
                <b-icon icon="telephone" /> +63{{ karenderya.contact_number }}
            </p>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <p class="info-text">
                <b-icon icon="house" /> {{ karenderya.address }}
            </p>
        </b-row>
    </div>
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
        },
        avatarSize: {
            type: String,
            default: "168"
        }
    }
};
</script>

<style lang="scss" scoped>
.info-text {
    text-align: center;
}
</style>
