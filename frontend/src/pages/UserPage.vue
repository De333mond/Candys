<template>
  <div class="page-wrapper">
    <div class="block">
      <form @submit.prevent="onSubmit">
        <div class="form-container fl f-col gap-1">

          <div class="personal-info-container fl gap-2">
            <my-input label="Имя" v-model="form.first_name"/>
            <my-input label="Фамилия" v-model="form.last_name"/>
          </div>

          <my-input label="Email" v-model="form.email"/>

          <div>
            <input class='input-checkbox' name="receive-emails" type="checkbox" v-model="form.receiveEmails"/>
            <label for="reсeive-emails" class="label-font">Получать Email с акциями</label>
          </div>

          <my-input type="date" label="Дата рождения" v-model="form.birthdate"/>
          <my-input label="Адрес доставки" v-model="form.address"/>
          <div class="fl gap-3">
            <my-button type="submit">Сохранить</my-button>
            <my-button @click="onLogOut">Выйти</my-button>
          </div>
        </div>
      </form>
    </div>
    <user-orders v-if="hasOrders" :orders="orders"/>
  </div>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import MyInput from "@/components/UI/MyInput";
import UserOrders from "@/components/user-orders";
import {DefaultAPIInstance} from "@/api";
import {mapState} from "vuex";
import login from "@/pages/Login";

export default {
  name: "UserPage",
  components: {UserOrders, MyButton, MyInput},
  data() {
    return {
      orders: [],
      form: {
        first_name: "",
        last_name: "",
        email: "",
        receiveEmails: false,
        address: "",
        birthdate: null,
      },
    }
  },
  computed: {
    ...mapState("AuthModule", [
      "currentUser",
    ]),

    hasOrders() {
      return this.orders.length > 0
    }
  },

  methods: {

    onLogOut(){
      this.$store.dispatch('AuthModule/onLogout')
      this.$router.push("/")
    },

    onSubmit() {
      this.$store.dispatch("AuthModule/updateUserInformation", {
        customer: {
          "delivery_adress": this.form.address,
          "get_emails": this.form.receiveEmails,
          "birthdate": this.form.birthdate,
          "user": this.currentUser.id,
        },
        user: {
          "first_name": this.form.first_name,
          "last_name": this.form.last_name,
          "email": this.form.email,
        }
      })
    }
  },

  beforeMount() {
    this.$store.dispatch('AuthModule/fetchUserInformation')
  },

  watch: {
  currentUser() {
    if (!this.currentUser)
      return

    this.form.email = this.currentUser.email
    this.form.first_name = this.currentUser.first_name
    this.form.last_name = this.currentUser.last_name

    DefaultAPIInstance
        .get("http://localhost:8000/api/customers/" + this.currentUser.customer + "/")
        .then(resp => {
          this.form.receiveEmails = resp.data.get_emails
          this.form.address = resp.data.delivery_adress
          this.form.birthdate = resp.data.birthdate
        })

    DefaultAPIInstance
        .get("http://localhost:8000/api/orders/by_user/?id=" + this.currentUser.id)
        .then(resp => this.orders = resp.data)
        .catch(e => console.log(e))
    },
  }
}
</script>

<style lang="scss" scoped>

.block {
  width: 60%;
  border-radius: 20px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.25);
  padding: 15px;
}

.form-container {
  align-items: flex-start;

  .personal-info-container {
    width: 100%;
  }
}

</style>