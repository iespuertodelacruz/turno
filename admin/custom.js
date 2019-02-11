const socket = new WebSocket('ws://' + wsHost + ':' + wsPort);

socket.addEventListener('message', function (event) {
    $("#turn").val(event.data)
});

$("#set-turn").click(function(event) {
    event.preventDefault();
    socket.send($("#turn").val());
});

$("#inc-turn").click(function(event) {
    event.preventDefault();
    current_turn = parseInt($("#turn").val());
    current_turn = (current_turn + 1) % 100;
    $("#turn").val(current_turn);
    socket.send(current_turn);
});

$("#dec-turn").click(function(event) {
    event.preventDefault();
    current_turn = parseInt($("#turn").val());
    if (current_turn == 0)
        current_turn = 99;
    else
        current_turn--;
    $("#turn").val(current_turn);
    socket.send(current_turn);
});
