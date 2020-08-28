let karenderya = (db, type) => {
    return db.define("karenderya", {
        id: {
            type: type.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        name: {
            type: type.STRING
        },
        street: {
            type: type.STRING
        },
        barangay: {
            type: type.STRING
        },
        city: {
            type: type.STRING
        },
        province: {
            type: type.STRING
        }
    });
};

module.exports = karenderya;