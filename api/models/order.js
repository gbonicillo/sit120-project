const order = (db, type) => {
    return db.define("order", {
        id: {
            type: type.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        status: {
            type: type.STRING,
            defaultValue: "pending"
        }
    });
};

module.exports = order;
