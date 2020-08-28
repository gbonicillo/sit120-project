const { Router } = require("express");
const userController = require("../controllers/userController");

const router = Router();

router.post("/register/", userController.create);
router.post("/login/", userController.login);
router.get("/users/", userController.users);
router.get("/users/:id", userController.profile);
router.get("/user", userController.user);

module.exports = router;
