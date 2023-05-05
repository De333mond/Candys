<template>
  <nav>
    <a class="navlink">{{ content }}</a>
  </nav>
</template>

<script>
export default {
  name: "CandysNavlink",
  props: {
    content: String,
  }
}
</script>

<style lang="scss" scoped>

.navlink {
  color: #3b3b3b; /* initial color */
  transition: color 0.1s ease; /* smooth transition */
  text-decoration: none;
  position: relative; /* needed for the line effect */
  font-family: "Nunito";
  font-style: normal;
  font-weight: 400;
  font-size: 28px;
  line-height: 36px;
}

.navlink:before {
  content: "";
  position: absolute;
  width: 100%;
  height: 2px;
  bottom: -2px; /* put the line under the text */
  background-color: #EB5C54;
  visibility: hidden; /* hide the line by default */
  transform: scaleX(0); /* scale it to 0 by default */
  transition: all 0.1s ease-out; /* smooth transition */
}

.navlink:hover {
  color: #EB5C54; /* change color on hover */
}

.navlink:hover:before {
  visibility: visible; /* show the line on hover */
  transform: scaleX(1); /* scale it to full width on hover */
}

</style>
