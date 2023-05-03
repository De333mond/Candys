<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import "./style.css";

export default {
  name: 'App',
}
</script>

<style>
  @font-face {
    font-family: "Nunito";
    src: local("Nunito"),
    url(./assets/fonts/Nunito/Nunito-Regular.ttf) format("truetype");
  }
  @font-face {
    font-family: "Montserrat";
    src: local("Montserrat"),
    url(./assets/fonts/Montserrat/Montserrat-Regular.ttf) format("truetype");
  }


  body {
    margin: 0;
  }
</style>