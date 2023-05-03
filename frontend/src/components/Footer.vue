<template>
  <div class="footer">
    <div class="row">
      <div class="column">
        <h2>Клиентам</h2>
        <ul>
          <li><FooterLink to="#" content="О нас"/></li>
          <li><FooterLink to="#" content="Доставка"/></li>
          <li><FooterLink to="#" content="На заказ"/></li>
        </ul>
      </div>
      <div class="column">
        <h2>Контакты</h2>
        <ul>
          <li><FooterLink to="#" content="+7 (912)-345-67-89"/></li>
          <li><FooterLink to="#" content="info@candys.com"/></li>
          <li><FooterLink to="#" content="Бережковская наб. 20, стр. 23"
          /></li>
        </ul>
      </div>
      <div class="column">
        <h2>Candys в соц. сетях</h2>
        <ul>
          <li><FooterLink to="#" content="ВКонтакте"/></li>
          <li><FooterLink to="#" content="Телеграмм"/></li>
          <li><FooterLink to="#" content="Инстаграмм"/></li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="">
        <p>&copy; {{ currentYear }} Candys</p>
      </div>
    </div>
  </div>
</template>

<script>
import FooterLink from "@/components/FooterLink";
export default {
  name: "CandysFooter",
  components: {FooterLink},
  data() {
    return {
      currentYear: new Date().getFullYear()
    }
  }
}
</script>

<style>
.footer {
  width: 100%;
  background-color: #F4D0A8;
  padding: 10px 10%;
  box-sizing: border-box;
  text-align: center;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.row {
  width: 80%;
  display: flex;
  justify-content: space-around;
  align-items: stretch;
}

.column {
  padding: 0 20px;
  width: 80%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  text-align: center;
}


h2 {
  font-size: 22px;
  margin-bottom: 10px;
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

li {
  font-size: 18px;
  margin-bottom: 10px;
}
</style>
