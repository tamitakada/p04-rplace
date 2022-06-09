var c = document.getElementById("slate");
var ctx = c.getContext("2d");

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
}

function prefillCanvas() {
  for (var i = 0; i < prefilledColors.length; i++) {
    drawRectFromPoint(
      Number(prefilledColors[i][0]), 
      Number(prefilledColors[i][1]), 
      prefilledColors[i][2]
    );
  }
}

prefillCanvas();
