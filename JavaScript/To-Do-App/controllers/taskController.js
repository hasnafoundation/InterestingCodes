var task = require('../models/task');
var async = require('async');

exports.task_list = function(req,res,next){
    async.parallel({
        task
    })
    
    res.send("task list");
}

exports.task_create_get = function(req,res){
    res.send("Create task GET");
}

exports.task_create_post = function(req, res){
    res.send("Create task POST");
}

exports.task_delete_post = function(req,res){
    res.send("delete task POST");
}

exports.task_delete_get = function(req, res){
    res.send("delete task GET")
} 

exports.task_update_get = function(req, res){
    res.send("update task GET");
}

exports.task_update_post = function(req, res){
    res.send("update task POST")
}