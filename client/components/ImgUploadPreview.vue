<template>
    <div>
        <b-img
            id="profile-picture-preview"
            thumbnail
            :src="imgUrl"
            @click="onClick"
        />
        <b-form-file
            id="profile-picture"
            v-model="dataModel"
            style="display: none"
            accept="image/jpeg, image/png"
        />
    </div>
</template>

<script>
export default {
    props: {
        imageUrl: {
            type: String,
            default: "https://via.placeholder.com/250"
        },
        onClick: {
            type: Function,
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

</style>
