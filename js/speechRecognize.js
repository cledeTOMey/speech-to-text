/**
 * Speech Recognization with microphone stream
 * @requires sox see http://sox.sourceforge.net/
 * sudo apt-get install sox
 * @requires auth google api key
 * export GOOGLE_APPLICATION_CREDENTIALS="absolute_path/voice.json"
 * @module
 */

const recorder = require('node-record-lpcm16')
const speech = require('@google-cloud/speech')

/**
 * 
 * @param {*} encoding 
 * @param {*} sampleRateHertz 
 * @param {*} languageCode 
 */
const speechRecognize = ({ encoding, sampleRateHertz, languageCode }, onRecognized) => {


    const request = {
        config: {
            encoding, sampleRateHertz, languageCode
        },
        interimResults: false, //Get interim results from stream
    };

    // Creates a client
    const client = new speech.SpeechClient();

    // Create a recognize stream
    const recognizeStream = client
        .streamingRecognize(request)
        .on('error', console.error)
        .on('data', onRecognized);

    // Start recording and send the microphone input to the Speech API
    recorder
        .record({
            sampleRateHertz: sampleRateHertz,
            threshold: 0, //silence threshold
            recordProgram: 'rec', // Try also "arecord" or "sox"
            silence: '5.0', //seconds of silence before ending
        })
        .stream()
        .on('error', console.error)
        .pipe(recognizeStream);

    console.log('Listening, press Ctrl+C to stop.');
    // [END micStreamRecognize]
}

speechRecognize({
    encoding: "LINEAR16",
    sampleRateHertz: 16000,
    languageCode: "fr-FR"
}, data => {
    process.stdout.write(
        data.results[0] && data.results[0].alternatives[0]
            ? `Transcription: ${data.results[0].alternatives[0].transcript}\n`
            : `\n\nReached transcription time limit, press Ctrl+C\n`
    )
})
