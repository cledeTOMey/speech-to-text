/**
 * Speech Recognition with microphone stream
 * @requires sox see http://sox.sourceforge.net/
 * sudo apt-get install sox
 * @requires auth set google api key as a global variable
 * export GOOGLE_APPLICATION_CREDENTIALS="absolute_path/voice.json"
 * @module
 */

const recorder = require('node-record-lpcm16')
const speech = require('@google-cloud/speech')

/**
 * capture microphone stream and use google speech api to convert it to text
 * @param {String} encoding - encoding of audio corresponding to audio input device
 * example : "LINEAR16"
 * @param {Number} sampleRateHertz - rate on Hz of audio sample
 * example : 16000, 48000
 * @param {String} languageCode - target language of recognition
 * example : "fr-FR", ""
 * @param {(data: Object): void} onRecognized - event listener that fires each time the
 * recognition stream returns a data
 * String result of recognition : data.results[0].alternatives[0].transcript
 */
const speechRecognition = ({ encoding, sampleRateHertz, languageCode }, onRecognized) => {

    // configure request
    const request = {
        config: {
            encoding, sampleRateHertz, languageCode
        },
        interimResults: false, // get the final result for each request
    };

    // init api client
    const client = new speech.SpeechClient();

    // Create a recognize stream
    const recognizeStream = client
        .streamingRecognize(request)
        .on('error', console.error)
        .on('data', onRecognized);

    // Start recording and send the microphone input to the Speech API
    recorder
        .record({
            sampleRateHertz,
            threshold: 0, //silence threshold
            recordProgram: 'rec', // Try also "arecord" or "sox"
            silence: '5.0', //seconds of silence before ending
        })
        .stream()
        .on('error', console.error)
        .pipe(recognizeStream);
        
    // [END micStreamRecognize]
}

module.exports = speechRecognition
