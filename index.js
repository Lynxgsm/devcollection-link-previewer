const express = require("express");
const app = express();
const { resolve } = require("path");
const fs = require("fs");
const { spawn } = require("child_process");
const os = require("os");
const port = process.env.PORT || 3000;
const JSON5 = require("json5");

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post("/api/preview", (req, res) => {
  const pythoncmd = os.type().toLowerCase() === "darwin" ? "python3" : "python";
  console.log(req.body);
  python = spawn(pythoncmd, [
    "-u",
    resolve(__dirname, "scripts", "main.py"),
    req.body.url,
  ]);

  python.stdout.on("data", function (data) {
    try {
      res.send(JSON5.parse(data.toString("binary")));
    } catch (error) {
      res.send(error);
    }
  });

  // in close event we are sure that stream from child process is closed
  python.on("close", (code) => {
    console.log(`child process close all stdio with code ${code}`);
  });
});

app.post("/api/download", (req, res) => {});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
