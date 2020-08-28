const user = (db, type) => {
    return db.define("user", {
        id: {
            type: type.INTEGER,
            primaryKey: true,
            autoIncrement: true
        },
        firstName: {
            type: type.STRING
        },
        lastName: {
            type: type.STRING
        },
        contact: {
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
        },
        username: {
            type: type.STRING
        },
        email: {
            type: type.STRING
        },
        password: {
            type: type.STRING
        },
        type: {
            type: type.STRING
        }
    });
};

module.exports = user;
