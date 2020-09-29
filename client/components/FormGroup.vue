<template>
    <b-form-group
        :label="label"
        :label-for="id"
    >
        <b-form-input
            v-if="formType === 'text'"
            :id="id"
            v-model="dataModel"
            :type="type"
            :required="required ? true : false"
            :placeholder="placeholder"
        />
        <b-form-select
            v-if="formType === 'select'"
            :id="id"
            v-model="dataModel"
            :required="required ? true : false"
            :options="options"
        />
        <b-form-textarea
            v-if="formType === 'textarea'"
            :id="id"
            v-model="dataModel"
            class="input-area"
            :type="type"
            :required="required ? true : false"
            :placeholder="placeholder"
        />
    </b-form-group>
</template>

<script>
export default {
    props: {
        id: {
            type: String,
            default: "id"
        },
        formType: {
            type: String,
            default: "text"
        },
        label: {
            type: String,
            default: "label"
        },
        type: {
            type: String,
            default: "text"
        },
        placeholder: {
            type: String,
            default: "placeholder"
        },
        required: {
            type: Boolean,
            default: false
        },
        options: {
            type: Array,
            default: () => []
        },
        value: {
            type: [Number, String],
            default: null
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

.input-area {
    height: 150px
}

</style>
