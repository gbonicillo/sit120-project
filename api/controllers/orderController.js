// const config = require("../config");
// const jwt = require("jsonwebtoken");
// const bcrypt = require("bcryptjs");
const db = require("../db");

module.exports.create = (req, res) => {
    db.Order.create()
        .then((order) => {
            order.setKarenderya(req.body.karenderyaId);
            order.setUser(req.body.userId);
            order.addItems(req.body.items);

            return res.json(order);
        }).catch((err) => {
            return res.status(500).json({
                message: "Server Error: " + err.message
            });
        });
};

module.exports.orders = (req, res) => {
    db.Order.findAll({
        include: [
            db.User,
            db.Karenderya,
            {
                model: db.MenuItem,
                as: "items"
            }
        ]
    }).then(orders => res.json(orders))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.order = (req, res) => {
    db.Order.findOne({
        where: {
            id: req.params.id
        },
        include: [
            db.User,
            db.Karenderya,
            {
                model: db.MenuItem,
                as: "items"
            }
        ]
    })
        .then(order => res.json(order))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};
