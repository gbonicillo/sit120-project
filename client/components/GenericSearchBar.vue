<template>
    <b-input-group>
        <b-form-input
            v-model="dataModel"
            :placeholder="placeholder"
            @keyup.enter="$emit('search')"
        />
        <b-input-group-append>
            <b-button
                variant="primary"
                @click="$emit('search')"
            >
                Search
            </b-button>
        </b-input-group-append>
    </b-input-group>
</template>

<script>
export default {
    props: {
        value: {
            type: String,
            default: null
        },
        onSearch: {
            type: Function,
            default: null
        },
        placeholder: {
            type: String,
            default: "Search here..."
        }
    },
    computed: {
        dataModel: {
            get () {
                return this.value;
            },
            set (val) {
                this.$emit("input", val);
            }
        }
    }
};
</script>

<style lang="scss" scoped>

</style>
