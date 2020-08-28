const bcrypt = require("bcryptjs");
const validator = require("express-validator");
const jwt = require("jsonwebtoken");
const db = require("../db");
const config = require("../config");
const { User } = require("../db");

module.exports.create = [
    validator.body("email").custom((value) => {
        return db.User.findOne({
            where: {
                email: value
            }
        })
            .then((user) => {
                if (user) {
                    return Promise.reject("Email already in use");
                }
            });
    }),
    validator.body("username").custom((value) => {
        return db.User.findOne({
            where: {
                username: value
            }
        })
            .then((user) => {
                if (user) {
                    return Promise.reject("Username already in use");
                }
            });
    }),
    (req, res) => {
        const errors = validator.validationResult(req);
        if (!errors.isEmpty()) {
            return res.status(422).json({ validationErrors: errors.mapped() });
        }
        db.User.create({
            firstName: req.body.firstName,
            lastName: req.body.lastname,
            street: req.body.street,
            barangay: req.body.barangay,
            city: req.body.city,
            province: req.body.province,
            username: req.body.username,
            email: req.body.email,
            password: req.body.password,
            type: req.body.type
        })
            .then((user) => {
                const salt = bcrypt.genSaltSync(10);
                const hash = bcrypt.hashSync(user.password, salt);

                user.password = hash;
                user.save();

                res.json(user);
            })
            .catch((err) => {
                return res.status(500).json({ message: "Server Error: " + err.message });
            });
    }
];

module.exports.login = (req, res) => {
    User.findOne({
        where: {
            username: req.body.username
        }
    })
        .then((user) => {
            if (user === null) {
                return res.status(500).json({
                    message: "Invalid username or password"
                });
            }

            return bcrypt.compare(req.body.password, user.password, (err, isMatched) => {
                if (err) {
                    return res.status(500).json({
                        message: "Error loggin in"
                    });
                }

                if (isMatched) {
                    return res.json({
                        user: {
                            id: user.id,
                            username: user.username,
                            name: user.firstName,
                            type: user.type
                        },
                        token: jwt.sign({
                            id: user.id,
                            username: user.username,
                            name: user.firstName,
                            type: user.type
                        }, config.authSecret)
                    });
                } else {
                    return res.status(500).json({
                        message: "Invalid username or password"
                    });
                }
            });
        })
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.users = (req, res) => {
    db.User.findAll().then(users => res.json(users))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.profile = (req, res) => {
    db.User.findOne({
        where: {
            id: req.params.id
        }
    })
        .then(user => res.json(user))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.user = (req, res) => {
    const token = req.headers.authorization;
    if (token) {
        jwt.verify(token.replace(/^Bearer\s/, ""), config.authSecret, function (err, decoded) {
            if (err) {
                return res.status(401).json({ message: "unauthorized" });
            } else {
                return res.json({ user: decoded });
            }
        });
    } else {
        return res.status(401).json({ message: "unauthorized" });
    }
};
