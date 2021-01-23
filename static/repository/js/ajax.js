body {
  background-color: white;
}

.cabecera {
  text-align: center;
  color: #006bb4;
  font-family: Roboto, sans-serif;
}

.login-form {
  margin: auto;
  height: 15em;
  border-radius:  .6em;
  background-color: #f2f2f2;
  font-family: arial;
  display: flex;
  flex-direction:column;
  justify-content: space-evenly;
  align-items: center;
  
}

.login-form__text {
  display: block;
  width: 90%;
  padding: 0 0 0 .6em;
  height: 2.6em;
  border: .2em solid #d7d7d7;
  border-radius: .6em;
  font-family: Roboto, sans-serif;
  font-size: 1.2rem;
  box-sizing: border-box;
}

.login-form__text:focus {
    outline: 0;
    border: .2em solid #006bb4;
}

.login-form__submit {
  border: .2em solid #006bb4;
  width: 90%;
  height: 2.6rem;
  background-color: #006bb4;
  color: white;
  border-radius: .6em;
  font-family: Roboto, sans-serif;
  font-size: 1.2rem;
}
.login-form__submit:focus {
    outline: 0;
}

.login-form__submit:active {
  background-color: #01448a;
  border: .2em solid #01448a;
}

.olvido-password {
  text-align: center;
  text-decoration: none;
}

.olvido-password:active {
  color: #003375;
}

.olvido-password:visited {
  color: #003375;
}

.p {
  text-align: center;
  font-family: Roboto, sans-serif;
  color: #003375;
  font-size: 1.2em;
}

.registrarse-link {
  text-decoration: none;
}

.registrarse-link