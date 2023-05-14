<template>
  <h1>User page</h1>
  <my-button @click="onLogOut">Log out</my-button>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
export default {
  name: "UserPage",
  components: {MyButton},
  methods: {
    onLogOut(){
      this.$store.dispatch('AuthModule/onLogout')
    }
  },
}
</script>

<style scoped>

</style>