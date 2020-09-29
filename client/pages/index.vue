<template>
    <general-contents-container>
        <b-row>
            <b-jumbotron
                class="w-100"
                :header="`Welcome ${userTypeText}`"
                lead="The site for checking reported issues and recalls for cars!"
                bg-variant="dark"
                text-variant="light"
            >
                <p>
                    Try searching report for your car by typing your car's make
                    and/or model in the search bar
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
