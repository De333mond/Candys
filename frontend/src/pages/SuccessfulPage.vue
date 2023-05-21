<template>
  <div class="page-wrapper">
    <div class="block fl f-col">
      <img src="../assets/images/icons/successful.png" alt="successful">
      <h2>Оплата прошла успешно!</h2>
<!--      <my-button @click="$router.push('/')">Вернуться на главную страницу</my-button>-->
    </div>
  </div>
</template>

<script>
export default {
  name: "SuccessfulPage",
}
</script>

<style lang="scss" scoped>

.block {
  box-shadow: 0 4px 8px rgba(0,0,0,.25);
  border-radius: 15px;
  padding: 20px;
  width: 40%;
  margin: 100px auto;
  box-sizing: border-box;
  align-items: center;
  gap: 10px;
  img {
    width: 60%;
  }
}

</style>