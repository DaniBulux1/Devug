//Karen Reyes

import { signInWithPopup, GoogleAuthProvider, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/11.8.1/firebase-auth.js";
import { auth } from './firebase-config.js';

const provider = new GoogleAuthProvider();

function signInWithGoogle() {
    signInWithPopup(auth, provider)
    .then(() => {
      window.location.href = "/lista_tutoriales/";
    })
    .catch((error) => {
      alert("Error: " + error.message);
    });
}

function logOut() {
  signOut(auth).then(() => {
    window.location.href = "/lista_tutoriales/";
  });
}

const btnLogIn = document.getElementById("btn-google");
if (btnLogIn) {
  btnLogIn.addEventListener("click", signInWithGoogle);
}

const btnLogOut = document.getElementById("btn-logOut");
if (btnLogOut) {
  btnLogOut.addEventListener("click", logOut);
}

onAuthStateChanged(auth, (user) => {
    if (user) {
        console.log("User UID:", user.reloadUserInfo.localId);
        console.log("Usuario autenticado:", user);
        
        const displayName = user.displayName;
        const email = user.email;
        const photoURL = user.photoURL;

        document.getElementById("user-name").textContent = displayName;
        document.getElementById("user-email").textContent = email;
        document.getElementById("user-photo").src = photoURL;
    }
});