const crypto = require("crypto")

const time = Math.round(new Date().getTime() / 1000)
const postData = { file_name: "16859981008371.png" }
const plaintext = "body="
  .concat(JSON.stringify(postData), "&timestamp=")
  .concat(time)
const hash = crypto.createHash("md5").update(plaintext).digest("hex")
console.log(time)
console.log(hash)
