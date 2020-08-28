const db = require("../db");

module.exports.create = (req, res) => {
    db.Menu.create({
        name: req.body.name
    })
        .then((menu) => {
            menu.setKarenderya(req.body.karenderyaId);
            menu.addItems(req.body.oldItems);

            req.body.newItems.forEach((item) => {
                db.MenuItem.create({
                    name: item.name,
                    price: item.price
                }).then((menuItem) => {
                    menuItem.setKarenderya(req.body.karenderyaId);
                    menu.addItem(menuItem);
                });
            });

            return res.json(menu);
        }).catch((err) => {
            return res.status(500).json({
                message: "Server Error: " + err.message,
                oldItems: req.body.oldItems,
                newItems: req.body.newItems
            });
        });
};

module.exports.menus = (req, res) => {
    db.Menu.findAll({
        include: [
            db.Karenderya,
            {
                model: db.MenuItem,
                as: "items"
            }
        ]
    }).then(menus => res.json(menus))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};

module.exports.menu = (req, res) => {
    db.Menu.findOne({
        where: {
            id: req.params.id
        },
        include: [
            db.Karenderya,
            {
                model: db.MenuItem,
                as: "items"
            }
        ]
    })
        .then(menu => res.json(menu))
        .catch((err) => {
            return res.status(500).json({ message: "Server Error: " + err.message });
        });
};
