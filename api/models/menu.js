let menu = (db, type) => {
    return db.define("menu", {
        id: {
            type: type.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: type.STRING
        },
    });
};

module.exports = menu;