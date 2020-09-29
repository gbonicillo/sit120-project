<template>
    <general-contents-container page-title="Register">
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
                    label="Confirm Password"
                    placeholder="Confirm Password"
                    type="password"
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
    middleware: "auth",
    auth: "guest",
    data () {
        return {
            form: {
                username: "",
                password: "",
                firstName: "",
                lastName: ""
            },
            error: null,
            validationErrors: null,
            otherError: ""

        };
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
                first_name: this.form.firstName,
                last_name: this.form.lastName
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
                    if (err.response.data.username) {
                        this.error = err.response.data.username;
                        $("#username")[0].setCustomValidity(this.error);
                    } else if (err.response.data.email) {
                        this.error = err.response.data.email;
                        $("#email")[0].setCustomValidity(this.error);
                    } else {
                        this.$toasted.global.defaultError({
                            msg: err.response.data.detail
                        });
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

</style>
