<template>
    <div id="main-container">
        <navbar />
        <b-container id="contents" class="p-1">
            <Nuxt />
        </b-container>
    </div>
</template>

<script>
import Navbar from "../components/Navbar";

export default {
    components: {
        Navbar
    }
};
</script>

<style lang="scss">

//Color theme
@import '@/assets/theme-colors.scss';

//Bootstrap files
@import '@/node_modules/bootstrap/scss/bootstrap';
@import '@/node_modules/bootstrap-vue/src/index.scss';

html{
    height: 100%;
}

body {
    // background-color: ;
    height: 100%;
}

#main-container {
    height: auto !important;
    min-height: 100vh;
}

// #contents {
//     background-color: #f9f5d7;
//     padding: 20px 20px;
//     min-height: 100%
// }

#__nuxt{
    position: relative;
    min-height: 100%;
    #__layout{
        height: auto !important;
        min-height: 100vh;
    }
}

.dropdown-item:hover, .dropdown-item:focus {
    text-decoration: none;
    background-color: #f2e5bc;
}

.form-control, .custom-select {
    border-color: var(--dark);
}

</style>
