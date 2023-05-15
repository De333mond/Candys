<template>
  <div class="product-page-content fl f-row">
    <ProductListFilter @changed="onFilterChanged" :filter="this.$route.query.filter"/>
    <div class="product-list-wrapper">
      <ProductList :products="sortedProducts"/>
    </div>
  </div>
</template>

<script>
import ProductList from "@/components/ProductList";
import ProductListFilter from "@/components/ProductListFilter";
import {mapState} from "vuex";
export default {
  name: "ProductsPage",
  components: {ProductListFilter, ProductList},
  data() {
    return {
      filterConfig: {
        category: null,
        order: null,
      },
    }
  },

  methods: {
    onFilterChanged(config) {
      this.filterConfig = config
    }
  },

  computed: {
    ...mapState("ProductsModule",[
        "products",
    ]),
    sortedProducts: function() {
      function compare(a, b) {
        switch (this.order){
          case "cheep": return a.price - b.price
          case "expensive": return b.price - a.price
          case "sale":
            if (a.adv_state === "sale")
              return -1;
            else if (b.adv_state === "sale")
              return 1;
            else return 0;
          case "new":
            if (a.adv_state === "new")
              return -1;
            else if (b.adv_state === "new")
              return 1;
            else return 0;
        }
      }
      let sortFunc = compare.bind(this.filterConfig)
      if (this.filterConfig.category !== null) {
        return this.products
            .filter(item => {
              return this.filterConfig.category.id === 0 ||
              this.filterConfig.category.id ===
              item.category.id
            })
            .sort(sortFunc)
      }
      else
        return this.products

    }
  },

  mounted() {
    this.$store.dispatch("ProductsModule/fetchProducts");
  },
}
</script>

<style scoped>
  .product-list-wrapper {
    width: 80%;
  }

  .product-page-content {
    padding: 35px 0;
    justify-content: space-around;
    /*margin-right: 30px;*/
  }
</style>