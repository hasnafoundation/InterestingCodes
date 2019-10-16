var mongoose = require('mongoose');

var Schema = mongoose.Schema;

var taskSchema = new Schema(
    {
        task: {type: String, required: true},
        time: {type: Date},
    }
);


taskSchema
.virtual('url')
.get(function(){
    return '/task/'+this._id;
});

module.exports = mongoose.model('to_do',taskSchema);