const express = require('express');
const path = require("node:path");
const app = express();
const port = 1011;
app.use(express.static(path.join(__dirname, 'static')));


app.listen(port, () => {
    console.log("Server is running on port " + port);
})
