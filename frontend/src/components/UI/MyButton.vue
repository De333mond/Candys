<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "MyButton"
}
</script>

<style scoped>
  button {
    padding: 5px 10px ;
    color: #EB5C54;
    background-color: white;
    border: 1px solid #EB5C54;
    border-radius: 1px;
    font-size: 16px;
    transition: 0.1s ease-in;
  }

  button:hover {
    background-color: #EB5C54;
    color: white;
  }
</style>