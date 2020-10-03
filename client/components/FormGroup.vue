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
        <b-input-group
            v-if="formType === 'tel'"
            prepend="+63"
        >
            <b-form-input
                :id="id"
                v-model="dataModel"
                type="tel"
                :required="required ? true : false"
                :placeholder="placeholder"
                pattern="9[0-9]{9}"
            />
        </b-input-group>
        <b-input-group
            v-if="formType === 'price'"
            prepend="₱"
        >
            <b-form-input
                :id="id"
                v-model="dataModel"
                type="number"
                :required="required ? true : false"
                :placeholder="placeholder"
                step="0.01"
            />
        </b-input-group>
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
@import '@/assets/theme-colors.scss';

.input-area {
    height: 150px
}

</style>
