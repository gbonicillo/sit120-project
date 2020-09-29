
export default {
    /*
  ** Nuxt rendering mode
  ** See https://nuxtjs.org/api/configuration-mode
  */
    mode: "universal",
    /*
  ** Nuxt target
  ** See https://nuxtjs.org/api/configuration-target
  */
    target: "server",
    /*
  ** Headers of the page
  ** See https://nuxtjs.org/api/configuration-head
  */
    head: {
        title: "Check Your Car",
        meta: [
            { charset: "utf-8" },
            { name: "viewport", content: "width=device-width, initial-scale=1" },
            { hid: "description", name: "description", content: process.env.npm_package_description || "" }
        ],
        link: [
            { rel: "icon", type: "image/x-icon", href: "/favicon.ico" }
        ],
        script: [
            {
                src: "https://code.jquery.com/jquery-3.5.1.min.js"
            }
        ]
    },
    /*
  ** Global CSS
  */
    css: [
    ],
    /*
  ** Plugins to load before mounting the App
  ** https://nuxtjs.org/guide/plugins
  */
    plugins: [
    ],
    /*
  ** Auto import components
  ** See https://nuxtjs.org/api/configuration-components
  */
    components: true,
    /*
  ** Nuxt.js dev-modules
  */
    buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
        "@nuxtjs/eslint-module"
    ],
    /*
  ** Nuxt.js modules
  */
    modules: [
    // Doc: https://bootstrap-vue.js.org
        "bootstrap-vue/nuxt",
        // Doc: https://axios.nuxtjs.org/usage
        "@nuxtjs/axios",
        "@nuxtjs/auth",
        "@nuxtjs/toast"
    ],
    /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
    axios: {
        baseURL: "http://localhost:8000/"
    },
    /*
  ** Build configuration
  ** See https://nuxtjs.org/api/configuration-build/
  */
    build: {
    },

    auth: {
        strategies: {
            local: {
                endpoints: {
                    login: {
                        url: "/api/auth/token",
                        method: "post",
                        propertyName: "access",
                        altProperty: "refresh"
                    },
                    logout: true,
                    user: {
                        url: "/api/auth/user",
                        method: "get",
                        propertyName: "user"
                    }
                }
            }
        },
        redirect: {
            login: "/login"
        }
    },
    router: {
        middleware: [
            "auth"
        ]
    },
    toast: {
        position: "top-center",
        iconPack: "fontawesome",
        duration: 3000,
        register: [
            {
                name: "defaultSuccess",
                message: payload =>
                    !payload.msg ? "Operation Success" : payload.msg,
                options: {
                    type: "success",
                    icon: "check"
                }
            },
            {
                name: "defaultError",
                message: payload =>
                    !payload.msg ? "Oops... Something went wrong" : payload.msg,
                options: {
                    type: "error",
                    icon: "times"
                }
            }
        ]
    },
    env: {
        paginationItemsPerPage: 10
    }
};
