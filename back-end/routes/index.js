var express = require('express');
var router = express.Router();
const multer=require("multer");
const fileUpload=multer();
let {PythonShell}=require("python-shell")
 
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});


module.exports = router;
