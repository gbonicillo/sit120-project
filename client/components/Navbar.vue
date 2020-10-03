<template>
    <b-navbar id="main-nav" toggleable="md" type="dark" variant="primary">
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
                <!--Short-circuit conditional -->
                <b-nav-item
                    v-for="
                        (item, key) of this.$auth.loggedIn && this.$auth.user.type === 'OW' ? ownerItems : []
                    "
                    :key="key"
                    :to="item.to"
                >
                    {{ item.title }}
                </b-nav-item>
                <b-nav-item
                    v-for="
                        (item, key) of this.$auth.loggedIn && this.$auth.user.type === 'CS' ? customerItems : []
                    "
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
                        :to="item.to"
                    >
                        {{ item.title }}
                    </b-dropdown-item>
                </b-nav-item-dropdown>
                <b-nav-item
                    v-for="(item, key) of rightGuestItems"
                    v-else
                    :key="key"
                    :to="item.to"
                >
                    {{ item.title }}
                </b-nav-item>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
    data () {
        return {
            searchTerm: "",
            emptyItems: [],
            globalItems: [
            ],
            authenticatedItems: [
                {
                    title: "Home",
                    to: {
                        name: "index"
                    }
                }
            ],
            ownerItems: [
                {
                    title: "My Karenderya",
                    to: {
                        name: "my-karenderya"
                    }
                },
                {
                    title: "All Orders",
                    to: {
                        path: "/my-karenderya/orders"
                    }
                },
                {
                    title: "Accepted Orders",
                    to: {
                        path: "/my-karenderya/orders/accepted"
                    }
                },
                {
                    title: "Rejected Orders",
                    to: {
                        path: "/my-karenderya/orders/rejected"
                    }
                },
                {
                    title: "Pending Orders",
                    to: {
                        path: "/my-karenderya/orders/pending"
                    }
                }
            ],
            customerItems: [
                {
                    title: "Karenderyas",
                    to: {
                        name: "karenderyas"
                    }
                },
                {
                    title: "My Orders",
                    to: {
                        name: "my-orders"
                    }
                }
            ],
            rightGuestItems: [
                {
                    title: "Login",
                    to: {
                        name: "login"
                    }
                }
            ],
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
                    title: "Change Profile Picture",
                    to: {
                        name: "user-change-profile-picture",
                        path: "/user/change-profile-picture"
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
