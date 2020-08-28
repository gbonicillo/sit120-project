const { Sequelize } = require("sequelize");
const UserModel = require("./models/user");
const KarenderyaModel = require("./models/karenderya");
const MenuModel = require("./models/menu");
const MenuItemModel = require("./models/menuItem");
const OrderModel = require("./models/order");

const db = new Sequelize({
    dialect: "sqlite",
    storage: `${__dirname}/db/database.db`
});

const User = UserModel(db, Sequelize);
const Karenderya = KarenderyaModel(db, Sequelize);
const Menu = MenuModel(db, Sequelize);
const MenuItem = MenuItemModel(db, Sequelize);
const Order = OrderModel(db, Sequelize);

const MenuMenuItem = db.define("menu_menu_item", {});
const OrderItem = db.define("order_item", {});

Karenderya.belongsTo(User, {
    onDelete: "CASCADE"
});

Menu.belongsTo(Karenderya, {
    onDelete: "CASCADE",
    unique: false
});

MenuItem.belongsTo(Karenderya, {
    onDelete: "CASCADE",
    unique: false
});

MenuItem.belongsToMany(Menu, {
    through: MenuMenuItem
});

Menu.belongsToMany(MenuItem, {
    through: MenuMenuItem,
    as: {
        singular: "item",
        plural: "items"
    }
});

MenuItem.belongsToMany(Order, {
    through: OrderItem
});

Order.belongsToMany(MenuItem, {
    through: OrderItem,
    as: {
        singular: "item",
        plural: "items"
    }

});

Order.belongsTo(User);
Order.belongsTo(Karenderya);

db.sync({ force: true });

module.exports = {
    User,
    Karenderya,
    Menu,
    MenuItem,
    Order
};
