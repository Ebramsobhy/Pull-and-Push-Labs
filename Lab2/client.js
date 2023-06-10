let username = window.prompt("please enter your name")

let mywebsocket = new WebSocket("ws://localhost:8080");
let chatbox = document.getElementById('chat')
let mymessage = document.getElementById("message")

console.log(mywebsocket)

let userheader = document.getElementById("user")
userheader.innerText = username;

mywebsocket.onopen = function(){
       console.log("--- Connection opened ---")

       message = {
          name: username, 
          type:"login"
       }
       msg_to_send = JSON.stringify(message)
       mywebsocket.send(msg_to_send)
    }

mywebsocket.onclose = function(){

}

mywebsocket.onerror = function(){

}

mywebsocket.onmessage = function(event){
    console.log("message received")
    message_details = JSON.parse(event.data)
    chatbox.innerHTML += message_details.message
}

mymessage.addEventListener("keyup", function(event){
    console.log(event)
    if (event.code === "Enter"){
        message = {
            "type":"chat",
            "body": mymessage.value+"\n"
        }

        msg_to_send = JSON.stringify(message)
        mywebsocket.send(msg_to_send)
        chatbox.innerHTML += "Me: " + mymessage.value+"\n"
        mymessage.value = ""
    }

})

