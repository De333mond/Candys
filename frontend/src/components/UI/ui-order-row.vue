<template>
  <tr>
    <td>{{formattedDate}}</td>
    <td>{{ formattedPickup }}</td>
    <td>Обработка платежа</td>
    <td>{{order.total_sum}}</td>
  </tr>
</template>

<script>
import dayjs from 'dayjs';
export default {
  name: "ui-order-row",
  props: {
    order: Object,
  },

  computed: {
    formattedDate() {
      return dayjs(this.order.delivery_date).format('DD.MM.YYYY HH:mm')
    },

    formattedPickup() {
      return this.order.pickup === "delivery" ? "Доставка" : "Самовывоз"
    }

  }
}
</script>

<style scoped>

  td {
    padding: 10px 0;
    font-family: Nunito;
    text-align: center;
  }
</style>