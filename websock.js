let ws = new WebSocket("ws://localhost:9999/");
let log = "";
ws.onmessage = function (message) {
    log = log + "<br>" + message.data;
    document.getElementById("txt").innerHTML = log;
}
document.getElementById("forward").addEventListener("click", function () {
     ws.send("forward");
 });
 document.getElementById("stop").addEventListener("click", function () {
    ws.send("stop");
});
 document.getElementById("backward").addEventListener("click", function () {
    ws.send("backward");
});