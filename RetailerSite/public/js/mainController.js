(function() {

	var app = angular.module('taiga');
	app.controller('mainController', ['$scope', '$http', '$timeout', '$window', function($scope, $http, $timeout, $window) {
		
		$scope.bought = false;

		$scope.emailSend = function() {
			$http.get("/api/email")
		    .then(function(response) {
		        $scope.bought = true;
		    });
		}
	
	}]);

})();