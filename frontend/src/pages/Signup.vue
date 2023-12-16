<script setup>
import Nav from "../components/Nav.vue";
import router from "../router";
</script>
<template>
  <div>
    <h1 class="typography">Sign Up</h1>
    <form @submit.prevent="submitForm">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="username" required />
      <br />
      <label for="email">Email:</label>
      <input type="email" id="email" v-model="email" required />
      <br />
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="password" required />
      <br />
      <button type="submit">Sign Up</button>
    </form>
    <p class="para">
      already a user?
      <router-link to="/login" class="typography2 greentext">Login</router-link>
    </p>
  </div>
</template>

<script>
import axios from "axios";
import { API_URL } from "../constants";

export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  methods: {
    async submitForm() {
      // Here you can add your form submission logic
      console.log(
        "Form submitted with:",
        this.username,
        this.email,
        this.password
      );

      try {
        await axios.post(API_URL + "/signup", {
          name: this.username,
          email: this.email,
          password: this.password,
        });
      } catch (e) {
        console.error(e);
      }

      // Success
    },
  },
};
</script>
<style>
button[type="submit"] {
  padding: 15px 50px;
  width: auto;
  background: #23aa49;
  border: none;
  color: white;
  cursor: pointer;
  display: inline-block;
  border-radius: 20px;
  clear: right;
  -webkit-transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -ms-transition: 0.2s ease all;
  -o-transition: 0.2s ease all;
  transition: 0.2s ease all;
}

button[type="submit"]:hover {
  opacity: 0.8;
}

button[type="submit"]:active {
  opacity: 0.4;
}
.para {
  margin-left: 46%;
}
</style>
