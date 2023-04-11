var kwadrat = document.getElementById("kwadrat");

var kolory = ["blue", "green", "red"];
var kolor = kolory[0]; // początkowo ustawiamy kolor na niebieski
var czas_reakcji = null;
var przycisk = document.getElementById("przycisk");
var czas_reakcji_element = document.getElementById("czas-reakcji");

function zmienKolor() {
    var randomIndex = Math.floor(Math.random()*3)
    kolor = kolory[randomIndex];
    kwadrat.style.backgroundColor = kolor;
    if (kolor === "green") {
        czas_reakcji = new Date().getTime();
    }
}

setInterval(zmienKolor, 1000);

przycisk.addEventListener("click", function() {
    if (czas_reakcji !== null && kolor === "green") {
        var czas = new Date().getTime() - czas_reakcji;
        czas_reakcji_element.innerHTML = "Czas reakcji: " + czas + " ms";
        czas_reakcji = null;
    } else {
        czas_reakcji_element.innerHTML = "To nie jest zielony"
    }
});
