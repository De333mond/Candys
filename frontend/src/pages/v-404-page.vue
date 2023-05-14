<template>
  <div class="page-wrapper">
    <div class="fl f-col not-found-image-container">
      <h1>Такого тортика у нас нет ((</h1>
      <img src="../assets/gifs/404.gif">
      <my-button @click="$router.push({name: 'home'})">Вернуться домой</my-button>
    </div>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
export default {
  name: "v-404-page",
  components: {MyButton}

}
</script>
<style lang="scss">
  .not-found-image-container {

    align-items: center;

    img {
     width: 600px;
    }
  }


</style>