<template>
    <general-contents-container page-title="Register">
        <b-form
            @submit.prevent="onSubmit"
            @input="onInput"
        >
            <h4>User Information</h4>
            <form-group
                id="username"
                v-model="form.username"
                label="Username"
                placeholder="Enter Username"
                :required="true"
            />
            <b-row>
                <b-col lg="6" md="12">
                    <form-group
                        id="password"
                        v-model="form.password"
                        label="Password"
                        placeholder="Enter password"
                        type="password"
                        :required="true"
                    />
                </b-col>
                <b-col lg="6" md="12">
                    <form-group
                        id="confirm-password"
                        label="Confirm Password"
                        placeholder="Confirm Password"
                        type="password"
                        :required="true"
                    />
                </b-col>
            </b-row>
            <form-group
                id="type"
                v-model="form.type"
                label="Type"
                :required="true"
                form-type="select"
                :options="typeOptions"
            />
            <b-row>
                <form-group
                    id="first-name"
                    v-model="form.firstName"
                    label="First Name"
                    placeholder="Enter first name"
                    :required="true"
                    class="col-lg-6 col-md-12"
                />
                <form-group
                    id="last-name"
                    v-model="form.lastName"
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
                v-model="form.contactNumber"
                form-type="tel"
                label="Contact Number"
                placeholder="Enter contact number (should be exactly 10 numbers long)"
                :required="true"
            />
            <h4>Address</h4>
            <form-group
                id="line-1"
                v-model="form.address.line1"
                label="Line 1"
                placeholder="Enter address line 1 (Street address)"
                :required="true"
            />
            <form-group
                id="line-2"
                v-model="form.address.line2"
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
                v-model="form.address.zipCode"
                label="Zip Code"
                placeholder="Enter zip code"
                type="number"
                :required="true"
                maxlength="4"
            />
            <b-button block type="submit" variant="primary">
                Register
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
    auth: "guest",
    data () {
        return {
            form: {
                username: "",
                password: "",
                firstName: "",
                lastName: "",
                email: "",
                contactNumber: "",
                profilePicture: null,
                type: "CS",
                address: {
                    line1: "",
                    line2: "",
                    barangay: "",
                    city: "",
                    province: "",
                    region: "",
                    zipCode: ""
                }
            },
            typeOptions: [
                {
                    value: "CS",
                    text: "Customer"
                },
                {
                    value: "OW",
                    text: "Owner"
                }
            ],
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
            // For some reason Nuxt attaches an Auth header for this
            // Django rest framework jwt doesn't like it
            this.$axios.setHeader("Authorization", "");
            await this.$axios.post("/api/auth/register", {
                username: this.form.username,
                password: this.form.password,
                email: this.form.email,
                contact_number: this.form.contactNumber,
                first_name: this.form.firstName,
                last_name: this.form.lastName,
                type: this.form.type,
                address: {
                    line_1: this.form.address.line1,
                    line_2: this.form.address.line2,
                    barangay: this.form.address.barangay,
                    city: this.form.address.city,
                    province: this.form.address.province,
                    region: this.form.address.region,
                    zip_code: this.form.address.zipCode
                }
            })
                .then((response) => {
                    this.$auth.loginWith("local", {
                        data: {
                            username: this.form.username,
                            password: this.form.password
                        }
                    })
                        .catch((err) => {
                            // eslint-disable-next-line no-console
                            console.log(err);
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
            $("#confirm-password")[0].setCustomValidity(
                $("#confirm-password")[0].value !== $("#password")[0].value ? "Passwords do not match" : ""
            );

            $("#password")[0].setCustomValidity(
                $("#password")[0].value.length < 6 ? "Password must be at least 6 characters long" : ""
            );

            $("#username")[0].setCustomValidity(
                $("#username")[0].value.match(/^[a-zA-Z0-9]+$/) ? "" : "Username must only have alphabetical and numerical characters"
            );

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
