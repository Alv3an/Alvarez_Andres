import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import db from './Firebase/FirebaseConfig'
import { doc, getDoc } from "firebase/firestore";
import CardPet from './Components/CardPet/CardPet'
import { collection, query, where, getDocs } from "firebase/firestore";

function App() {
  //  const [pets, setPets] = useState(null)
  const [pets, setPets] = useState([])

  useEffect(() => {
    const getPets = async () => {

      const q = query(collection(db, "mascotas"));//, where("especie", "==", "Perro"));
      const a = query(collection(db, "mascotas/ecU61udwSupy41ppWK8b/images"));
      const querySnapshot = await getDocs(q);
      const querySnapshot_1 = await getDocs(a);
      const arrayImages = [];
      const arrayPets = [];
      querySnapshot.forEach((doc) => {
        console.log(doc.id, " => ", doc.data());
        arrayPets.push({ ...doc.data(), id: doc.id })
      });
      querySnapshot_1.forEach((doc) => {
        console.log(doc.id, " => ", doc.data());
        arrayPets.push({ ...doc.data(), id: doc.id })
      });
      setPets(arrayPets)
      console.log(arrayPets)
    }
    getPets();
  }, [])

  return (
    <main>
      <h1>Hola Mundo</h1>
      {pets.length > 0 ? pets.map((item) => {
        return <CardPet pets={item} key={item.id} />
      }) : <h5>Cargando</h5>}
    </main>
  );
}

export default App


//Un solo documento
// useEffect(() => {
//   const getPets = async () => {
//     const docRef = doc(db, "mascotas", "ecU61udwSupy41ppWK8b");
//     const docSnap = await getDoc(docRef);

//     if (docSnap.exists()) {
//       console.log("Document data:", docSnap.data());
//       setPets(docSnap.data());
//     } else {
//       // docSnap.data() will be undefined in this case
//       console.log("No such document!");
//     }
//   }
//   getPets();