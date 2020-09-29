module.exports = {
    root: true,
    env: {
        browser: true,
        node: true,
        jquery: true
    },
    parserOptions: {
        parser: "babel-eslint"
    },
    extends: [
        "@nuxtjs",
        "plugin:nuxt/recommended"
    ],
    plugins: [
    ],
    // add your custom rules here
    rules: {
        semi: [
            "error",
            "always"
        ],
        quotes: [
            "error",
            "double",
            { allowTemplateLiterals: true }
        ],
        indent: [
            1,
            4
        ],
        "vue/html-indent": [
            1,
            4,
            { alignAttributesVertically: true }
        ],
        "vue/script-indent": [
            1,
            4
        ],
        "prefer-promise-reject-errors": "off"
    }
};
