<template>
  <b-navbar toggleable="md" type="dark" variant="dark">
    <b-navbar-toggle target="nav_collapse" />
    <b-navbar-brand to="/">
      OK
    </b-navbar-brand>
    <b-collapse id="nav_collapse" is-nav>
      <b-navbar-nav v-if="!this.$auth.loggedIn" />
      <b-navbar-nav v-else-if="this.$auth.user.type=='customer'">
        <b-nav-item to="/">
          Home
        </b-nav-item>
        <b-nav-item to="/karenderyas">
          Karenderyas
        </b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav v-else-if="this.$auth.user.type=='karenderya'">
        <b-nav-item to="/">
          Home
        </b-nav-item>
        <b-nav-item to="/orders">
          Pending Orders
        </b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-item-dropdown v-if="!$auth.loggedIn" text="Demo" right>
          <b-dropdown-item href="#" @click.prevent="login('karenderya')">
            Karenderya
          </b-dropdown-item>
          <b-dropdown-item href="#" @click.prevent="login('customer')">
            Customer
          </b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown v-else text="User" right>
          <b-dropdown-item v-if="this.$auth.user.type=='customer'" href="#" @click.prevent="login('karenderya')">
            Switch to Karenderya
          </b-dropdown-item>
          <b-dropdown-item v-else-if="this.$auth.user.type=='karenderya'" href="#" @click.prevent="login('customer')">
            Switch to Customer
          </b-dropdown-item>
          <b-link to="/logout" class="dropdown-item">
            Signout
          </b-link>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>
