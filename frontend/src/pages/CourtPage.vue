<template>
  <table>
    <tr>
      <th>image</th>
      <th>title</th>
      <th>Цена</th>
      <th>Количество</th>
      <th>Сумма</th>
      <th>Delete</th>
    </tr>
    <tr 
        v-for="courtItem in courtItems"
        :key="courtItem.item.id"
    >
      <td><img :src="courtItem.item.image" alt=""></td>
      <td>{{ courtItem.item.title}}</td>
      <td>{{ courtItem.item.price }}</td>
      <td><v-counter v-model="courtItem.additionalInfo.quantity"/></td>
      <td>{{ getTotalPrice(courtItem) }}</td>
      <td><my-button @click="onDelete"><img src="@/assets/images/icons/delete.png" alt=""></my-button></td>
    </tr>
    </table>
  <my-button @click="$router.push('/order')">Make order</my-button>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import VCounter from "@/components/UI/v-counter";
import {mapState} from "vuex";
export default {
  name: "CourtPage",
  components: {VCounter, MyButton},
  data() {
    return {

    }
  },

  computed: {
    ...mapState("CourtModule", [
        'courtItems'
    ])
  },

  methods: {
    getTotalPrice(courtItem) {
      let price = courtItem.item.price;

      if (courtItem.additionalInfo.fillingId)
        price += courtItem.item.availableFillings.filter((fill) => {fill.id === courtItem.additionalInfo.fillingId})[0].price_delta

      if (courtItem.additionalInfo.title)
        price += 250

      price = price  * courtItem.additionalInfo.quantity;
      return price;
    },

    onDelete() {
      console.error("Deletion isnt work now")
    }
  },

  watch: {
    courtItems() {
      console.log(this.courtItems)
    }
  }
}
</script>

<style scoped>

</style>