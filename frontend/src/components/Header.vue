<template>
  <div class="header-wrapper">
    <div class="logo-wrapper" @click="$router.push({name: 'home'})">
      <img class="logo-icon-img" src="../assets/images/icons/logo-icon.png">
      <img class="logo-title-img" src="../assets/images/icons/logo-title.png">
    </div>
    <div class="navbar-wrapper">
      <CandysNavlink class="nav-link" @click="$router.push('/products/?filter=sale')" content="Акции"/>
      <CandysNavlink class="nav-link" @click="$router.push('/products')" content="Каталог"/>
      <CandysNavlink class="nav-link" @click="$router.push('/custom')" content="На заказ"/>
      <CandysNavlink class="nav-link" @click='$router.push("/about-us")' content="О нас"/>
    </div>
    <div class="ico-buttons-wrapper">
      <div class="court-wrapper">
        <div class="court-items-count-wrapper">
          {{ courtLength }}
        </div>
        <img src="../assets/images/icons/basket.png" alt="" @click="$router.push('/court')">
      </div>
      <img src="../assets/images/icons/user.png" alt="" @click="$router.push('/me')">
    </div>
  </div>
</template>

<script>
import CandysNavlink from "@/components/UI/Navlink";
import {mapGetters} from "vuex";

export default {
  name: "CandysHeader",
  components: {CandysNavlink},
  computed: {
    ...mapGetters("CourtModule",[
      "courtLength",
    ])
  }
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
    width: 64px;
  }

  .court-wrapper {
    display: flex;
    align-items: flex-end;
    flex-direction: column;
    justify-content: end;
  }

  .court-items-count-wrapper {
    position: absolute;
    background-color: #EB5C54;
    padding: 5px 10px;
    border-radius: 15px;
    color: white;
    /*top: 64px;*/
    /*left: 0;*/
  }

</style>