<template>
    <div>
        <b-row>
            <b-col class="d-flex justify-content-center mb-2">
                <user-profile-picture
                    :src="user.profile_picture"
                    :size="168"
                />
            </b-col>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <h1> {{ user.first_name + " " + user.last_name }} </h1>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <p class="info-text">
                <b-icon icon="envelope" /> {{ user.email }}
            </p>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <p class="info-text">
                <b-icon icon="telephone" /> +63{{ user.contact_number }}
            </p>
        </b-row>
        <b-row class="d-flex justify-content-center">
            <p class="info-text">
                <b-icon icon="house" /> {{ user.address }}
            </p>
        </b-row>
    </div>
</template>

<script>

export default {
    props: {
        user: {
            type: Object,
            default () {
                return {
                    first_name: "",
                    last_name: "",
                    profile_picture: "",
                    email: "",
                    contact_number: "",
                    address: ""
                };
            }
        }
    }
};
</script>

<style lang="scss" scoped>
.info-text {
    text-align: center;
}
</style>
