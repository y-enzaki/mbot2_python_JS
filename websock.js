let ws = new WebSocket("ws://localhost:9999/");
let log = "";
let senddata = {};
let recvdata = {};
ws.onmessage = function (message) {
    log = log + "<br>" + message.data;
    document.getElementById("txt").innerHTML = log;
}
document.getElementById("forward").addEventListener("click", function () {
    let com = { command: "forward" };
    ws.send(JSON.stringify(com));
    //ws.send("forward");
 });
document.getElementById("stop").addEventListener("click", function () {
    let com = { command: "stop" };
    ws.send(JSON.stringify(com));
    //ws.send("stop");
});
document.getElementById("backward").addEventListener("click", function () {
    let com = { command: "backward" };
    ws.send(JSON.stringify(com));
    //ws.send("backward");
});
document.getElementById("fullpower").addEventListener("click", function () {
    let com = {
        command: "setpower",
        power1: 100,
    power2:100,
    };
    ws.send(JSON.stringify(com));
    //ws.send("backward");
});
document.getElementById("turn90").addEventListener("click", function () {
    let com = {
        command: "turn",
        angle1: 90,
    };
    ws.send(JSON.stringify(com));
    //ws.send("backward");
});
document.getElementById("reset").addEventListener("click", function () {
    let com = { command: "reset" };
    ws.send(JSON.stringify(com));
    //ws.send("backward");
});