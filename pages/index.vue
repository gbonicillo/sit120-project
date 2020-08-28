<template>
    <div>
        <b-jumbotron header="Welcome!" :lead="greeting">
            <p>You are of user type {{ $auth.user.type }}</p>
        </b-jumbotron>
    </div>
</template>

<script>
export default {
    middleware: "auth",
    data () {
        return {
            greeting: `Good day to you ${this.$auth.user.name}`
        };
    }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
</style>
