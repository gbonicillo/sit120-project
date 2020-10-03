<template>
    <general-contents-container page-title="Register">
        <b-form
            @submit.prevent="onSubmit"
            @input="onInput"
        >
            <h4>User Information</h4>
            <b-row>
                <form-group
                    id="first-name"
                    v-model="form.first_name"
                    label="First Name"
                    placeholder="Enter first name"
                    :required="true"
                    class="col-lg-6 col-md-12"
                />
                <form-group
                    id="last-name"
                    v-model="form.last_name"
                    label="Last Name"
                    placeholder="Enter last name"
                    :required="true"
                    class="col-lg-6 col-md-12"
                />
            </b-row>
            <h4>Contact Information</h4>
            <form-group
                id="email"
                v-model="form.email"
                label="Email"
                placeholder="Enter email"
                type="email"
                :required="true"
            />
            <form-group
                id="contactNumber"
                v-model="form.contact_number"
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
    middleware: "auth",
    async asyncData ({ $axios, params, error, store }) {
        try {
            const user = await $axios.$get(`/api/users/${store.$auth.user.id}/update`);
            return {
                form: user
            };
        } catch (err) {
            error({ statusCode: 500, message: "Something went wrong..." });
        }
    },
    data () {
        return {
            error: null,
            validationErrors: null,
            otherError: ""

        };
    },
    computed: {
        profilePictureURL () {
            let url = "";
            if (this.form.profilePicture === null) {
                url = "http://localhost:8000/api/media/defaults/user.png";
            } else {
                url = URL.createObjectURL(this.form.profilePicture);
            }
            return url;
        }
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.put(`/api/users/${this.$auth.user.id}/update`, {
                email: this.form.email,
                contact_number: this.form.contact_number,
                first_name: this.form.first_name,
                last_name: this.form.last_name,
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
                .then((response) => {
                    this.$router.push({
                        path: "/user/"
                    });
                })
                .catch((err) => {
                    if (err.response.data.username) {
                        this.error = err.response.data.username;
                        $("#username")[0].setCustomValidity(this.error);
                    } else if (err.response.data.email) {
                        this.error = err.response.data.email;
                        $("#email")[0].setCustomValidity(this.error);
                    } else {
                        this.$toasted.global.defaultError({
                            msg: err.response.data.details
                        });
                    }
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
