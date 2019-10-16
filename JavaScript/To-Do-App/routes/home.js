var express = require('express');
var router = express.Router();

//Requires task controller
var task_controller = require('../controllers/taskController');


router.get('/', task_controller.task_list);

router.get('/task/create', task_controller.task_create_get);

router.post('/task/create', task_controller.task_create_post);

router.get('/task/:id/update', task_controller.task_update_get);

router.post('/task/:id/update', task_controller.task_update_post);

router.get('/task/:id/delete', task_controller.task_delete_get);

router.post('/task/:id/delete', task_controller.task_delete_post);

module.exports = router;