<template>
    <general-contents-container page-title="Change Password">
        <b-form
            @submit.prevent="onSubmit"
            @input="onInput"
        >
            <b-row>
                <form-group
                    id="old-password"
                    v-model="form.oldPassword"
                    label="Old Password"
                    placeholder="Enter password"
                    type="password"
                    :required="true"
                    class="col-12"
                />
            </b-row>
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
                    type="password"
                    :required="true"
                    class="col-lg-6 col-md-12"
                />
            </b-row>
            <b-button block type="submit" variant="primary">
                Change Password
            </b-button>
        </b-form>
    </general-contents-container>
</template>

<script>
import FormGroup from "@/components/FormGroup";
import GeneralContentsContainer from "@/components/GeneralContentsContainer";

export default {
    components: {
        FormGroup,
        GeneralContentsContainer
    },
    middleware: "auth",
    data () {
        return {
            form: {
                oldPassword: "",
                password: ""
            },
            error: null,
            validationErrors: null,
            otherError: ""

        };
    },
    methods: {
        async onSubmit (evt) {
            await this.$axios.put(`/api/auth/user/change-password/${this.$auth.user.id}`, {
                old_password: this.form.oldPassword,
                new_password: this.form.password
            })
                .then((response) => {
                    if (response.status === 200) {
                        this.$router.push({
                            path: `/user/`
                        });
                    }
                })
                .catch((err) => {
                    if (err.response.data.old_password) {
                        this.error = err.response.data.old_password;
                        $("#old-password")[0].setCustomValidity(this.error);
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
        }
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>

</style>
