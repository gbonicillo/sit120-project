<template>
    <b-navbar toggleable="md" type="dark" variant="dark">
        <b-navbar-toggle target="nav_collapse" />
        <b-navbar-brand to="/">
            Online Karenderya
        </b-navbar-brand>

        <b-collapse id="nav_collapse" is-nav>
            <b-navbar-nav>
                <b-nav-item
                    v-for="(item, key) of this.$auth.loggedIn ? authenticatedItems : globalItems"
                    :key="key"
                    :to="item.to"
                >
                    {{ item.title }}
                </b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
                <b-nav-item-dropdown
                    v-if="this.$auth.loggedIn"
                    :text="this.$auth.user.username"
                    right
                >
                    <b-dropdown-item
                        v-for="(item, key) of rightNavAuthenticatedItems"
                        :key="key"
                    >
                        <b-link :to="item.to">
                            {{ item.title }}
                        </b-link>
                    </b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    data () {
        return {
            searchTerm: "",
            globalItems: [
                {
                    title: "Home",
                    to: {
                        name: "index"
                    }
                }
            ],
            authenticatedItems: [],
            rightNavAuthenticatedItems: [
                {
                    title: "Profile",
                    to: {
                        name: "user"
                    }
                },
                {
                    title: "Update Info",
                    to: {
                        name: "user-update",
                        path: "/user/update"
                    }
                },
                {
                    title: "Change Password",
                    to: {
                        name: "user-change-password",
                        path: "/user/change-password"
                    }
                },
                {
                    title: "Logout",
                    to: {
                        name: "logout"
                    }
                }
            ]
        };
    }
};
</script>

<style lang="scss" scoped>
.navbar-profile-picture{
    height: 30px;
    width: 30px;
}
</style>
