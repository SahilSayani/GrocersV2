<script setup>

</script>
<template>
  
  <div>
    <h1 class="typography">Login</h1>

    <form @submit.prevent="login">
      <label for="username">Email</label>
      <input
        type="email"
        id="email"
        name="email"
        placeholder="Type in your email.."
        v-model="email"
        required
      />

      <label for="password">Password</label>
      <input
        type="password"
        id="password"
        name="password"
        placeholder="Enter your password.."
        v-model="password"
        required
      />
      <input type="submit" name="submit" value="Log In" />
    </form>
    <p>
      Don't have an account?
      <router-link to="/signup" class="typography2 greentext signup">
        Sign Up</router-link
      >
    </p>
  </div>
</template>

<script>
import axios from "axios";
import { API_URL } from "../constants";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async login() {
      // Perform login logic here, such as sending a request to a server
      // with the email and password
      console.log(
        `Logging in with email: ${this.email} and password: ${this.password}`
      );

      const { data } = await axios.post(API_URL + "/login", {
        email: this.email,
        password: this.password,
      });
      const token = data.token;

      localStorage.setItem("token", token);
      localStorage.setItem("user", JSON.stringify(data));
      localStorage.setItem("email", this.email);

      console.log("After Login", { data });

      this.$router.push("/")

      // Whenever you need authentication
      // await axios.get(API_URL + "/wishlist", {
      //   headers: {
      //     Authorization: "Bearer " + data.token,
      //   },
      // });
    },
  },
};
</script>
<style>
form {
  margin: 4% auto 0 auto;
  padding: 30px;
  width: 400px;
  height: auto;
  overflow: hidden;
  border-radius: 10px;
}

form label {
  font-size: 14px;
  color: darkgray;
  cursor: pointer;
}

form label,
form input {
  float: left;
  clear: both;
}

form input {
  margin: 15px 0;
  padding: 15px 10px;
  width: 100%;
  outline: none;
  border: 1px solid #bbb;
  border-radius: 20px;
  display: inline-block;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -ms-transition: 0.2s ease all;
  -o-transition: 0.2s ease all;
  transition: 0.2s ease all;
}

form input[type="text"]:focus,
form input[type="password"]:focus {
  border-color: #23aa49;
}

input[type="submit"] {
  padding: 15px 50px;
  width: auto;
  background: #23aa49;
  border: none;
  color: white;
  cursor: pointer;
  display: inline-block;
  clear: right;
  -webkit-transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -ms-transition: 0.2s ease all;
  -o-transition: 0.2s ease all;
  transition: 0.2s ease all;
}

input[type="submit"]:hover {
  opacity: 0.8;
}

input[type="submit"]:active {
  opacity: 0.4;
}

.forgot,
.register {
  margin: 10px;
  float: left;
  clear: left;
  display: inline-block;
  color: cornflowerblue;
  text-decoration: none;
}

.forgot:hover,
.register:hover {
  color: darkgray;
}

input {
  font: 1.2em sans-serif;
  width: 300px;
  box-sizing: border-box;
  border: 1px solid #999;
  border-radius: 4px;
}
p {
  margin-left: 43%;
}
</style>
