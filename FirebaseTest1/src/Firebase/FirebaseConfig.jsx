// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyBlqqCNFz3tfm2aPiXeEYu1-Hwwo7pZQNI",
  authDomain: "basededatosweb2025.firebaseapp.com",
  projectId: "basededatosweb2025",
  storageBucket: "basededatosweb2025.firebasestorage.app",
  messagingSenderId: "609351357531",
  appId: "1:609351357531:web:aee25e345e87bdf07e1b7e"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
// Initialize Cloud Firestore and get a reference to the service
const db = getFirestore(app);

export default db