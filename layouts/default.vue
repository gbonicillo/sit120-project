<template>
    <div>
        <navbar />
        <b-container class="p-1">
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
