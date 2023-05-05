<template>
  <div class="header-wrapper">
    <div class="logo-wrapper" @click="$router.push({name: 'home'})">
      <img class="logo-icon-img" src="../assets/images/icons/logo-icon.png">
      <img class="logo-title-img" src="../assets/images/icons/logo-title.png">
    </div>
    <div class="navbar-wrapper">
      <CandysNavlink class="nav-link" content="Акции"/>
      <CandysNavlink class="nav-link" @click="$router.push('products')" content="Каталог"/>
      <CandysNavlink class="nav-link" @click="$router.push('custom')" content="На заказ"/>
      <CandysNavlink class="nav-link" @click='$router.push("about-us")' content="О нас"/>
    </div>
    <div class="ico-buttons-wrapper">
      <img src="../assets/images/icons/basket.png" alt="">
      <img src="../assets/images/icons/user.png" alt="">
    </div>
  </div>
</template>

<script>
import CandysNavlink from "@/components/UI/Navlink";
export default {
  name: "CandysHeader",
  components: {CandysNavlink}

}
</script>

<style scoped>
  .header-wrapper {
    width: 100%;
    display: flex;
    box-sizing: border-box;
    flex-direction: row;
    padding: 10px;
    justify-content: space-around;
    align-items: center;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  }

  .logo-wrapper {
    display: flex;
    flex-direction: column;
    width: 96px;
    height: 96px;
    align-items: center;
  }

  .navbar-wrapper {
    display: flex;
    flex-direction: row;
    gap: 30px;
  }

  .ico-buttons-wrapper {
    display: flex;
    flex-direction: row;
    height: 64px;
    gap: 20px;
  }

  .logo-icon-img {
    width: 64px;
  }

  img {
    height: 100%;
    width: 100%;
  }

  @media {}
</style>