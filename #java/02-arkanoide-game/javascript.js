const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

canvas.width = 448;
canvas.height = 400;

//variables of game
let counter = 0;

/* variables of ball */
const ballRadius = 4;
// position of ball
let x = canvas.width/2;
let y = canvas.height - 30;
//velocity of ball

let dx = 2;
let dy = -2;





function drawball(){
    ctx.beginpath();
    ctx.arc(x, y, ballRadius, 0, Math.Pi*2);
    ctx.fillStyle = "#fff";
    ctx.fill();
}


function drawPaddle(){}
function drawBricks(){}



function collisionDetection(){}
function ballMovement(){}
function paddleMovement(){} 

function draw (){
    
    // draw and checks the game
    drawball();
    drawPaddle();   
    drawBricks();
    //drawScore();

    //collision and movement
    collisionDetection();
    ballMovement();
    paddleMovement();



    window.requestAnimationFrame(draw);

}
draw() 