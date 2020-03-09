# Speech Recognition implemented on JavaScript with google speech API
## Get Started
### install sox and configure google API Auth
Sox `http://sox.sourceforge.net/`
```bash
sudo apt-get install sox
```
Set google api credentials as a glabal variable
```bash
export GOOGLE_APPLICATION_CREDENTIALS="absolute_path/voice.json"
```
### install dependencies
```bash
npm i
```
### start server
```bash
npm run server
```
Server starts on `mqtt://localhost:12345`
### start client (for testing)
```bash
npm run client
```
And start speaking
