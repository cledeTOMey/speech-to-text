/**
 * mqtt server example
 * @module
 */
const aedes = require("aedes")()
const server = require("net").createServer(aedes.handle)
const PORT = 12345

const speechRecognition = require("./speechRecognition")

// detect client connection
aedes.on("client", client => {
    console.log(`Client ${client.id} connected.`)
})

// start speech recognition
speechRecognition({
    encoding: "LINEAR16",
    sampleRateHertz: 16000,
    languageCode: "fr-FR"
}, data => {
    // verify result
    let transcript = "Reached transcription time limit, press Ctrl+C"
    if(data.results[0] && data.results[0].alternatives[0]){
        transcript = data.results[0].alternatives[0].transcript
    }
    console.log(`transcription : ${transcript}`)

    // publish the transcript when receiving
    aedes.publish({
        cmd: 'publish',
        qos: 2,
        topic: 'speech-to-text',
        payload: transcript,
        retain: false
      })
})

// mqtt://localhost:12345
server.listen(PORT, () => {
    console.log(`Server launched on ${PORT}, listening, press Ctrl+C to terminate.`)
})
