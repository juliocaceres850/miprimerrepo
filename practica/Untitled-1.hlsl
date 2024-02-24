<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página de Respuestas</title>
</head>
<body>
    <div id="chat-container">
        <div id="chat-output"></div>
        <input type="text" id="user-input" placeholder="Hazme una pregunta...">
        <button onclick="askQuestion()">Enviar</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

#chat-container {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

#chat-output {
    height: 200px;
    overflow-y: scroll;
    border-bottom: 1px solid #ccc;
    margin-bottom: 10px;
}

input {
    width: 70%;
    padding: 8px;
    box-sizing: border-box;
}

button {
    padding: 8px;
    cursor: pointer;
}
function askQuestion() {
    var userInput = document.getElementById("user-input").value;
    var chatOutput = document.getElementById("chat-output");

    // Muestra la pregunta del usuario
    chatOutput.innerHTML += "<strong>Tú:</strong> " + userInput + "<br>";

    // Lógica de generación de respuesta (puedes personalizar esto)
    var response = generateResponse(userInput);

    // Muestra la respuesta en el chat
    chatOutput.innerHTML += "<strong>Respuesta:</strong> " + response + "<br>";

    // Limpia el campo de entrada
    document.getElementById("user-input").value = "";

    // Desplázate hacia abajo para mostrar la respuesta más reciente
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

function generateResponse(question) {
    // Aquí puedes implementar la lógica para generar respuestas basadas en la pregunta
    // Por ejemplo, podrías tener un conjunto de respuestas predefinidas o utilizar un modelo de lenguaje como GPT-3 para respuestas más avanzadas.
    return "¡Gracias por tu pregunta! La respuesta podría estar en camino...";
}
