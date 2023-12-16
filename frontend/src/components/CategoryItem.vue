<template>
<div class="main flex">
    <div class="card">
        <div class="cardData">data</div>
    </div>
    <div class="typography2">category</div>
</div>
</template>

<script>
export default {

}
</script>

<style>
.main{
    flex-direction: column;
}
.card{
width: 5rem;
height: 5rem;
margin:auto;
flex-shrink: 0;
background: #1A3848;
border-radius: 16px;
}
.cardData{
justify-content: center;
align-items: center;
padding: 1.5rem 1.4rem;
}
</style>