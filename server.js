var express = require('express');
var path = require('path');
var app = new express();

app.use(express.static(__dirname))
app.use('*',function(req,res){
  res.sendFile(path.resolve(__dirname,'build/index.html'))
})
app.listen(8090);
console.log('app is running at port 8090')
