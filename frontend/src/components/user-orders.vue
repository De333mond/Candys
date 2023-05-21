<template>
  <table class="user-orders-table">
    <tr>
      <th>Дата доставки</th>
      <th>Тип доставки</th>
      <th>Статус</th>
      <th>Сумма</th>
    </tr>
    <ui-order-row
      v-for="order in orders"
      :key="order.id"
      :order="order"
    />
  </table>
</template>

<script>
import UiOrderRow from "@/components/UI/ui-order-row";
export default {
  name: "user-orders",
  components: {UiOrderRow},

  props: {
    orders: Array
  },
}
</script>

<style scoped>
.user-orders-table {
  table-layout: fixed;
  width: 100%;
  border-radius: 15px;
  box-shadow: 0 4px 8px rgba(0,0,0,.25);
  padding: 20px;
}
</style>