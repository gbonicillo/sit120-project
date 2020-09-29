<template>
    <div>
        <b-row>
            <b-col>
                <b-button
                    v-if="$auth.user.is_staff"
                    variant="danger"
                    class="float-lg-right m-2"
                    @click="deleteFunction"
                >
                    Delete
                </b-button>
            </b-col>
            <b-col>
                <b-button
                    v-if="$auth.user.is_staff"
                    variant="primary"
                    class="float-sm-right float-lg-left m-2"
                    :to="updateTo"
                >
                    Update
                </b-button>
            </b-col>
        </b-row>
    </div>
</template>

<script>
export default {
    props: {
        updateTo: {
            type: String,
            default: ""
        },
        deleteFunction: {
            type: Function,
            default: null
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
