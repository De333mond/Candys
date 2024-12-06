<template>
  <div class="slider-item">
    <img :src="image">
  </div>
</template>

<script>
export default {
  name: "SliderItem",
  props: {
    image: String
  },

}
</script>

<style scoped>
  img {
    width: 100vw;
  }
</style>