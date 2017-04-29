document.getElementById("id_text").addEventListener("keypress",charactercnt);

var a = 1;

function charactercnt() {
	var current = document.getElementById("counter");
	current.value = a;
	a++;
}

