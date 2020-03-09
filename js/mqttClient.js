/**
 * mqtt client example (for testing)
 */
const mqtt = require("mqtt")
const client = mqtt.connect("mqtt://localhost:12345")

client.on("connect", () => {
    console.log("Successfully connected to the server.")
    // when connected subscribe to the topic
    client.subscribe("speech-to-text")
})

client.on("message", (topic, message) => {
    console.log(`${topic}: ${message}`)
})
