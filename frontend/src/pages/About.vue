<template>
  <div>
      <div class="typography">About</div>
      <div class="bg"></div>
      <div class="flex aboutcontainer">
      <h2> Created by Sahil Sayani (21f1003203) as a part of the </h2>
      <h2>MAD2 Project at IIT Madras (BS Programming and Data Science)</h2>
    </div>
    </div>

</template>

<script>
export default {

}
</script>

<style>
.aboutcontainer{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 10%;
  margin-left: 10%;
  margin-right: 10%;
  margin-bottom: 10%;
}
.bg{
width: 99vw;
height: 99vh;
flex-shrink: 0;
border-radius: 906px;
background: #172C38;
position: absolute;
z-index: -50;
margin-top: -30%;
}
</style>