const express = require("express");
const app = express();
const path = require("path");
const PORT = process.env.PORT || 5000;
const firebaseApp = require("./src/firebase");
const {
  collection,
  getFirestore,
  getDocs,
  addDoc,
} = require("firebase/firestore/lite");
const linkPreviewGenerator = require("link-preview-generator");
const puppeteer = require("puppeteer");
// MIDDLEWARES

db = getFirestore(firebaseApp);

app
  .use(express.static(path.join(__dirname, "public")))
  .use(express.json())
  .use(express.urlencoded({ extended: true }))
  .set("views", path.join(__dirname, "views"))
  .set("view engine", "ejs");

app.get("/api/articles", (req, res) => {
  getArticles(db)
    .then((articles) => {
      res.send(articles);
    })
    .catch((err) => {
      console.log(err);
    });
});

app.post("/api/article", (req, res) => {
  getPreviewData(req.body.url).then((data) => {
    addArticle(db, { ...data, url: req.body.url }).then((article) => {
      res.send(article);
    });
  });
});

app.get("/api/pdf", (req, res) => {
  printPDF(
    "https://programmingwithswift.com/how-to-save-a-file-locally-with-flutter/"
  ).then((pdf) => {
    res.set({
      "Content-Type": "application/pdf",
      "Content-Length": pdf.length,
    });
    res.send(pdf);
  });
});

app.post("/api/getinfo", (req, res) => {
  getPreviewData(req.body.url).then((data) => {
    res.send(data);
  });
});

async function getArticles(db) {
  const articleCols = collection(db, "articles");
  const snapshot = await getDocs(articleCols);
  return snapshot.docs.map((doc) => doc.data());
}

async function addArticle(db, body) {
  const article = collection(db, "articles");
  return await addDoc(article, body);
}

async function getPreviewData(url) {
  return linkPreviewGenerator(url);
}

async function printPDF(url) {
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(url, {
    waitUntil: "networkidle0",
  });
  const pdf = await page.pdf({
    format: "A4",
  });

  await browser.close();
  return pdf;
}

app.get("/", (req, res) => res.render("pages/index"));

app.listen(PORT, () => {
  console.log(`Listening on ${PORT}`);
});
