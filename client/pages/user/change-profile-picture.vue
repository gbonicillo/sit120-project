<template>
    <general-contents-container>
        <b-form
            @submit.prevent="onSubmit"
        >
            <b-row class="d-flex justify-content-center mb-2">
                <b-avatar
                    v-if="profilePictureUrl === 'http://localhost:8000/api/media/defaults/user.png'"
                    id="profile-picture-preview"
                    size="230px"
                    variant="primary"
                    button
                    badge-variant="secondary"
                    badge-top
                    @click="onProfilePictureClick"
                />
                <b-avatar
                    v-else
                    id="profile-picture-preview"
                    :src="profilePictureUrl"
                    size="230px"
                    button
                    badge-variant="secondary"
                    badge-top
                    @click="onProfilePictureClick"
                />
            </b-row>
            <b-row>
                <b-form-file
                    id="profile-picture"
                    v-model="profilePicture"
                    :required="true"
                    style="display: none"
                    accept="image/jpeg, image/png"
                />
            </b-row>

            <b-row>
                <b-button
                    type="submit"
                    variant="primary"
                    block
                    class="mt-2"
                >
                    Change Profile Picture
                </b-button>
            </b-row>
        </b-form>
    </general-contents-container>
</template>

<script>
export default {
    middleware: "auth",
    async asyncData ({ $axios, params, store, error }) {
        try {
            const result = await $axios.$get(`/api/users/${store.$auth.user.id}/profile-picture`);
            return {
                profilePictureUrl: result.profile_picture
            };
        } catch (err) {
            error({ statusCode: 500, message: "Something went wrong..." });
        }
    },
    data () {
        return {
            profilePicture: null
        };
    },
    watch: {
        profilePicture (value) {
            if (this.profilePicture !== null) {
                this.profilePictureUrl = URL.createObjectURL(this.profilePicture);
            }
        }
    },
    methods: {
        async onSubmit () {
            try {
                const formData = new FormData();
                formData.append("profile_picture", this.profilePicture);
                await this.$axios.put(`/api/users/${this.$auth.user.id}/profile-picture`, formData);
                this.$toasted.global.defaultSuccess({
                    msg: "Success: Your profile picture has been changed!"
                });
            } catch (err) {
                this.$toasted.global.defaultError({
                    msg: err
                });
            }
        },
        onProfilePictureClick () {
            $("#profile-picture").click();
        }
    }
};
</script>

<style lang="scss" scoped>
#profile-picture-preview {
    cursor: pointer;
}
</style>
