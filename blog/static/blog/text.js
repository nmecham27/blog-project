document.getElementById("id_text").addEventListener("keydown",charactercnt);

var a = 0;

function charactercnt() {
	var x = event.keyCode;
	if(x == 8 && a > 0){
	    --a;
	    var current = document.getElementById("counter");
	    current.value = a;
	}
	else if(x != 8){
	    var current = document.getElementById("counter");
	    ++a;
	    current.value = a;
	}
}

