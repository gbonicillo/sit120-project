const jwt = require("jsonwebtoken");

const config = {
    authSecret: "jdkslqwem;zojrjqww2mvazajui232jal"
};

module.exports = config;

module.exports.isAuthenticated = function (req, res, next) {
    const token = req.headers.authentication;
    if (token) {
        jwt.verify(
            token.replace(/^Bearer\s/, ""),
            config.authSecret,
            (err, decoded) => {
                if (err) {
                    return res.status(401).json({ message: "unauthorized" });
                } else {
                    return next;
                }
            });
    } else {
        return res.status(401).json({ message: "unauthorized" });
    }
};
