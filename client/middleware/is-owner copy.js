export default function ({ store, error }) {
    if (!store.state.auth.user.type === "OW") {
        return error({
            statusCode: 401,
            message: "User does not have the authorization to access this page"
        });
    }
}
