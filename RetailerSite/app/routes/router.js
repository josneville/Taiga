/**
 * Main route function to expose backend endpoints
 * @param app
 */
var Email = require('./email')

module.exports = function(app){
	app.get('/api/email', Email.send)
};