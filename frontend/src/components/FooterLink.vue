<template>
  <a :href="to">{{content}}</a>
</template>

<script>
export default {
  name: "FooterLink",
  props: ['to', 'content']
}
</script>

<style scoped>
a {
  color: black; /* initial color */
  transition: color 0.3s ease; /* smooth transition */
  text-decoration: none;
  font-family: 'Montserrat';
  font-style: normal;
  font-weight: 600;
  font-size: 18px;
  line-height: 29px;
}

a:hover {
  color: #EB5C54; /* color on hover */
}

</style>