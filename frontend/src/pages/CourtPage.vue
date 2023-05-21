<template>
  <div class="page-wrapper">
    <div class="court-content" v-if="courtLength > 0">
      <table class='court-table' v-if="isProductsFetched">
        <tr>
          <th></th>
          <th>Название</th>
          <th>Цена</th>
          <th>Количество</th>
          <th>Сумма</th>
          <th></th>
        </tr>
        <ui-court-item
            v-for="(courtItem, index) in courtItems"
            :key="courtItem.item"
            :products="products"
            :court-item="courtItem"
            :index="index"
            @priceChanged="(value) => totalCourtPrice += value"
        />
        </table>
      <div class="total-wrapper">
        <hr>
        <h3>Всего: {{ totalCourtPrice }}</h3>
      </div>
      <my-button @click="$router.push('/order')">Перейти к оформлению</my-button>
    </div>
    <div v-else class="court-content">
      <h1>Товаров пока что нет в корзине :(</h1>
      <MyButton @click="$router.push({name: 'products'})">Перейти в каталог</MyButton>
    </div>
  </div>
</template>


<script>
import MyButton from "@/components/UI/MyButton";
import {mapGetters, mapState} from "vuex";
import UiCourtItem from "@/components/UI/ui-court-item";
export default {
  name: "CourtPage",
  computed: {
    ...mapState('CourtModule', [
      'courtItems'
    ]),

    ...mapGetters('CourtModule', [
        "courtLength",
    ]),

    ...mapState('ProductsModule', [
      "products"
    ]),

    isProductsFetched(){
      return this.products.length > 0
    }
  },

  components: {UiCourtItem, MyButton},

  data() {
    return {
      totalCourtPrice: 0,
    }
  },

  beforeMount() {
    this.totalCourtPrice = 0;
    this.$store.dispatch('ProductsModule/fetchProducts')
  },
}
</script>

<style lang="scss" scoped>
  .court-table {
    width: 80%;
    margin: 0 auto;
    table-layout: fixed;
    border-spacing: 20px;
  }

  th {
    font-family: Nunito;
    color: #4f4f4f;
    font-size: 20px;
  }
  .total-wrapper {
    display: flex;
    flex-direction: column;
    justify-content: left;
    width: 80%;
    margin: 0 10%;
  }

  .court-content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

</style>