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

  mounted() {
    console.log(this.image)
  }


}
</script>

<style scoped>
  img {
    width: 100vw;
  }
</style>