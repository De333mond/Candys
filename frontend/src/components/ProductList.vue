<template>
  <div class="list-wrapper fl">
    <ProductCard
          v-for="(item, index) in products"
          :key="index"
          :item="item"
          class="product-list-item"
      />
  </div>
</template>

<script>
import ProductCard from "@/components/ProductCard";

export default {
  name: "ProductList",
  components: {ProductCard},

  props: {
    products: {
      type: Array,
      required: true,
    }
  },

  computed: {
  },
}
</script>

<style scoped>
  .list-wrapper {
    flex-wrap: wrap;
    justify-content: flex-start;
    gap: 70px 20px;
  }


</style>