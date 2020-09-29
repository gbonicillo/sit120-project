<template>
    <div id="globalContainer">
        <b-card id="loginForm">
            <b-card-title class="text-center">
                Login
            </b-card-title>
            <b-card-body>
                <b-form @submit.prevent="onSubmit">
                    <form-group
                        id="username"
                        v-model="form.username"
                        label="Username"
                        placeholder="Enter Username"
                        :required="true"
                    />
                    <form-group
                        id="password"
                        v-model="form.password"
                        label="Password"
                        placeholder="Enter password"
                        type="password"
                        :required="true"
                    />
                    <b-button block type="submit" variant="primary">
                        Login
                    </b-button>

                    <div id="signUp">
                        Not yet registered? <n-link to="/register/">
                            Register here
                        </n-link>
                    </div>
                </b-form>
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
import FormGroup from "../components/FormGroup";

export default {
    components: {
        FormGroup
    },
    middlware: "auth",
    auth: "guest",
    data () {
        return {
            form: {
                username: "",
                password: ""
            },
            error: ""
        };
    },
    methods: {
        onSubmit () {
            this.$auth.loginWith("local", {
                data: {
                    username: this.form.username,
                    password: this.form.password
                }
            })
                .catch((err) => {
                    if (err.response.data.detail) {
                        this.error = err.response.data.detail;
                        this.$toasted.global.defaultError({
                            msg: this.error
                        });
                    }
                });
        }
    }
};
</script>

<style lang="scss" scoped>
#loginForm{
    width: 330px;
    margin: 20px;
}

#globalContainer{
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

#signUp{
    text-align: center;
    padding: 20px 0 0;
}

#errorMessage{
    text-align: center;
    padding: 0 0 5px 0;
}
</style>
