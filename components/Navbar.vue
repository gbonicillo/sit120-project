<template>
    <b-navbar toggleable="md" type="dark" variant="dark">
        <b-navbar-toggle target="nav_collapse" />
        <b-navbar-brand to="/">
            OK
        </b-navbar-brand>
        <b-collapse id="nav_collapse" is-nav>
            <b-navbar-nav v-if="$auth.loggedIn && $auth.user.type=='karenderya'">
                <b-nav-item to="/">
                    Home
                </b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
                <b-nav-item v-if="!$auth.loggedIn" to="/register">
                    Register
                </b-nav-item>
                <b-nav-item v-else to="/logout">
                    Logout
                </b-nav-item>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>
