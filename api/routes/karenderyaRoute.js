const { Router } = require("express");
const karenderyaController = require("../controllers/karenderyaController");

const router = Router();

router.post("/karenderyas/create", karenderyaController.create);
router.get("/karenderyas/", karenderyaController.karenderyas);
router.get("/karenderyas/:id", karenderyaController.karenderya);

module.exports = router;
