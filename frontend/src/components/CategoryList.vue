<template>
  <div class="fl f-row category-container">
    <CategoryItem
        v-for="item in categories"
        :key="item.id"
        :category="item"
    />
  </div>
</template>

<script>
import CategoryItem from "@/components/CategoryItem";
import axios from "axios";
export default {
  name: "CategoryList",
  components: {CategoryItem},
  data() {
    return {
      categories: [],
    }
  },


  mounted() {
    //TODO: add limit to api
    axios.get('http://127.0.0.1:8000/api/categories/')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.log(error);
        });
  }
}
</script>

<style scoped>
  .category-container {
    width: 80%;
    margin: 0 10%;
    justify-content: space-between;
    text-align: center;
  }
</style>