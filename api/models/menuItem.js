const menuItem = (db, type) => {
    return db.define("menu_item", {
        id: {
            type: type.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: type.STRING
        },
        price: {
            type: type.FLOAT
        }
    });
};

module.exports = menuItem;
