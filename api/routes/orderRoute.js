const { Router } = require("express");
const orderController = require("../controllers/orderController");

const router = Router();

router.post("/orders/create", orderController.create);
router.get("/orders/", orderController.orders);
router.get("/orders/:id", orderController.order);

module.exports = router;
