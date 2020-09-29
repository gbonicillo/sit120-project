export default function ({ store, error }) {
    if (!store.state.auth.user.is_staff) {
        return error({
            statusCode: 401,
            message: "User is does not have the authorization to access this page"
        });
    }
}
