
(function() {
	var app = angular.module('taiga', ['ngRoute']);

	app.config(function($routeProvider, $locationProvider) {

	$routeProvider.when('/', {
			templateUrl: 'index.html',
			controller: 'mainController.js'
	});

	if(window.history && window.history.pushState){
    		$locationProvider.html5Mode(true);
  		}
	});
})();