var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

var color = "red";
var mode = true;

var drawRect = function(e) {
  if (mode) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    var fillingRect = new Path2D(); //instead of beginPath
    fillingRect.moveTo(mouseX, mouseY);
    fillingRect.lineTo(mouseX+10, mouseY);
    fillingRect.lineTo(mouseX+10, mouseY+10);
    fillingRect.lineTo(mouseX, mouseY+10);
    fillingRect.lineTo(mouseX, mouseY);
    fillingRect.closePath();

    ctx.fillStyle = color;
    ctx.fill(fillingRect);
    mode = false;
  }
}

function changeColor(c) {
  color = c;
  console.log(color);
}

c.addEventListener("click", drawRect);
