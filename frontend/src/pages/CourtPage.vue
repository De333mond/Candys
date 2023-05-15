<template>
  <div class="page-wrapper">
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
</template>


<script>
import MyButton from "@/components/UI/MyButton";
import {mapState} from "vuex";
import UiCourtItem from "@/components/UI/ui-court-item";
export default {
  name: "CourtPage",
  components: {UiCourtItem, MyButton},

  data() {
    return {
      totalCourtPrice: 0,
    }
  },

  computed: {
    ...mapState('CourtModule', [
        'courtItems'
    ]),

    ...mapState('ProductsModule', [
        "products"
    ]),

    isProductsFetched(){
      return this.products.length > 0
    }
  },

  beforeMount() {
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

</style>