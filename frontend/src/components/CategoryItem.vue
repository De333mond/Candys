<template>
  <div class="category-item-container">
    <div class="cat-image-wrapper">
      <img :src="category.image">
    </div>
    <h2 class="cat-title">{{ category.title }}</h2>
  </div>
</template>

<script>
export default {
  name: "CategoryItem",
  props: {
    category: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>

  .cat-image-wrapper {
    width: 240px;
    height: 240px;
    overflow: hidden;
    border-radius: 50%;

    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);
    transition: all .3s ease;
  }

  .cat-image-wrapper:hover {
    box-shadow: 0px 6px 14px rgba(0, 0, 0, 0.35);
  }
  .cat-image-wrapper:hover + .cat-title {
    color: #EB5C54;
  }

  .cat-image-wrapper img {
    height: 100%;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .cat-title {
    transition: all .3s ease;
  }





</style>