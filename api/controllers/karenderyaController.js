const db = require("../db");

module.exports.create = (req, res) => {
    db.Karenderya.create({
        name: req.body.name,
        street: req.body.street,
        barangay: req.body.barangay,
        city: req.body.city,
        province: req.body.province
    })
        .then((karenderya) => {
            karenderya.setUser(req.body.userId);

            return res.json(karenderya);
        })
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.karenderyas = (req, res) => {
    db.Karenderya.findAll({
        include: db.User
    }).then(karenderyas => res.json(karenderyas))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.karenderya = (req, res) => {
    db.Karenderya.findOne({
        where: {
            id: req.params.id
        },
        include: db.User
    })
        .then(karenderya => res.json(karenderya))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};
