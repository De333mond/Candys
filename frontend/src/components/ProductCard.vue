<template>
  <div class="product-container">
    <div class="image-container" @click="$router.push('/item/' + item.id)">
      <img :src="item.image" alt="">
      <div v-if="isNotStandard" class="adv-title-container">
        <p v-if="isNotStandard" class="product-type-title">{{ advTitle }}</p>
      </div>
    </div>
      <p>{{ item.title }}</p>
      <div class="product-footer">
        <p class="price">
          <span :class="{sale: isOnSaleWithoutError}">{{ item.price }} P </span>
          <sup v-if='isOnSaleWithoutError' class="old-price">{{ item.oldPrice}}</sup>
        </p>
        <MyButton @click="addToCourt">В корзину</MyButton>
      </div>
  </div>
</template>

<script>

import MyButton from "@/components/UI/MyButton";
export default {
  name: "ProductCard",
  components: {MyButton},
  data() {
    return {
    }
  },

  props: {
    item: {
      type: Object,
      required: true,
    },
  },

  computed: {
    isNotStandard() {
      return this.item.adv_state !== "no"
    },

    isOnSaleWithoutError() {
      return this.item.price < this.item.oldPrice && this.item.adv_state === "sale"
    },

    advTitle() {
      if (this.item.adv_state === "sale")
        return "Акция"
      else if (this.item.adv_state === "new")
        return "Новинка"
      return ""
    }
  },



  methods: {
    addToCourt() {
      let additionalInfo = {
        title: null,
        fillingId: null,
        quantity: 1
      }
      this.$store.dispatch("CourtModule/addItem", {item: this.item, additionalInfo})
    }
  }

}


</script>

<style scoped>
  .product-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 0px 10px 5px;
    gap: 32px;

    box-sizing: border-box;

    width: 280px;
    height: 440px;

    background: #FFFFFF;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
  }

  .product-container:hover {
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.3);
  }

  .image-container {
    position: relative;
    width: 280px;
    height: 280px;
    overflow: hidden;
  }

  .image-container img {
    height: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }


  p {
    margin: 0;
    text-align: center;
    font-family: "Nunito";
    font-size: 20px;
  }

  .product-footer {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;

    gap: 60px;

    width: 264px;
    height: 50px;
  }

  .adv-title-container {
    background-color: #EB5C54;
    padding: 2px 7px;
    border-radius: 0 0 15px 0;
    position: absolute;
  }

  .adv-title-container p {
    margin: 0;
    color: white;
    font-size: 17px;
  }

  .old-price {
    font-size: 14px;
    text-decoration: line-through;
  }

  .sale {
    color: #EB5C54;
  }

</style>