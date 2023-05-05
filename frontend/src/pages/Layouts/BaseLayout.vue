<template>
  <CandysHeader/>
  <router-view></router-view>
  <CandysFooter/>
</template>

<script>
import CandysHeader from "@/components/Header";
import CandysFooter from "@/components/Footer";
export default {
  name: "BaseLayout",
  components: {CandysFooter, CandysHeader}
}
</script>

<style scoped>

</style>