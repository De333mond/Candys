<template>
  <div class="page-wrapper fl f-col">
    <h1>Торты и десесерты с доставкой</h1>
    <ImageSlider style="width: 100vw"/>
    <h1>Акции</h1>
    <ProductList :products="onSaleLimited"/>
    <h1>Категории</h1>
    <CategoryList/>
    <h1>О нас</h1>
    <TextSection style="margin-top: -60px;">
      &emsp;&emsp;Нас зовут Юля и Марина, мы дружили, мечтали, готовили вместе с первого класса. С октября 2012 года мы начали готовить торты и десерты для своих друзей и коллег по работе. Вкус наших десертов вызывал полнейший восторг, который побудил бросить офисную работу и открыть свою онлайн-кондитерскую <span style="color: #EB5C54; font-size: 24px;">Candys</span>. Сейчас мы выросли в настоящее кондитерское производство, в котором помимо нас работает еще 16 человек. Наш кондитерский цех отвечает всем нормам, в нём мы ежедневно творим для вас торты и десерты на заказ!
    </TextSection>
  </div>
</template>

<script>
import ProductList from "@/components/ProductList";
import ImageSlider from "@/components/UI/ImageSlider";
import CategoryList from "@/components/CategoryList";
import TextSection from "@/components/UI/TextSection";
import {mapGetters} from "vuex";
export default {
  name: "MainPage",
  components: {TextSection, CategoryList, ImageSlider, ProductList},
  computed: {
    ...mapGetters('ProductsModule', [
      "getOnSale",
    ]),
    onSaleLimited() {
      return this.getOnSale.filter((el, i) => i < 8);
    },
  },

  mounted() {
    console.log(this.getOnSale, this.getOnSale == null)
    this.$store.dispatch("ProductsModule/fetchProducts")
  }
}
</script>

<style scoped>
  .content-wrapper {
    align-items: center;
    gap: 70px 0;
    padding: 70px 0;
  }
</style>