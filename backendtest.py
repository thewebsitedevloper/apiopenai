<!DOCTYPE html>
<html>
  <head>
    <title>Chatbot</title>
    <script>
      function sendMessage() {
        // Get user's input
        var input = document.getElementById("userInput").value;

        // Call the Python function to get a response from the chatbot
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/get_response", true);
        xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhr.onreadystatechange = function () {
          if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            // Update the chat window with the chatbot's response
            document.getElementById("chatWindow").innerHTML +=
              "<p>Chatbot: " + xhr.responseText + "</p>";
          }
        };
        xhr.send(JSON.stringify({ input: input }));

        // Clear the user's input
        document.getElementById("userInput").value = "";
      }
    </script>
  </head>
  <body>
    <div id="chatWindow"></div>
    <input type="text" id="userInput" />
    <button onclick="sendMessage()">Send</button>
  </body>
</html>