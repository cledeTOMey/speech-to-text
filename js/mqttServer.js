const aedes = require("aedes")()
const server = require("net").createServer(aedes.handle)

const speechRecognition = require("./speechRecognition")

speechRecognition({
    encoding: "LINEAR16",
    sampleRateHertz: 16000,
    languageCode: "fr-FR"
}, data => {
    const transcript = "Reached transcription time limit, press Ctrl+C"
    if(data.results[0] && data.results[0].alternatives[0]){
        transcript = data.results[0].alternatives[0].transcript
    }
    aedes.publish({
        cmd: 'publish',
        qos: 2,
        topic: 'speech-to-text',
        payload: transcript,
        retain: false
      })
})

server.listen(12345)
