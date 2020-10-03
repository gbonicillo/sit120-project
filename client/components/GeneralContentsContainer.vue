<template>
    <div>
        <b-card id="general-contents-container">
            <b-card-title
                v-if="pageTitle.length > 0"
            >
                <b-row
                    align-v="center"
                >
                    <b-col>
                        <page-header :page-title="pageTitle" />
                    </b-col>
                </b-row>
            </b-card-title>
            <b-card-body>
                <slot />
            </b-card-body>
        </b-card>
    </div>
</template>

<script>
import PageHeader from "@/components/PageHeader";

export default {
    components: {
        PageHeader
    },
    props: {
        pageTitle: {
            type: String,
            default: ""
        }
    },
    computed: {
        hasHeaderExtra () {
            return !!this.$slots.headerExtra;
        }
    }
};
</script>

<style lang="scss" scoped>
#general-contents-container{
    padding: 10px;
    height: auto;
    min-height: 100vh;
}
</style>
