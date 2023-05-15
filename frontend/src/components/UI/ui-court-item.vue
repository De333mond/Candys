<template>
  <tr class="court-item">
    <td>
      <div class="court-item-image-wrapper" @click="$router.push('item/' + courtItem.item)">
        <img :src="item.image" alt="">
      </div>
    </td>
    <td><span class="court-item-text court-item__title">{{ item.title }}</span></td>
    <td>
      <div class="td-container-align-center"><span class="court-item-text">{{ item.price }}</span></div>
    </td>
    <td class="td-counter" >
      <div class="td-container-align-center">
        <v-counter :initial="courtItem.additionalInfo.quantity" @changed="countChanged"/>
      </div>
    </td>
    <td>
      <div class="td-container-align-center"><span class="court-item-text">{{ totalPrice }}</span>
      </div>
    </td>
    <td>
      <div class="td-container-align-center">
        <my-button class="delete-button" @click="onDelete"><img src="@/assets/images/icons/delete.png" alt=""></my-button>
      </div>
    </td>
  </tr>
  <ul v-if="hasAdditions" class="court-additional-info">
    <li v-if="this.courtItem.additionalInfo.title !== null"><span class="court-item-text">Надпись: {{ courtItem.additionalInfo.title }}</span></li>
    <li v-if="this.courtItem.additionalInfo.fillingId !== null">
      <span class="court-item-text">Начинка: {{ fillingTitle }}</span>
    </li>
  </ul>
</template>

<script>
import VCounter from "@/components/UI/v-counter";
import MyButton from "@/components/UI/MyButton";
export default {
  name: "ui-court-item",
  components: {MyButton, VCounter},
  props: {
    courtItem: Object,
    products: Object,
    index: Number,
  },


  computed: {
    item() {
      return this.products.filter(el => el.id === this.courtItem.item)[0]
    },

    totalPrice() {
      let price = this.item.price

      if (this.courtItem.additionalInfo.title)
        price += 250


      if (this.courtItem.additionalInfo.fillingId !== -1 && this.courtItem.additionalInfo.fillingId)
        price += this.item.available_fillings.filter((el) => (el.id === this.courtItem.additionalInfo.fillingId))[0].price_delta

      price *= this.courtItem.additionalInfo.quantity
      return price
    },

    fillingTitle() {
      return this.item.available_fillings.filter((el) => (el.id === this.courtItem.additionalInfo.fillingId))[0].title
    },

    hasAdditions() {
      return this.courtItem.additionalInfo.title !== null || this.courtItem.additionalInfo.fillingId !== null
    }
  },

  methods: {
    countChanged(value) {
      this.$store.dispatch("CourtModule/setItemQuantity", {index: this.index, quantity: value});
    },

    onDelete() {
      this.$emit("priceChanged", -this.totalPrice)
      this.$store.dispatch("CourtModule/deleteItem", this.courtItem)
    }
  },
  watch: {
    totalPrice(newValue, oldValue) {
      this.$emit("priceChanged", newValue - oldValue)
    }
  },

  mounted() {
    this.$emit("priceChanged", this.totalPrice)
  }
}
</script>

<style lang="scss" scoped>

  .court-item, .court-additional-info{
    box-shadow: 0 4px 12px rgba(0,0,0,.125);
    border-radius: 15px;
    width: 100%;
    overflow: hidden;
    //padding-right: 20px;
    padding: 0;
    box-sizing: border-box;
  }

  .court-additional-info {
    padding: 10px;
    width: 300px;
    margin-left: 30px;
  }

  .court-item-image-wrapper {
    width: 128px;
    height:128px;
    overflow: hidden;
    position: relative;
    border-radius: 15px;

    img {
      height: 100%;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  }


  .delete-button {
    border: none;
    img {
      width: 24px;
    }
  }

  .court-item__title {
    max-width: 250px;
    display: flex;
    text-align: left;
  }

  .td-container-align-center {
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .court-item-text {
    font-family: Nunito;
    size: 14px;
  }

  td {
    padding: 0;
  }


</style>