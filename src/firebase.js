const { initializeApp } = require("firebase/app");

const firebaseConfig = {
  apiKey: "AIzaSyCGB68pPQxktkKHcw7u9GdicHypwFBjP58",
  authDomain: "devcollection-c587d.firebaseapp.com",
  projectId: "devcollection-c587d",
  storageBucket: "devcollection-c587d.appspot.com",
  messagingSenderId: "586834796380",
  appId: "1:586834796380:web:670e6a76ba4327280e6b99",
  measurementId: "G-DM5J7NVZ6T",
};

module.exports = initializeApp(firebaseConfig);
