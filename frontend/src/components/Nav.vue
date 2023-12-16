<template>
<nav class="flex nav">
<img src="../assets/logo.svg" style="height:4rem; margin-top:0.5rem; margin-left: 1rem;"/>
<div class="typography logotitle">Grocers</div>
<div class="rightnav">
<ul class="navbar-nav">
        <div class="search">
            
        </div>
        <li class="nav-item" v-if="role === 1">
            <a class="nav-link" @click="GoToAdmin">
                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="12" viewBox="0 0 384 512"><path d="M221.5 51.7C216.6 39.8 204.9 32 192 32s-24.6 7.8-29.5 19.7l-120 288-40 96c-6.8 16.3 .9 35 17.2 41.8s35-.9 41.8-17.2L93.3 384H290.7l31.8 76.3c6.8 16.3 25.5 24 41.8 17.2s24-25.5 17.2-41.8l-40-96-120-288zM264 320H120l72-172.8L264 320z"/>
                </svg>
            </a>
        </li>
        <li class="nav-item" v-if="role === 2">
            <a class="nav-link" @click="GoToManager">
                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="14" viewBox="0 0 448 512"><path d="M22.7 33.4c13.5-4.1 28.1 1.1 35.9 12.9L224 294.3 389.4 46.2c7.8-11.7 22.4-17 35.9-12.9S448 49.9 448 64V448c0 17.7-14.3 32-32 32s-32-14.3-32-32V169.7L250.6 369.8c-5.9 8.9-15.9 14.2-26.6 14.2s-20.7-5.3-26.6-14.2L64 169.7V448c0 17.7-14.3 32-32 32s-32-14.3-32-32V64C0 49.9 9.2 37.5 22.7 33.4z"/>
                </svg>
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" @click="GoToHome">
                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="18" viewBox="0 0 576 512"><path d="M575.8 255.5c0 18-15 32.1-32 32.1h-32l.7 160.2c0 2.7-.2 5.4-.5 8.1V472c0 22.1-17.9 40-40 40H456c-1.1 0-2.2 0-3.3-.1c-1.4 .1-2.8 .1-4.2 .1H416 392c-22.1 0-40-17.9-40-40V448 384c0-17.7-14.3-32-32-32H256c-17.7 0-32 14.3-32 32v64 24c0 22.1-17.9 40-40 40H160 128.1c-1.5 0-3-.1-4.5-.2c-1.2 .1-2.4 .2-3.6 .2H104c-22.1 0-40-17.9-40-40V360c0-.9 0-1.9 .1-2.8V287.6H32c-18 0-32-14-32-32.1c0-9 3-17 10-24L266.4 8c7-7 15-8 22-8s15 2 21 7L564.8 231.5c8 7 12 15 11 24z"/>
                </svg>
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" @click="goToLogin" >
                <svg xmlns="http://www.w3.org/2000/svg" height="24"  viewBox="0 0 448 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/></svg>
            </a>
        </li>
        <li class="nav-item">
            <a class="nav-link" @click="goToCart">
                <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 576 512"><!--! Font Awesome Free 6.4.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M0 24C0 10.7 10.7 0 24 0H69.5c22 0 41.5 12.8 50.6 32h411c26.3 0 45.5 25 38.6 50.4l-41 152.3c-8.5 31.4-37 53.3-69.5 53.3H170.7l5.4 28.5c2.2 11.3 12.1 19.5 23.6 19.5H488c13.3 0 24 10.7 24 24s-10.7 24-24 24H199.7c-34.6 0-64.3-24.6-70.7-58.5L77.4 54.5c-.7-3.8-4-6.5-7.9-6.5H24C10.7 48 0 37.3 0 24zM128 464a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm336-48a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"/></svg>
            </a>
            <!-- <b-badge :count="totalItems" showZero>2</b-badge> -->
        </li>
        <li class="nav-item">
            <a class="nav-link" @click="goToAbout" >
                <svg xmlns="http://www.w3.org/2000/svg" height="16" width="18" viewBox="0 0 576 512"><path d="M512 80c8.8 0 16 7.2 16 16V416c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V96c0-8.8 7.2-16 16-16H512zM64 32C28.7 32 0 60.7 0 96V416c0 35.3 28.7 64 64 64H512c35.3 0 64-28.7 64-64V96c0-35.3-28.7-64-64-64H64zM208 256a64 64 0 1 0 0-128 64 64 0 1 0 0 128zm-32 32c-44.2 0-80 35.8-80 80c0 8.8 7.2 16 16 16H304c8.8 0 16-7.2 16-16c0-44.2-35.8-80-80-80H176zM376 144c-13.3 0-24 10.7-24 24s10.7 24 24 24h80c13.3 0 24-10.7 24-24s-10.7-24-24-24H376zm0 96c-13.3 0-24 10.7-24 24s10.7 24 24 24h80c13.3 0 24-10.7 24-24s-10.7-24-24-24H376z"/></svg>
            </a>
        </li>
    </ul>
</div>
</nav>
</template>

<script>
export default {
    name: "Nav",
    props: {
    role: Number, // Assuming role is a number, adjust the type accordingly
  },
  methods: {
    goToLogin() {
      this.$router.push("/login");
    },
    goToCart() {
      this.$router.push("/cart");
    },
    GoToHome() {
      this.$router.push("/");
    },
    GoToManager() {
      this.$router.push("/manager");
    },
    GoToAdmin() {
      this.$router.push("/admin");
    },
    goToAbout() {
      this.$router.push("/about");
    },
  },
};
</script>

<style>
.logotitle{
    font-size: 2rem;
    font-weight: 700;
    color: #ffffff;
    margin-left: 2rem;
    justify-content: center;
}
.nav{
    align-items: center;
}
.search{
    display: flex;
    width: 15rem;
    padding-bottom: 0.5rem;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    gap: 0.5rem;
    border-radius: 2rem;
    
    
}
ul{
    list-style-type: none;
    text-decoration: none;
    
}
.navbar-nav{
    display:flex;
    gap: 2rem;
    
}
.rightnav{
    margin-left: auto;
    margin-right: 5%;
    gap: 2rem;
}
svg{
    margin-right: 1rem;
    margin-top: 0.5rem;
    height: 2rem;
    width: 2rem;
    fill: #617986;
}
svg:hover {
  fill: #ffffff;
}
</style>