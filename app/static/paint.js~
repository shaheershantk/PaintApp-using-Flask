document.getElementById("pencil").onclick=function() {
	var canvas = document.querySelector('#paint');
	var ctx = canvas.getContext('2d');
	
	var sketch = document.querySelector('#sketch');
	var sketch_style = getComputedStyle(sketch);
	// Creating a tmp canvas	
	var tmp_canvas = document.createElement('canvas');
	var tmp_ctx = tmp_canvas.getContext('2d');
	tmp_canvas.id = 'tmp_canvas';
	tmp_canvas.width = canvas.width;
	tmp_canvas.height = canvas.height;
	
	sketch.appendChild(tmp_canvas);

	colors(ctx);
	var mouse = {x: 0, y: 0};
	var last_mouse = {x: 0, y: 0};
	
	/* Mouse Capturing Work */
	tmp_canvas.addEventListener('mousemove', function(e) {
		last_mouse.x = mouse.x;
		last_mouse.y = mouse.y;
		
		mouse.x = e.pageX - this.offsetLeft;
		mouse.y = e.pageY - this.offsetTop;
	}, false);
	/*pencil color*/
	colors(tmp_ctx);
	/* Drawing on Paint App */
	tmp_ctx.lineWidth = 5;
	tmp_ctx.lineJoin = 'round';
	tmp_ctx.lineCap = 'round';
	tmp_ctx.strokeStyle = 'blue';
	
	tmp_canvas.addEventListener('mousedown', function(e) {
		x=e.x;
		y=e.y;
		draw=true;
	}
	tmp_canvas.addEventListener('mousemove', onPaint, false);
		if (draw){
  			a =event.x;
			b =event.y;
   			context.beginPath();
   			context.moveTo(x,y);
   			context.lineTo(a,b);
   			context.stroke();
   			context.closePath();
   			jsondata.push({"Type":"pencil", "X0":x,"Y0":y,"X1":a,"Y1":b,"width":context.lineWidth,"color":context.strokeStyle})
   			x=a;
   			y=b;
		
	}, false);
	
	tmp_canvas.addEventListener('mouseup', function() {
		tmp_canvas.removeEventListener('mousemove', onPaint, false);
		// Writing down to real canvas now
		ctx.drawImage(tmp_canvas, 0, 0);
		// Clearing tmp canvas
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		
	}, false);
	
	var onPaint = function() {
		tmp_ctx.beginPath();
		tmp_ctx.moveTo(last_mouse.x, last_mouse.y);
		tmp_ctx.lineTo(mouse.x, mouse.y);
		tmp_ctx.closePath();
		tmp_ctx.stroke();
	};
	
}
document.getElementById("rectangle").onclick=function() {
	
	var canvas = document.querySelector('#paint');
	var ctx = canvas.getContext('2d');
	
	var sketch = document.querySelector('#sketch');
	var sketch_style = getComputedStyle(sketch);
	
	
	
	// Creating a tmp canvas
	var tmp_canvas = document.createElement('canvas');
	var tmp_ctx = tmp_canvas.getContext('2d');
	tmp_canvas.id = 'tmp_canvas';
	tmp_canvas.width = canvas.width;
	tmp_canvas.height = canvas.height;
	
	sketch.appendChild(tmp_canvas);
	colors(tmp_ctx);
	var mouse = {x: 0, y: 0};
	var start_mouse = {x: 0, y: 0};
	
	
	/* Mouse Capturing Work */
	tmp_canvas.addEventListener('mousemove', function(e) {
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;
	}, false);
	
	
	/* Drawing on Paint App */
	tmp_ctx.lineWidth = 5;
	tmp_ctx.lineJoin = 'round';
	tmp_ctx.lineCap = 'round';
	tmp_ctx.strokeStyle = 'blue';
	tmp_ctx.fillStyle = 'blue';
	
	tmp_canvas.addEventListener('mousedown', function(e) {
		img=context.getImageData(0,0,canvas.width,canvas.height);
 		startx=e.x;
 		starty=e.y;
 		drag2=true;
		}
	tmp_canvas.addEventListener('mousemove', onPaint, false);
		
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;
		
		start_mouse.x = mouse.x;
		start_mouse.y = mouse.y;
		
		onPaint();
	}, false);
	
	tmp_canvas.addEventListener('mouseup', function() {
		tmp_canvas.removeEventListener('mousemove', onPaint, false);
		drag2=false;
		jsondata.push({"Type":"rect", 			"X0":startx,"Y0":starty,"W":rectw,"H":recth,"width":context.lineWidth,"color":context.strokeStyle,"fill":f})
		
		
		// Writing down to real canvas now
		ctx.drawImage(tmp_canvas, 0, 0);
		// Clearing tmp canvas
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		}, false);
	
	var onPaint = function() {
		
		// Tmp canvas is always cleared up before drawing.
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		
		var x = Math.min(mouse.x, start_mouse.x);
		var y = Math.min(mouse.y, start_mouse.y);
		var width = Math.abs(mouse.x - start_mouse.x);
		var height = Math.abs(mouse.y - start_mouse.y);
		tmp_ctx.strokeRect(x, y, width, height);
		
	};
	
}



