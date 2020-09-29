<template>
    <div>
        <b-card id="general-contents-container">
            <b-card-title>
                <b-row
                    align-v="center"
                >
                    <b-col sm="12" lg="8">
                        <page-header :page-title="pageTitle" />
                    </b-col>
                    <b-col sm="12" lg="4">
                        <slot name="header-extra" />
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
    padding: 20px;
    height: auto;
    min-height: 100vh;
}
</style>
