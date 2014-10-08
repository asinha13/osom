var module = angular.module('OSOMBasicApp',[])

module.factory('svcBasic',["$http","$timeout",function($http, $timeout) {
    var self = {};
    var refresh_rate = 0; // Never refresh
    self.osom = {};
    var retries = 0;
    var max_retries = 3;

    var _poller = function() {
        self.get_new_osom()
        if (refresh_rate > 0) {
            $timeout(function to () {
                _poller();
            },refresh_rate*1000);
        }
    };

    self.set_refersh_rate = function(rate) {
        var old_rate = refresh_rate;
        refresh_rate = rate;
        if (old_rate<=0 && rate > 0) {
            _poller();
        }
    };

    self.get_osom_object = function() {
        self.get_new_osom();
        return self.osom;
    };

    self.get_new_osom = function() {
        $http.get('/api/')
            .success(function(data,status) {
                retries = 0;
                if (status!=200) {
                    console.log("Request status : ",status);
                    return;
                }
                angular.copy(data,self.osom);
            })
            .error(function(data,status) {
                if (retries <= max_retries) {
                    retries -= 1;
                    self.get_new_osom();
                }
            });
    };
    return self;
}]);


module.controller('ctrlBasic', ["$scope","svcBasic",function($scope, svcBasic) {
    $scope.osom = svcBasic.get_osom_object();

    $scope.set_refresh_rate = function(rate) {
        svcBasic.set_refresh_rate();
    };

    $scope.refresh = function() {
        svcBasic.get_new_osom();
    };
}]);