<template>
    <general-contents-container page-title="Update your karenderya">
        <b-form
            @submit.prevent="onSubmit"
            @input="onInput"
        >
            <h4>Karenderya Info</h4>
            <form-group
                id="name"
                v-model="form.name"
                label="Name"
                placeholder="Enter name"
                :required="true"
            />
            <b-form-group
                label="Karenderya Profile Picture (Click on image below to select file)"
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
                    icon="shop"
                    size="230px"
                    button
                    variant="primary"
                    @click="onClickProfilePicture"
                />
            </b-row>
            <form-group
                id="contactNumber"
                v-model="form.contactNumber"
                form-type="tel"
                label="Contact Number"
                placeholder="Enter contact number (should be exactly 10 numbers long)"
                :required="true"
            />
            <h4>Address</h4>
            <form-group
                id="line-1"
                v-model="form.address.line_1"
                label="Line 1"
                placeholder="Enter address line 1 (Street address)"
                :required="true"
            />
            <form-group
                id="line-2"
                v-model="form.address.line_2"
                label="Line 2"
                placeholder="Enter address line 2 (Apartment number, etc | Optional)"
            />
            <form-group
                id="barangay"
                v-model="form.address.barangay"
                label="Barangay"
                placeholder="Enter barangay"
                :required="true"
            />
            <form-group
                id="city"
                v-model="form.address.city"
                label="City"
                placeholder="Enter city"
                :required="true"
            />
            <form-group
                id="province"
                v-model="form.address.province"
                label="Province"
                placeholder="Enter province"
                :required="true"
            />
            <form-group
                id="region"
                v-model="form.address.region"
                label="Region"
                placeholder="Enter region"
                :required="true"
            />
            <form-group
                id="zip-code"
                v-model="form.address.zip_code"
                label="Zip Code"
                placeholder="Enter zip code"
                type="number"
                :required="true"
                maxlength="4"
            />
            <b-button block type="submit" variant="primary">
                Update
            </b-button>
        </b-form>
        {{ form.address }}
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
            const result = await $axios.$get(`/api/user/my-shop`);
            const karenderya = await $axios.$get(`/api/shops/${result.id}/update`);
            const profilePictureUrl = karenderya.profile_picture;
            delete karenderya.profile_picture;
            delete karenderya.menu_items;
            return {
                karenderyaId: result.id,
                form: {
                    name: karenderya.name,
                    contactNumber: karenderya.contact_number,
                    address: karenderya.address
                },
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
                contactNumber: "",
                address: {
                    line_1: "",
                    line_2: "",
                    barangay: "",
                    city: "",
                    province: "",
                    region: "",
                    zipCode: ""
                }
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
            await this.$axios.put(`/api/shops/${this.karenderyaId}/update`, {
                name: this.form.name,
                contact_number: this.form.contactNumber,
                owner: this.$auth.user.id,
                address: {
                    line_1: this.form.address.line_1,
                    line_2: this.form.address.line_2,
                    barangay: this.form.address.barangay,
                    city: this.form.address.city,
                    province: this.form.address.province,
                    region: this.form.address.region,
                    zip_code: this.form.address.zip_code
                }
            })
                .then(async (response) => {
                    if (response.data.id) {
                        if (this.profilePicture !== null) {
                            const formData = new FormData();
                            formData.append("profile_picture", this.profilePicture);
                            await this.$axios.put(`/api/shops/${response.data.id}/profile-picture`, formData);
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
        onInput (evt) {
            $("#zip-code")[0].setCustomValidity(
                $("#zip-code")[0].value.length <= 4 ? "" : "Zip code max length is 4"
            );
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
