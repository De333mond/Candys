<template>
  <div class="page-wrapper">
    <div class="fl item-card-container">
      <div class="fl item__image-wrapper">
        <img :src="item.image" class="item__image">
      </div>
      <div class="fl f-col item__information">
        <div class="item__information-wrapper">
          <h2>{{ item.title }}</h2>
          <p>{{item.description}}</p>
          <MyInput label="Добавить надпись на торт?" v-model="additionalInfo.title"/>

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
import axios from "axios";
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";
import VCounter from "@/components/UI/v-counter";
import ProductList from "@/components/ProductList";

export default {
  name: "ItemPage",
  components: {ProductList, VCounter, MyButton, MyInput},
  data() {
    return {
      item: {},
      additionalInfo: {
        title: "",
        quantity: 1,
        fillingId: -1,
      },
      popularItems: [],
    }
  },

  mounted() {
    axios
        .get(`http://localhost:8000/api/products/${this.$route.params.id}/`)
        .then((response) => {
          this.item = response.data
        })
        .catch((e) => {
          if (e.response.status == 404)
            this.$router.push({name: "404"})
          else
            console.error(e)
      })
    axios.get('http://127.0.0.1:8000/api/products/on_sale/?limit=4')
        .then(response => {
          this.popularItems = response.data;
        })
        .catch(error => {
          console.log(error);
        });
  },

  computed: {
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

  methods: {
    addToCourt() {
      this.$store.dispatch("CourtModule/addItem", {item: this.item, additionalInfo: this.additionalInfo})
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

</style>