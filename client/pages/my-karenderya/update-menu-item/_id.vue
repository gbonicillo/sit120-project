<template>
    <general-contents-container page-title="Add Menu Item">
        <b-form
            @submit.prevent="onSubmit"
        >
            <h4>Menu Item Info</h4>
            <form-group
                id="name"
                v-model="form.name"
                label="Name"
                placeholder="Enter name"
                :required="true"
            />
            <b-form-group
                label="Menu Item Picture (Click on image below to select file)"
                label-for="profile-picture"
            >
                <b-form-file
                    id="profile-picture"
                    v-model="profilePicture"
                    style="display: none"
                    accept="image/jpeg, image/png"
                />
            </b-form-group>
            <b-row class="d-flex justify-content-center mb-2">
                <b-avatar
                    id="profile-picture-preview"
                    :src="profilePictureUrl"
                    icon="cart"
                    size="230px"
                    button
                    variant="primary"
                    @click="onClickProfilePicture"
                />
            </b-row>
            <form-group
                id="price"
                v-model="form.price"
                label="Price"
                form-type="price"
                placeholder="0.00"
                :required="true"
            />
            <form-group
                id="description"
                v-model="form.description"
                label="Description"
                form-type="textarea"
                placeholder="Enter description (optional)"
            />
            <b-button block type="submit" variant="primary">
                Update
            </b-button>
        </b-form>
    </general-contents-container>
</template>

<script>
import GeneralContentsContainer from "@/components/GeneralContentsContainer";
import FormGroup from "@/components/FormGroup";

export default {
    components: {
        GeneralContentsContainer,
        FormGroup
    },
    middleware: ["auth", "is-owner"],
    async asyncData ({ $axios, params, redirect, error }) {
        try {
            const karenderya = await $axios.$get(`/api/user/my-shop`);
            const menuItem = await $axios.$get(`/api/menu-items/${params.id}/update`);
            const profilePictureUrl = menuItem.picture;
            delete menuItem.picture;
            return {
                form: menuItem,
                karenderyaId: karenderya.id,
                profilePictureUrl
            };
        } catch (err) {
            if (err.response.status === 404) {
                redirect(`/my-karenderya/create`);
            } else {
                error({ statusCode: 500, message: "Something went wrong..." });
            }
        }
    },
    data () {
        return {
            // Can't watch nested value so place outside
            profilePicture: null,
            form: {
                name: "",
                price: "",
                description: ""
            }

        };
    },
    computed: {
        profilePictureURL () {
            let url = "";
            if (this.profilePicture === null) {
                url = "http://localhost:8000/api/media/defaults/user.png";
            } else {
                url = URL.createObjectURL(this.profilePicture);
            }
            return url;
        }
    },
    watch: {
        profilePicture (value) {
            if (this.profilePicture !== null) {
                this.profilePictureUrl = URL.createObjectURL(this.profilePicture);
            }
        }
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.put(`/api/menu-items/${this.form.id}/update`, {
                name: this.form.name,
                price: this.form.price,
                description: this.form.description,
                shop: this.karenderyaId
            })
                .then(async (response) => {
                    if (response.data.id) {
                        if (this.profilePicture !== null) {
                            const formData = new FormData();
                            formData.append("picture", this.profilePicture);
                            await this.$axios.put(`/api/menu-items/${response.data.id}/picture`, formData);
                        }
                        this.$router.push({
                            path: "/my-karenderya"
                        });
                    }
                })
                .catch((err) => {
                    this.$toasted.global.defaultError({
                        msg: err.response.data.details
                    });
                });
        },
        onClickProfilePicture (evt) {
            $("#profile-picture").click();
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

</style>
