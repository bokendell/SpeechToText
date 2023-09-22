runSpeechRecog = () => {
    document.getElementById("output").innerHTML = "Loading text...";
    var output = document.getElementById('output');
    var action = document.getElementById('action');
    let recognition = new webkitSpeechRecognition();

    recognition.onstart = () => {
        action.innerHtml = "Listening..."
    }

    recognition.onResult = (e) => {
        var transcript = e.results[0][0].transcript;
        var confidence = e.results[0][0].confidence;
        output.innerHtml = transcript;
        output.classList.remove("hide")
        action.innerHtml = "";
    }
    recognition.start();
}
