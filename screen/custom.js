const socket = new WebSocket('ws://' + wsHost + ':' + wsPort);

var audio = new Audio('alert.mp3');

socket.addEventListener('message', function (event) {
    audio.play();
    $("#number").text(event.data)
});
