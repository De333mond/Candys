<template>
  <div class="fl counter">
    <button class="counter-button" @click="dec">
      <img src="@/assets/images/icons/minus-icon.svg" alt="-">
    </button>
    <input type="text" :value="count" @input="$emit('changed', $event.target.value)">
    <button class="counter-button" @click="inc">
      <img src="@/assets/images/icons/plus-icon.svg" alt="+">
    </button>
  </div>
</template>

<script>
export default {
  name: "v-counter",

  data() {
    return {
      count: 1,
    }
  },

  methods: {
    dec() {
      if (this.count > 0) {
        this.count -= 1;
        this.$emit('changed', this.count);
      }
    },
    inc() {
      this.count += 1;
      this.$emit('changed', this.count);
    }
  },
}
</script>

<style lang="scss" scoped>
  .counter {
    width: 100px;
  }

  .counter-button {
    border: 1px solid #EB5C54;
    border-radius: 0;
    display: flex;
    align-items: center;
    background-color: #fff;
    padding: 7px;
    transition: .2s ease;

    img {
      width: 10px;
      color: #EB5C54;
    }

    &:hover {
      background-color: #EB5C54;
    }
  }

  .counter {
    input {
      font-family: Nunito;
      font-size: 16px;
      border: 1px solid #EB5C54;
      border-radius: 0;
      width: 30%;
      text-align: center;

      &:focus {
        outline: none;
      }
    }
  }



</style>