const mqtt = require("mqtt")
const client = mqtt.connect("http://localhost:12345")

client.on("message", (topic, message) => {
    console.log(`${topic}: ${message}`)
})
