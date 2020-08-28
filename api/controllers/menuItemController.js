const db = require("../db");

module.exports.create = (req, res) => {
    db.MenuItem.create({
        name: req.body.name,
        price: req.body.price
    })
        .then((menuItem) => {
            menuItem.setKarenderya(req.body.karenderyaId);
            res.json(menuItem);
        })
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.menuItems = (req, res) => {
    db.MenuItem.findAll({
        include: db.Karenderya
    }).then(menuItems => res.json(menuItems))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.menuItem = (req, res) => {
    db.MenuItem.findOne({
        where: {
            id: req.params.id
        },
        include: db.Karenderya
    })
        .then(menuItem => res.json(menuItem))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};
