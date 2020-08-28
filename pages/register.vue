<template>
    <b-card id="registerCard">
        <b-card-title>
            <page-header page-title="Register" />
        </b-card-title>
        <b-card-body>
            <b-form
                @submit.prevent="onSubmit"
                @input="onInput"
            >
                <form-group
                    id="username"
                    v-model="form.username"
                    label="Username"
                    placeholder="Enter Username"
                    :required="true"
                />
                <b-row>
                    <form-group
                        id="password"
                        v-model="form.password"
                        label="Password"
                        placeholder="Enter password"
                        type="password"
                        :required="true"
                        class="col-lg-6 col-md-12"
                    />
                    <form-group
                        id="confirmPassword"
                        v-model="form.password"
                        label="Confirm Password"
                        placeholder="Confirm Password"
                        ype="password"
                        :required="true"
                        class="col-lg-6 col-md-12"
                    />
                </b-row>
                <form-group
                    id="email"
                    v-model="form.email"
                    label="Email"
                    placeholder="Enter email"
                    type="email"
                    :required="true"
                />
                <form-group
                    id="type"
                    v-model="form.type"
                    label="User Type"
                    :required="true"
                    form-type="select"
                    :options="types"
                />

                <b-row>
                    <form-group
                        id="firstName"
                        v-model="form.firstName"
                        label="First Name"
                        placeholder="Enter first name"
                        :required="true"
                        class="col-lg-6 col-md-12"
                    />
                    <form-group
                        id="lastName"
                        v-model="form.lastName"
                        label="Last Name"
                        placeholder="Enter last name"
                        :required="true"
                        class="col-lg-6 col-md-12"
                    />
                </b-row>
                <form-group
                    id="street"
                    v-model="form.street"
                    label="Street Address"
                    placeholder="Enter street address"
                    :required="true"
                />
                <b-row>
                    <form-group
                        id="barangay"
                        v-model="form.barangay"
                        label="Barangay"
                        placeholder="Enter barangay"
                        :required="true"
                        class="col-lg-4 col-md-12"
                    />
                    <form-group
                        id="city"
                        v-model="form.city"
                        label="City"
                        placeholder="Enter city"
                        :required="true"
                        class="col-lg-4 col-md-12"
                    />
                    <form-group
                        id="province"
                        v-model="form.province"
                        label="Province"
                        placeholder="Enter province"
                        :required="true"
                        class="col-lg-4 col-md-12"
                    />
                </b-row>
                <b-button block type="submit" variant="primary">
                    Register
                </b-button>
            </b-form>
        </b-card-body>
    </b-card>
</template>

<script>
import PageHeader from "../components/PageHeader";
import FormGroup from "../components/FormGroup";

export default {
    components: {
        PageHeader,
        FormGroup
    },
    middleware: "auth",
    auth: "guest",
    data () {
        return {
            form: {
                username: "",
                password: "",
                firstName: "",
                lastName: "",
                street: "",
                barangay: "",
                city: "",
                province: "",
                type: null
            },
            types: [
                "customer",
                "owner"
            ],
            error: null,
            validationErrors: null,
            otherError: ""

        };
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.post("/api/register/", {
                username: this.form.username,
                password: this.form.password,
                email: this.form.email,
                type: this.form.type,
                firstName: this.form.firstName,
                lastName: this.form.lastName,
                street: this.form.street,
                barangay: this.form.barangay,
                city: this.form.city,
                province: this.form.province

            })
                .then((response) => {
                    if (response.data.id) {
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
                    }
                })
                .catch((err) => {
                    if (err.response.data.message) {
                        this.error = err.response.data.message;
                    } else if (err.response.data.validationErrors) {
                        this.validationErrors = err.response.data.validationErrors;
                        if (this.validationErrors.email) {
                            $("#email")[0].setCustomValidity(this.validationErrors.email.msg);
                        }

                        if (this.validationErrors.username) {
                            $("#username")[0].setCustomValidity(this.validationErrors.username.msg);
                        }
                    }
                });
        },

        onInput (evt) {
            $("#confirmPassword")[0].setCustomValidity(
                $("#confirmPassword")[0].value !== $("#password")[0].value ? "Passwords do not match" : ""
            );

            $("#password")[0].setCustomValidity(
                $("#password")[0].value.length < 6 ? "Password must be at least 6 characters long" : ""
            );

            $("#username")[0].setCustomValidity(
                $("#username")[0].value.match(/^[a-zA-Z0-9]+$/) ? "" : "Username must only have alphabetical and numerical characters"
            );
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
#registerCard{
    padding: 20px;
}
</style>
