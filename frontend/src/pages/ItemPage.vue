<template>
  <div class="page-wrapper">
    <div v-if="isProductsFetched" class="fl item-card-container">
      <div class="fl item__image-wrapper">
        <img :src="item.image" class="item__image">
      </div>
      <div class="fl f-col item__information">
        <div class="item__information-wrapper">
          <h2>{{ item.title }}</h2>
          <p><span class="item-page__description">{{item.description}}</span></p>
          <MyInput v-if="item.category.canHaveTitle" label="Добавить надпись на торт?" v-model="additionalInfo.title"/>

          <div v-if="hasFillings" class="fl f-col">
            <label for="select-filling">Выбрать начинку</label>
            <select name="select-filling" v-model="additionalInfo.fillingId">
              <option :value="-1">Нет</option>
              <option
                v-for="(fill) in item.available_fillings"
                :key="fill.id"
                :value="fill.id"
              >{{ fill.title }} (+{{ fill.price_delta}} Р)</option>
            </select>
          </div>
        </div>
        <div class="fl item__controls-container">
          <div class="fl count-wrapper">
            <v-counter @changed="(count) => {this.additionalInfo.quantity = count}"/>
            <span class="item__controls__price">{{totalPrice}} Р</span>
          </div>
          <my-button class="add-to-cart-btn" @click="addToCourt">В корзину</my-button>
        </div>
      </div>
    </div>
    <h1>Популярные товары</h1>
    <ProductList :products="popularItems"/>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";
import VCounter from "@/components/UI/v-counter";
import ProductList from "@/components/ProductList";
import {mapState} from "vuex";

export default {
  name: "ItemPage",
  components: {ProductList, VCounter, MyButton, MyInput},
  data() {
    return {
      additionalInfo: {
        title: '',
        quantity: 1,
        fillingId: -1,
      },
    }
  },

  computed: {
    ...mapState("ProductsModule", [
        "products",
    ]),

    item() {
      return this.products.filter(el => el.id === Number(this.$route.params.id))[0]
    },

    popularItems() {
      const limit = 4;
      return this.products.filter((el, i) => i < limit)
    },

    isProductsFetched() {
      return this.products.length > 0
    },

    hasFillings() {
      try {
        return this.item.available_fillings.length > 0
      }
      catch (e) {
        return false
      }
    },

    totalPrice() {
      let price = this.item.price;

      if (this.item.available_fillings && this.additionalInfo.fillingId >= 0)
        price += this.item.available_fillings.filter((el) => (el.id === this.additionalInfo.fillingId))[0].price_delta

      if (this.additionalInfo.title.length > 0)
        price += 250

      price = price  * this.additionalInfo.quantity;
      return price;
    }
  },

  beforeMount() {
    this.$store.dispatch("ProductsModule/fetchProducts")
    console.log(this.item.category)
  },

  methods: {
    addToCourt() {
      this.$store.dispatch("CourtModule/addItem", {item: this.item.id, additionalInfo: {
          title: this.additionalInfo.title.length > 0 ? this.additionalInfo.title : null,
          quantity: this.additionalInfo.quantity,
          fillingId: this.additionalInfo.fillingId !== -1 ? this.additionalInfo.fillingId : null,
        }})
    }
  },
}
</script>

<style lang="scss">
  .item-card-container {
    border-radius: 15px;
    box-shadow: 0 5px 10px rgba(0,0,0,.25);
    overflow: hidden;
    width: 80%;
    margin: 30px auto;
  }

  .item__image-wrapper {
    justify-content: center;
    align-items: center;
    overflow: hidden;
    width: 400px;
    height: 400px;

    img {
      height: 100%;
      margin: auto;
    }
  }

  .item__information-wrapper {
    width: 100%;
  }

  .item__information {
    margin: 10px 20px 20px;
    box-sizing: border-box;
    width: 50%;
    justify-content: space-between;

    label {
      font-family: Nunito;
      font-size: 14px;
    }

    select {
      border: 1px solid #EB5C54;
      border-radius: 2px;
      padding: .5em;
      outline: none;
    }

    select option {
      font-family: Nunito;
      font-size: 14px;
    }
  }

  .item__controls-container {
    justify-content: space-between;
    align-items: center;
  }

  .item__controls__price {
    font-family: Nunito;
    color: #EB5C54;
    font-size: 18px;
    font-weight: bold;
  }

  .count-wrapper {
    align-items: center;
  }
  .item-page__description {
    font-family: Nunito;
    font-size: 18px;
  }
</style>