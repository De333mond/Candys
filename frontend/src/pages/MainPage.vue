<template>
  <div class="page-wrapper fl f-col">
    <CandysHeader/>
    <h1>Торты и десесерты с доставкой</h1>
    <ImageSlider/>
    <h1>Акции</h1>
    <ProductList :products="products"/>
    <h1>Категории</h1>
    <CategoryList/>
    <h1>О нас</h1>
    <TextSection style="margin-top: -60px;">
      &emsp;&emsp;Нас зовут Юля и Марина, мы дружили, мечтали, готовили вместе с первого класса. С октября 2012 года мы начали готовить торты и десерты для своих друзей и коллег по работе. Вкус наших десертов вызывал полнейший восторг, который побудил бросить офисную работу и открыть свою онлайн-кондитерскую <span style="color: #EB5C54; font-size: 24px;">Candys</span>. Сейчас мы выросли в настоящее кондитерское производство, в котором помимо нас работает еще 16 человек. Наш кондитерский цех отвечает всем нормам, в нём мы ежедневно творим для вас торты и десерты на заказ!
    </TextSection>
    <CandysFooter/>
  </div>
</template>

<script>
import CandysHeader from "@/components/Header";
import CandysFooter from "@/components/Footer";
import ProductList from "@/components/ProductList";
import ImageSlider from "@/components/UI/ImageSlider";
import axios from "axios";
import CategoryList from "@/components/CategoryList";
import TextSection from "@/components/UI/TextSection";
export default {
  name: "MainPage",
  components: {TextSection, CategoryList, ImageSlider, ProductList, CandysFooter, CandysHeader},
  data() {
    return {
      products: []
    }
  },

  mounted() {
    axios.get('http://127.0.0.1:8000/api/products/on_sale/?limit=8')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.log(error);
        });
  }
}
</script>

<style scoped>
  .page-wrapper  {
    gap: 70px 0;
    align-items: center;
    width: 100%;
  }
</style>