"use strict";

/**
 *WebSocket Interface
 */

/*const receivedMessage = {
    action: "join" | "start",
    data: [{
        id: "user_id",
        name: "user_name",
        avatar: "user_url"
    }]
};

const sentMessage = {
    action: "start"
};*/

class JoinView {
    constructor() {
        this.friends = [];
        this.userName = document.getElementById("user-name").value;
        this.hostName = document.getElementById("host-name").value;

        this.initComponents();
        this.initWebSocket();
    }

    initComponents() {
        this.$usersContainer = document.getElementById("joined-users-container");
        this.$startGame = document.getElementById("start-game");
        this.$startGame.addEventListener("click", () => {
            this.startGame();
        });
    }

    initWebSocket() {
        this.socket = new WebSocket(`ws://${window.location.host}/join/${this.hostName}`);

        this.socket.onmessage = (event) => {
            const message = JSON.parse(event.data);
            this.handleStatusChange(message);
        }
    }

    handleStatusChange(message) {
        if (message.action = "join") {
            this.addFriend(message.data);

            if (this.friends.length >= 1) {
                this.$startGame.disabled = false;
                if (this.hostName === this.userName) {
                    this.$startGame.innerHTML = "Waiting for host to start the game...";
                }
            }
        } else if (message.action = "start") {
            this.navigateToGame();
        }
    }

    addFriend(friends) {
        for (let friend of friends) {
            if (friend.id in this.friends || friend.id === this.userName) continue;

            this.friends.push(friend.id);

            const template = `<img class="joined-user-avatar" src="${friend.avatar}" title="${friend.name}">`;
            this.$usersContainer.innerHTML += template;
        }
    }

    startGame() {
        this.socket.send({
            action: "start"
        });
    }

    navigateToGame() {
        window.location = `${window.location.host}/monopoly`
    }
}

window.onload = () => {
    new JoinView();
};