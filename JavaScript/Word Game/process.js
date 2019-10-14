var app = angular.module("GameApp",[]);
app.controller("GameController",['$scope',function($scope){

var words = ["apple","orange","strawberry","mangustine","lemon"];
$scope.incletterschosen = [];
$scope.corletterschosen = [];
$scope.guesses = 6;
$scope.displayword = '';
$scope.input ={

    letter : ''
}

var selectWord = function(){
    var index = Math.round(Math.random()* words.length);
    return words[index];
}

var newgame = function(){

    $scope.incletterschosen = [];
    $scope.corletterschosen = [];
    $scope.guesses = 6;
    $scope.displayword = '';

    selectedword = selectWord();
    var tempDisplayword = '';
    for (var i = 0; i<selectedword.length;i++){
        tempDisplayword +='*';

    }
$scope.displayword = tempDisplayword;
}

$scope.letterchosen = function(){
    for (var i = 0; i <$scope.corletterschosen.length ;i++) {
        if($scope.corletterschosen[i].toLowerCase()==$scope.input.letter.toLowerCase()){
            $scope.input.letter="";
            return;
        }
        
    }
    for (var i = 0; i <$scope.incletterschosen.length ;i++) {
        if($scope.incletterschosen[i].toLowerCase()==$scope.input.letter.toLowerCase()){
            $scope.input.letter="";
            return;
        }
        
    }

    var correct =false;

    for(var i = 0; i<selectedword.length;i++){
        if(selectedword[i].toLowerCase()==$scope.input.letter.toLowerCase()){
            $scope.displayword = $scope.displayword.slice(0,i)+$scope.input.letter.toLowerCase()
            +$scope.displayword.slice(i+1);

            correct = true;
        }
    }
    if(correct){
        $scope.corletterschosen.push($scope.input.letter.toLowerCase());
    }
    else{
        $scope.guesses --;
        $scope.incletterschosen.push($scope.input.letter.toLowerCase());
    }

    $scope.input.letter = "";

    if($scope.guesses == 0){
        alert("Game Over !!");
    
            newgame();
        
    }
    if($scope.displayword.indexOf("*") == -1){
        alert("Weldone, You Won !!!");
    }
}

newgame();

}]); 