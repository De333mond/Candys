<template>
  <div class="login-form-wrapper">
    <div class="form-container fl gap-1 f-col">
      <my-input :error="hasError" v-model="username" label="Имя пользователя" type="text"/>
      <my-input :error="hasError" v-model="password" label="Пароль" type="password"/>
      <router-link class="text-link" to="/register">Нет аккаунта? Зарегистрироваться</router-link>
      <my-button @click="onSubmit">Войти</my-button>
    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";

export default {
  name: "LoginPage",
  components: {MyButton, MyInput},
  data() {
    return {
      username: 'Dezzy',
      password: 'root',
      hasError: false,
      previousPath: null,
    }
  },

  created () {
    this.previousPath = this.$router.options.history.state.back
  },

  methods: {
    onSubmit () {
      this.$store.dispatch("AuthModule/onLogin", {
        username: this.username,
        password: this.password,
      }).then(() => {
        this.hasError = this.$store.state.hasError;
        if (!this.hasError)
          this.$router.push(this.prevRoutePath)
      })
    },
  },

  computed: {
    prevRoutePath() {
      return this.previousPath ? this.previousPath : '/home'
    }
  },

}
</script>

<style lang="scss" scoped>

 .login-form-wrapper {
   width: 40%;
   margin: 15% auto;
   padding: 10px;
   box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
   border-radius: 15px;
 }


 .form-container {
   margin: 40px 30px;
 }
 .text-link {
   font-family: Nunito;
   font-size: 14px;
   color: #EB5C54;
 }

</style>