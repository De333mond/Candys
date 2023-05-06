<template>
  <div v-if="true" class="product-list-filter-container">
    <div class="product-list_section">
      <div
          class="filter-title-container"
          @click="categoriesCollapsed = !categoriesCollapsed"
      >
        <h3>Категория</h3>
      </div>
        <ul v-show="!categoriesCollapsed">
          <li
              v-for="item in categories"
              :key="item.id"
              @click="config.category = item; this.$emit('changed', this.config)"
              :class="{'filter-item-active': item === config.category}"
          >
            <div class="filter-item"><span class="filter-item-text">{{ item.title }}</span></div>
          </li>
        </ul>
    </div>
    <hr>
    <div class="product-list_section">
      <div
          class="filter-title-container"
          @click="ordersCollapsed = !ordersCollapsed;"
      >
        <h3>Сортировка</h3>
      </div>
        <ul v-show="!ordersCollapsed">
          <li
            v-for="item in order_filters"
            :key="item"
            @click="onOrderClick(item)"
            :class="{'filter-item-active': config.order === item.value}"
          >
            <div class="filter-item"><span class="filter-item-text">{{ item.title }}</span></div>
          </li>
        </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductListFilter",
  data() {
    return {
      categoriesCollapsed: true,
      ordersCollapsed: true,
      categories: [
          {id: 0, title: "Все"},
      ],

      order_filters: [
        {
          title: "Сначала недорогие",
          value: "cheep",
        },
        {
          title: "Сначала дорогие",
          value: "expensive",
        },
        {
          title: "Сначала по акции",
          value: "sale",
        },
        {
          title: "Сначала новинки",
          value: "new"
        }
      ],

      config: {
        category: null,
        order: null,
      }
    }
  },

  methods: {
    onOrderClick(item) {
      if (item.value !== this.config.order) {
        this.config.order = item.value;
      }
      else {
        this.config.order = null;
      }
      this.$emit("changed", this.config)
    }
  },

  mounted() {
    axios.get("http://127.0.0.1:8000/api/categories/")
        .then(response => {
          this.config.category = this.categories[0]
          this.categories = this.categories.concat(response.data)
        }).catch(e => {
          console.log(e)
    })
  }
}
</script>

<style scoped>
  .product-list-filter-container {
    width: 250px;
    height: fit-content;
    border-radius: 5px;
    box-shadow: 0 0 16px rgba(0,0,0, .2);
    overflow: hidden;
  }

  .product-list-filter-container h3 {
    margin: 0;
  }

  .product-list_section li {
    margin: 0;
  }

  .filter-item, .filter-title-container {
    padding: 15px 20px;
    transition: .1s ease;
  }

  .filter-item:hover, .filter-title-container:hover {
    background-color: #EB5C54;
  }

  .filter-item-active {
    background-color: #c94d46;
  }

  .filter-item-text {
    font-family: Nunito;
    margin-left: 10px;
    font-size: 17px;
  }

</style>