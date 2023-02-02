
var Websock = pc.createScript('playcanvas_websocket');
var ws;
Websock.attributes.add('server', { type: 'string', default: "ws://localhost:9999/"});
Websock.prototype.initialize = function () {
    ws = new WebSocket(this.server);
    ws.onmessage = function (message) {
        console.log(message.data);
    }
}