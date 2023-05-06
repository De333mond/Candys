<template>
  <div class="product-page-content fl f-row">
    <ProductListFilter @changed="onFilterChanged"/>
    <div class="product-list-wrapper">
      <ProductList :products="sortedProducts"/>
    </div>
  </div>
</template>

<script>
import ProductList from "@/components/ProductList";
import axios from "axios";
import ProductListFilter from "@/components/ProductListFilter";
export default {
  name: "ProductsPage",
  components: {ProductListFilter, ProductList},
  data() {
    return {
      products: [],
      filterConfig: null,
    }
  },

  methods: {
    onFilterChanged(config) {
      this.filterConfig = config
    }
  },

  computed: {
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
      if (this.filterConfig !== null)
        return this.products
            .filter(item => {return this.filterConfig.category.id === 0 || this.filterConfig.category.id === item.category})
            .sort(sortFunc)
      else
        return this.products

    }
  },

  mounted() {
    axios.get('http://127.0.0.1:8000/api/products/')
      .then(response => {
        this.products = response.data;
      })
      .catch(error => {
        console.log(error);
      });
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