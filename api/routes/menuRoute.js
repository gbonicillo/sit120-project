const { Router } = require("express");
const menuController = require("../controllers/menuController");

const router = Router();

router.post("/menus/create", menuController.create);
router.get("/menus/", menuController.menus);
router.get("/menus/:id", menuController.menu);

module.exports = router;
