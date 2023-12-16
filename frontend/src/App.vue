<script setup>
import { computed } from "vue";
import router from "./router";
import Nav from "./components/Nav.vue";
const role = computed(() => JSON.parse(localStorage.getItem("user"))?.user_role || 3);
</script>

<template>
  <Nav :role=role />
  <div>
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/signup">Sign Up</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/cart">Cart</router-link>|
      <router-link v-if="role === 2" to="/manager">Manager</router-link> |
      <router-link v-if="role === 1" to="/admin">Admin</router-link> |
      <router-link to="/productdetails">Product Details</router-link> |
      <router-link to="/category">Category</router-link> |
    </div> -->
    <router-view />
  </div>
</template>

<style></style>
