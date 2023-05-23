<template>
  <div class="login-form-wrapper">
    <div class="form-container fl gap-1 f-col">
      <my-input  v-model="username" label="Имя пользователя" type="text"/>
      <my-input  v-model="password" label="Пароль" type="password"/>
      <my-input
          :error="!passwordsEqual"
          error-message="Введены разные пароли"
          v-model="confirmPassword"
          label="Повторите пароль"
          type="password"/>
      <router-link class="text-link" to="/login">Войти</router-link>
      <my-button @click="onSubmit">Зарегистрироваться</my-button>
    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput";
import MyButton from "@/components/UI/MyButton";

export default {
  name: "register-page",
  components: {MyButton, MyInput},
  data() {
    return {
      username: 'Dezzy',
      password: '',
      confirmPassword: '',
      previousPath: null,
    }
  },

  created () {
    this.previousPath = this.$router.options.history.state.back
  },

  methods: {
    onSubmit () {
      if (!this.passwordsEqual)
        return

      this.$store.dispatch("AuthModule/onSignUp", {
        username: this.username,
        password: this.password,
        re_password: this.confirmPassword
      })
    },
  },

  computed: {
    prevRoutePath() {
      return this.previousPath ? this.previousPath : '/home'
    },
    passwordsEqual() {
      return this.password === this.confirmPassword
    }
  },

}
</script>

<style scoped>

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