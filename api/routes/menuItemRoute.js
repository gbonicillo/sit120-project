const { Router } = require("express");
const menuItemController = require("../controllers/menuItemController");

const router = Router();

router.post("/menuItems/create", menuItemController.create);
router.get("/menuItems/", menuItemController.menuItems);
router.get("/menuItems/:id", menuItemController.menuItem);

module.exports = router;
