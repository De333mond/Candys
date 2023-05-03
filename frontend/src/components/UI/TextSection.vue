<template>
  <div class="about-us-container">
    <p class="about-us-text">
      <slot></slot>
    </p>
  </div>
</template>

<script>
export default {
  name: "TextSection",
}
</script>

<style scoped>
  .about-us-text {
    font-family: Nunito;
    font-size: 24px;
  }

  .about-us-container {
    width: 80%;
    margin: 0 10%;
  }
</style>