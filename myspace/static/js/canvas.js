var c = document.getElementById("slate");
var currentTime = new Date();

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

var color = "red";
var mode = true;

var drawRect = function(e) {
  checkTime()
  if (mode) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    var fillingRect = new Path2D(); //instead of beginPath
    // stays within grid
    mouseX -= mouseX % 10;
    mouseY -= mouseY % 10;
    fillingRect.moveTo(mouseX, mouseY);
    fillingRect.lineTo(mouseX+10, mouseY);
    fillingRect.lineTo(mouseX+10, mouseY+10);
    fillingRect.lineTo(mouseX, mouseY+10);
    fillingRect.lineTo(mouseX, mouseY);
    fillingRect.closePath();

    ctx.fillStyle = color;
    ctx.fill(fillingRect);
    mode = false;
    currentTime = new Date();
  }
}

function checkTime() {
  var checkNow = new Date();
  var timeDiff = (checkNow - currentTime) / 1000;
  console.log("timeDiff: ", timeDiff);
  if (timeDiff >= 10) {
    mode = true;
  }
}

function changeColor(c) {
  color = c;
  console.log(color);
}

c.addEventListener("click", drawRect);
