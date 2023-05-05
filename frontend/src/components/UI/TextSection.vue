<template>
  <div class="text-section-wrapper fl">
    <p class="text-section-p">
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
  .text-section-p {
    font-family: Nunito;
    font-size: 24px;
    margin: 0;
  }

  .text-section-wrapper {
    width: 100%;
    padding: 15px;
    box-sizing: border-box;
  }


</style>