document.getElementById("circle").onclick=
function() {
	
	var canvas = document.querySelector('#paint');
	var ctx = canvas.getContext('2d');
	
	var sketch = document.querySelector('#sketch');
	var sketch_style = getComputedStyle(sketch);
	
	
	// Creating a tmp canvas
	var tmp_canvas = document.createElement('canvas');
	var tmp_ctx = tmp_canvas.getContext('2d');
	tmp_canvas.id = 'tmp_canvas';
	tmp_canvas.width = canvas.width;
	tmp_canvas.height = canvas.height;
	
	sketch.appendChild(tmp_canvas);
	colors(tmp_ctx);
	var mouse = {x: 0, y: 0};
	var start_mouse = {x: 0, y: 0};
	var last_mouse = {x: 0, y: 0};
	
	
	/* Mouse Capturing Work */
	tmp_canvas.addEventListener('mousemove', function(e) {
		mouse.x = e.pageX - this.offsetLeft;
		mouse.y = e.pageY - this.offsetTop;
	}, false);
	
	
	/* Drawing on Paint App */
	tmp_ctx.lineWidth = 5;
	tmp_ctx.lineJoin = 'round';
	tmp_ctx.lineCap = 'round';
	tmp_ctx.strokeStyle = 'blue';
	tmp_ctx.fillStyle = 'blue';
	
	tmp_canvas.addEventListener('mousedown', function(e) {
		img=context.getImageData(0,0,canvas.width,canvas.height);
 		startx=e.x;
 		starty=e.y;
 		drag3=true;
		}
		tmp_canvas.addEventListener('mousemove', onPaint, false);
		
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;
		
		start_mouse.x = mouse.x;
		start_mouse.y = mouse.y;
		
		onPaint();
	}, false);
	
	tmp_canvas.addEventListener('mouseup', function() {
		tmp_canvas.removeEventListener('mousemove', onPaint, false);
		jsondata.push({"Type":"circle", 		"X0":startx,"Y0":starty,"X1":endx,"Y1":endy,"width":context.lineWidth,"color":context.strokeStyle,"fill":f})
		drag3=false;
		// Writing down to real canvas now
		ctx.drawImage(tmp_canvas, 0, 0);
		// Clearing tmp canvas
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		
	}, false);
	
	var onPaint = function() {
		
		// Tmp canvas is always cleared up before drawing.
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		
		var x = (mouse.x + start_mouse.x) / 2;
		var y = (mouse.y + start_mouse.y) / 2;
		
		var radius = Math.max(
			Math.abs(mouse.x - start_mouse.x),
			Math.abs(mouse.y - start_mouse.y)
		) / 2;
		
		tmp_ctx.beginPath();
		tmp_ctx.arc(x, y, radius, 0, Math.PI*2, false);
		// tmp_ctx.arc(x, y, 5, 0, Math.PI*2, false);
		tmp_ctx.stroke();
		tmp_ctx.closePath();
		
	};
	
}
document.getElementById("line").onclick=function() {
	
	var canvas = document.querySelector('#paint');
	var ctx = canvas.getContext('2d');
	
	var sketch = document.querySelector('#sketch');
	var sketch_style = getComputedStyle(sketch);
	
	
	// Creating a tmp canvas
	var tmp_canvas = document.createElement('canvas');
	var tmp_ctx = tmp_canvas.getContext('2d');
	tmp_canvas.id = 'tmp_canvas';
	tmp_canvas.width = canvas.width;
	tmp_canvas.height = canvas.height;
	
	sketch.appendChild(tmp_canvas);
	colors(tmp_ctx);
	var mouse = {x: 0, y: 0};
	var start_mouse = {x: 0, y: 0};
	
	
	/* Mouse Capturing Work */
	tmp_canvas.addEventListener('mousemove', function(e) {
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;
	}, false);
	
	
	/* Drawing on Paint App */
	tmp_ctx.lineWidth = 5;
	tmp_ctx.lineJoin = 'round';
	tmp_ctx.lineCap = 'round';
	tmp_ctx.strokeStyle = 'blue';
	tmp_ctx.fillStyle = 'blue';
	
	tmp_canvas.addEventListener('mousedown', function(e) {
		img=context.getImageData(0,0,canvas.width,canvas.height);
 		startx=e.x;
 		starty=e.y;
 		drag1=true;
		tmp_canvas.addEventListener('mousemove', onPaint, false);
		
		mouse.x = typeof e.offsetX !== 'undefined' ? e.offsetX : e.layerX;
		mouse.y = typeof e.offsetY !== 'undefined' ? e.offsetY : e.layerY;
		
		start_mouse.x = mouse.x;
		start_mouse.y = mouse.y;
		
		onPaint();
	}, false);
	
	tmp_canvas.addEventListener('mouseup', function() {
		tmp_canvas.removeEventListener('mousemove', onPaint, false);
		drag1=false;
		jsondata.push({"Type":"line", "X0":startx,"Y0":starty,"X1":endx,"Y1":endy,"width":context.lineWidth,"color":context.strokeStyle})
		
		// Writing down to real canvas now
		ctx.drawImage(tmp_canvas, 0, 0);
		// Clearing tmp canvas
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		
	}, false);
	
	var onPaint = function() {
		
		// Tmp canvas is always cleared up before drawing.
		tmp_ctx.clearRect(0, 0, tmp_canvas.width, tmp_canvas.height);
		
		tmp_ctx.beginPath();
		tmp_ctx.moveTo(start_mouse.x, start_mouse.y);
		tmp_ctx.lineTo(mouse.x, mouse.y);
		tmp_ctx.stroke();
		tmp_ctx.closePath();
		
	};
	
}


function colors(x){

	document.getElementById("black").onclick=function(){
	x.strokeStyle='black';  }
	
	document.getElementById("red").onclick=function(){
	x.strokeStyle='red';   }

	document.getElementById("green").onclick=function(){
	x.strokeStyle='green'; }

	document.getElementById("eraser").onclick=function(){
	x.strokeStyle='white'; }
	}
	document.getElementById("clear").onclick=function(){
		 ctx=document.getElementById("paint").getContext("2d");
 		 ctx.fillStyle="white";
		 ctx.fillRect(0, 0, 900, 500);  
}



