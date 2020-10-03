<template>
    <general-contents-container>
        <b-row>
            <b-jumbotron
                class="w-100"
                :header="`Welcome ${userTypeText}`"
                lead="The site for ordering from your favorite karenderyas online!"
                bg-variant="primary"
                text-variant="light"
            >
                <p>
                    This site is still under construction
                </p>
            </b-jumbotron>
        </b-row>
    </general-contents-container>
</template>

<script>
export default {
    computed: {
        userTypeText () {
            let userTypeText = "";

            switch (this.$auth.user.type) {
            case "CS":
                userTypeText = "Customer";
                break;
            case "OW":
                userTypeText = "Owner";
                break;
            default:
                userTypeText = "User";
            }
            return userTypeText;
        }
    }
};
</script>
