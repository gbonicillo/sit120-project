const express = require("express");

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const user = require("./routes/userRoute");
const karenderya = require("./routes/karenderyaRoute");
const menuItem = require("./routes/menuItemRoute");
const menu = require("./routes/menuRoute");
const order = require("./routes/orderRoute");

app.use(user);
app.use(karenderya);
app.use(menuItem);
app.use(menu);
app.use(order);

module.exports = {
    path: "/api",
    handler: app
};
