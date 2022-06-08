var c = document.getElementById("slate");
var currentTime = new Date();

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

var color = "red";
var mode = true;

var pixelDataBroadcast = document.getElementById("broadcast_data");
var pixelForm = document.getElementById("broadcast");

var drawRect = function(e) {
  checkTime()
  if (mode) {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);

    mouseX -= mouseX % 10;
    mouseY -= mouseY % 10;

    drawRectFromPoint(mouseX, mouseY, color);

    pixelInfo = `(${x}, ${y}, ${color})`;
    console.log(pixelInfo);
    pixelDataBroadcast.value = pixelInfo;
    pixelForm.submit();
  }
}

function drawRectFromPoint(x, y, cl) {
  var fillingRect = new Path2D(); //instead of beginPath
  fillingRect.moveTo(x, y);
  fillingRect.lineTo(x+10, y);
  fillingRect.lineTo(x+10, y+10);
  fillingRect.lineTo(x, y+10);
  fillingRect.lineTo(x, y);
  fillingRect.closePath();

  ctx.fillStyle = cl;
  ctx.fill(fillingRect);
  mode = false;
  showMessage();
  currentTime = new Date();
}

function prefillCanvas() {
  for (var i = 0; i < prefilledColors.length; i++) {
    drawRectFromPoint(prefilledColors[i][0], prefilledColors[i][1], prefilledColors[i][2]);
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

function showMessage() {
  let m = document.getElementById("blockout-message");
  m.className = "show";
  setTimeout(function(){ m.className = m.className.replace("show", ""); }, 10000);
}

function changeColor(c) {
  color = c;
  const d = document.getElementById("displayColor");
  d.innerHTML = c;
  d.style.color = c;
}

c.addEventListener("click", drawRect);
prefillCanvas();
