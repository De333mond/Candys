<template>
  <div class="page-wrapper">
    <h1>Заказать индивидуальный торт</h1>
    <TextSection>
      <p>Мы в Candys предлагаем нашим клиентам возможность заказать <span class="highlighted">индивидуальный торт</span> или десерт, который будет соответствовать их пожеланиям и потребностям. Мы готовы пойти на любые эксперименты и реализовать самые <span class="highlighted">смелые идеи</span> наших клиентов.</p>
      <p>Важно отметить, что <span class="highlighted">качество</span> нашей продукции всегда на высшем уровне. Мы используем только <span class="highlighted">натуральные</span> и <span class="highlighted">качественные</span> ингредиенты, чтобы обеспечить нашим клиентам <span class="highlighted">лучшее вкусовое и эстетическое впечатление</span>.</p>
      <p>Мы также очень <span class="highlighted">клиентоориентированы</span> и стремимся удовлетворить все потребности и желания наших клиентов. Однако, такие заказы требуют много времени и труда, поэтому <span class="highlighted">сроки</span> могут быть достаточно большими. Рекомендуем обращаться к нам за индивидуальным заказом заранее, чтобы мы могли подготовиться и реализовать проект в срок.</p>
      <p>Мы готовы принять вызов и создать торт или десерт, который будет соответствовать самым <span class="highlighted">смелым фантазиям</span> наших клиентов. Не стесняйтесь обращаться к нам с любыми вопросами или идеями, мы всегда рады новым вызовам.</p>
    </TextSection>

    <div class="custom-form-container">
      <h2>Отправить заявку</h2>
      <form action="" class="custom-form fl f-col">
        <div class="custom-input-wrapper">
          <MyInput v-model="number" label="Номер телефона" placeholder="+7(9**)** ** ***"/>
          <MyInput v-model="date" label="Дата" type="datetime-local"/>
        </div>
        <MyTextarea v-model="comment" label="Комментарий"/>
        <div class="custom-form__button">
          <my-button type="submit">Отправить</my-button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import TextSection from "@/components/UI/TextSection";
import MyButton from "@/components/UI/MyButton";
import MyInput from "@/components/UI/MyInput";
import MyTextarea from "@/components/UI/MyTextarea";
export default {
  name: "CustomOrderPage",
  components: {MyTextarea, MyInput, MyButton, TextSection},
  data() {
    return {
      number: "",
      date: Date.now(),
      comment: "",
    }
  }
}
</script>

<style scoped>

  .custom-form-container {
    width: 80%;
    margin: 0 10%;
    padding: 20px;
    box-shadow: 0px 8px 16px rgba(0, 0, 0, .25);
    border-radius: 25px;
  }


  .custom-input-wrapper {
    width: 30%;
  }

  .custom-form__button {
    width: 10%;
  }


</style>