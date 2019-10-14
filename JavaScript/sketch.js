let snake;
let bait;
var score = 0;
var alive = 1;
var highscore = 0;

function setup() {
  createCanvas(400, 400);
  
  snake = new Snake();
  bait = new Bait(random(width), random(height));
}

function draw() {
  background(0);
  
  snake.show();
  if(alive)
    snake.move();
  
  bait.show();
  
  if(overlap(snake, bait)){
    bait.refresh();
    score++;
    incLen =10;
  }

  if(snake.x<0 ||snake.x>width-2 || snake.y<0 || snake.y>height-5){
    alive = 0;
    textSize(60);
    text("Game Over", 30, 180);
    textSize(40);
    text("Score : "+score, 100, 300); 
    if(score > highscore)
      highscore = score;
    text("Highscore : "+highscore, 65, 350);
    textSize(25);
    text("Click to continue" , 100, 380);
  }else{
    textSize(20);
    text("Score : "+score, 300, 390);

  }

}

function mousePressed() {
  score = 0;
  alive = 1;
  snake = new Snake();
}

function overlap(snake, bait){
  if(dist(snake.x, snake.y, bait.x, bait.y) < 10){
    return 1;
  }
  return 0;
}

function keyPressed() {
  if(keyCode === DOWN_ARROW){
    snake.direction = 3;
  }else if(keyCode === UP_ARROW){
    snake.direction = 1;
  }else if(keyCode === LEFT_ARROW){
    snake.direction = 4;
  }else if(keyCode === RIGHT_ARROW){
    snake.direction = 2;
  }
}

class Snake{
  constructor() {
    this.x = 200;
    this.y = 200;
    this.length = 20;
    this.width = 5;
    this.direction = 1;
    this.snake = new Queue();
  
    for(var i=this.length; i>0; i--){
      var data = [this.x, this.y + i, 1];
      this.snake.pushE( data );
    }
  }
  
  show(){
    fill(255);
    for(var i=0; i<this.length; i++){
      if((this.snake.list[i])[2] === 1 || (this.snake.list[i])[2] === 3){
        rect((this.snake.list[i])[0], (this.snake.list[i])[1], this.width, 1); 
      }else{
        rect((this.snake.list[i])[0], (this.snake.list[i])[1], 1, this.width);
      }
    }
  }
  
  move(){
    if(this.direction == 1){
      this.y = this.y-1;
    }else if(this.direction == 2){
      this.x = this.x+1;
    }else if(this.direction == 3){
      this.y = this.y+1;
    }else if(this.direction == 4){
      this.x = this.x-1;
    }
    this.snake.pushE( [this.x, this.y, this.direction] );
    
    if(this.length <= this.snake.list.length)
	this.snake.popE();
  }


}


class Queue{
  constructor(){
    this.list = [];
  }
  
  pushE(elem) {
    this.list.push(elem);
  }
  
  popE(){
    if(this.list.length === 0){
      return "error";
    }else{
      this.list.splice(0, 1);
    }
  }
  
  destructor(){
  }
}


class Bait{
  constructor(x, y){
    this.x = x;
    this.y = y;
  }
  
  show(){
    fill(255,0,0);
    noStroke();
    circle(this.x, this.y, 4);
  }
  
  refresh(){
    this.x = random(width);
    this.y = random(height);
  }
}
