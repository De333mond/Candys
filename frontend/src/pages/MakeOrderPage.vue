<template>
  <div class="page-wrapper">
    <div class="form-block">
      <div class="fl f-col order__form-wrapper">
        <form @submit.prevent="submitForm">

          <my-input
              :error="v$.orderData.delivery_address.$dirty && v$.orderData.delivery_address.$invalid"
              v-model.trim="v$.orderData.delivery_address.$model"
              label="Адрес доставки"
              error-message="Заполните это поле!"
          />
          <div class="fl f-col order-block">
            <label class="label-font" for="delivery-select">Способ доставки</label>
            <select name="select delivery-select" class="select" v-model="orderData.pickup">
              <option selected value="delivery">Доставка</option>
              <option value="pickup">Самовывоз</option>
            </select>
          </div>

          <div class="order-block">
            <input type="checkbox" name="as-faster-delivery" v-model="orderData.asFaster">
            <label class="label-font" for="as-faster-delivery">Как можно скорее</label>
          </div>

          <my-input
              v-if='!orderData.asFaster'
              type="datetime-local"
              label="Время доставки"
              v-model="orderData.delivery_date"
          />

          <div class="fl f-col order-block">
            <label class="label-font" for="payment-select">Способ оплаты</label>
            <select name="payment-select" class="select" v-model="orderData.payment">
              <option selected value="card">Онлайн</option>
              <option value="money">Наличные</option>
            </select>
          </div>
          <my-textarea label="Комментарий к заказу" v-model="orderData.comment"></my-textarea>
          <my-button type="submit">{{ orderData.payment === 'card' ? "Перейти к оплате" : "Заказать" }}</my-button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import MyInput from "@/components/UI/MyInput";
import MyTextarea from "@/components/UI/MyTextarea";
import MyButton from "@/components/UI/MyButton";
import axios from "axios";
import {mapGetters, mapState} from "vuex";
import {formatDate} from "@/utils";
import useVuelidate from "@vuelidate/core";
import {DefaultAPIInstance} from "@/api";
const { required, minLength} = require('vuelidate/lib/validators')

export default {
  name: "MakeOrderPage",
  components: {MyButton, MyTextarea, MyInput},
  setup () {
    return {
      v$: useVuelidate()
    }
  },
  data() {
    return {
      orderData: {
        delivery_address: '',
        delivery_date: null,
        asFaster: true,
        comment: "",
        pickup: 'delivery',
        payment: 'card',
      },
    }
  },

  validations() {
    return {
      orderData: {
        delivery_address: {required,},
      }
    }
  },

  computed: {
    ...mapState("AuthModule", [
      'credentials',
      "currentUser",
      'userInfo'
    ]),
    ...mapGetters("CourtModule", [
        "courtLength"
    ])
  },

  methods: {
    submitForm() {
      if (this.orderData.delivery_date === null)
        this.orderData.delivery_date = formatDate(new Date())

      this.v$.$touch()
      if (this.v$.orderData.$invalid || this.courtLength === 0)
        return

      let apiInstance = axios.create({
        headers: {
          "Authorization": "Token " + this.credentials.token,
          "Content-Type": "application/json"
        }
      })

      apiInstance.post('http://localhost:8000/api/orders/', {
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Token " + this.credentials.token
        },
        ...this.orderData,
        "user": this.currentUser.id,
      }).then(resp => {
        this.$store.dispatch("CourtModule/makeOrder", {orderId: resp.data.id, token: this.credentials.token})
        if (resp.status === 201)
          this.$router.push("/successful")
      }).catch(e => console.log(e))
    }
  },

  watch: {
    userInfo() {
      console.log(this.userInfo)
      if (this.userInfo !== null)
        console.log(this.userInfo.delivery_adress)
        this.orderData.delivery_address = this.userInfo.delivery_adress
    }
  },

  beforeMount() {
    this.$store.dispatch("AuthModule/fetchUserInformation")
  },
}
</script>

<style lang="scss" scoped>

.order-block {
  margin: 20px 0;
}


.form-block {
  display: flex;
  flex-direction: column;
  //align-items: start;
  border-radius: 15px;
  padding: 20px;
  width: 40%;
  margin: 0 auto;
  box-shadow: 0 4px 8px rgba(0, 0, 0, .25);
}

.select {
  border: 1px solid #EB5C54;
  border-radius: 2px;
  padding: 0.5em;
  outline: none;
}
</style>